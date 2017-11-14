# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DingdianItem(scrapy.Item):
    # define the fields for your item here like:
    #书籍名字
    name = scrapy.Field()
    #作者
    author = scrapy.Field()
    #书籍 地址
    book_url = scrapy.Field()
    #书籍状态
    serialstatus = scrapy.Field()
    #书籍字数
    serialnumber = scrapy.Field()
    #书籍类别
    category = scrapy.Field()
    #书籍编号
    name_id = scrapy.Field()