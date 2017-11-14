from Spider.MySQLPipeline.sql import Sql
from Spider.items import DingdianItem


class DingdianPipelines(object):
    def process_item(self,item,spider):
        if isinstance(item,DingdianItem):
            xs_name = item['xs_name']
            ret = Sql.select_name(self,xs_name)
            if(ret[0] == 1):
                print('已经存在该书籍')
                pass
            else:
                xs_name = item['xs_name']
                xs_author = item['xs_author']
                category = item['category']
                name_id = item['name_id']
                Sql.insert_dd_name(self,xs_name,xs_author,category,name_id)
