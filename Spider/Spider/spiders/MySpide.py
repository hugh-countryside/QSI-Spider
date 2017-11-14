import scrapy
from bs4 import BeautifulSoup
from scrapy import Request

from Spider.items import DingdianItem


class MySpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["23wx.cc"]
    bash_url = 'http://www.23wx.cc/class/'
    bashurl = '.html'

    def start_requests(self):
        for i in range(1, 11):
            url = self.bash_url + str(i) + '_1' + self.bashurl
            yield Request(url, self.parse)
        yield Request('http://www.23wx.cc/quanben/1', self.parse)

    def parse(self, response):
        # print(response.text)
        # 获取最大数值
        max_num = BeautifulSoup(response.text,'lxml').find('div',class_='pagelink').find_all('a')[-1].text
        bashurl = str(response.url)[:-1]
        print(max_num)
        for num in range(1,int(max_num)+1):
            url = bashurl + str(num)
            yield Request(url,callback=self.get_name)
    def get_name(self,response):
        tds =  BeautifulSoup(response.text,'lxml').find_all('tr')[1:]
        for td in tds:
            novelName = td.find('a').text
            novelUrl = td.find('a')['href']
            name_id = str(novelUrl)[-6:-1]
            yield Request(novelUrl,callback=self.get_chapterurl,meta={'name':novelName,'url':novelUrl,'name_id':name_id})
    def get_chapterurl(self,response):
        item = DingdianItem()
        item['name'] = str(response.meta['name'].replace('\xa0',''))
        item['book_url'] = response.meta['url']
        category = BeautifulSoup(response.text,'lxml').find('div',id='con_top')
        author = BeautifulSoup(response.text,'lxml').find('div',id='info').find_all('p')[0].text
        item['category'] = str(category).replace('/','')
        item['author'] = str(author).replace('/','')
        item['name_id'] = 12
        return item