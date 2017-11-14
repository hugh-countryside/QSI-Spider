import pymysql




db = pymysql.connect("localhost","root","123456","python")
cursor=db.cursor()
print('链接上')
sql = 'INSERT INTO dd_name("xs_name","xs_author","category","name_id") VALUES({%s,%s,%s,%s})'
value = {
    'xs_name':'圣墟',
    'xs_author':'辰东',
    'category':'玄幻',
    'name_id':'2'
     }
cursor.execute(sql,value)
cursor.close()
# class Sql:
#     @classmethod
#     def insert_dd_name(cls,xs_name,xs_author,category,name_id):
#         sql = 'INSERT INTO dd_name("xs_name","xs_author","category","name_id") VALUES(%s,%s,%s,%s)'
#         value = {
#             'xs_name':xs_name,
#             'xs_author':xs_author,
#             'category':category,
#             'name_id':name_id
#         }
#         cursor.execute(sql,value)
#         cursor.close()
#     @classmethod
#     def select_name(cls,xs_name):
#         sql = "SELECT EXISTS(SELECT 1 FROM dd_name WHERE xs_name = %s)"
#         value = {
#             'xs_name':xs_name
#         }
#         cursor.execute(sql,value)
#         return cursor.fetchall()[0]