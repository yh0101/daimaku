import pymysql
import time

# 连接数据库
db = pymysql.connect(host='localhost', port=3306, user='root', password='', database='pachong', charset='utf8')

# 设定参数
company = '福耀玻璃'     # 设定目标公司
today = time.strftime("%Y-%m-%d")    # 设置当天日期

# 编写SQL语句提取目标公司当天的全部新闻数据
cur = db.cursor()    # 获取会话指针，用来调用SQL语句
sql = 'SELECT * FROM article WHERE company = %s AND date = %s'
cur.execute(sql,(company,today))
data = cur.fetchall()     # 提取所有数据并赋值给变量data
# 计算当天评分
score = 100
for i in range(len(data)):
    score += data[i][5]   # 汇总目标公司当天每条新闻的评分

db.commit()    # 更新数据表，如果对数据表没有修改，可以不写这行
cur.close()    # 关闭会话指针
db.close()     # 关闭数据库连接

print(company + '的今日舆情评分为: ' + str(score))