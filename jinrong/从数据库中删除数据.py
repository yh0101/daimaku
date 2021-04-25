import pymysql
db = pymysql.connect(host='localhost',port=3306,user='root',password='',database='pachong',charset='utf8')

company = '长城汽车'

cur = db.cursor()    # 获取会话指针，用来调用SQL语句
sql = 'DELETE FROM test WHERE company = %s'   # 编写SQL语句

cur.execute(sql,company)   #  执行SQL语句
db.commit()      # 因为改变了数据表结构，这一行必须要写
cur.close()      # 关闭会话指针
db.close()       # 关闭数据库连接
