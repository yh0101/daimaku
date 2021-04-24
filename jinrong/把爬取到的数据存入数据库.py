import requests
import re
import pymysql
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75'}

def baidu(company):
    url = 'https://www.baidu.com/s?rtt=4&bsst=1&cl=2&tn=news&ie=utf-8&word=' + company
    res = requests.get(url,headers=headers).text

    p_href = '<h3 class="news-title_1YtI1"><a href="(.*?)"'
    href = re.findall(p_href, res, re.S)
    p_title = '<h3 class="news-title_1YtI1">.*?>(.*?)</a>'
    title = re.findall(p_title, res, re.S)
    p_date = '<span class="c-color-gray2 c-font-normal">(.*?)</span>'
    date = re.findall(p_date, res)
    p_source = '<span class="c-color-gray c-font-normal c-gap-right">(.*?)</span>'
    source = re.findall(p_source, res)

    for i in range(len(title)):  # range(len(title)),这里因为知道len(title) = 10，所以也可以写成for i in range(10)
        title[i] = title[i].strip()  # strip()函数用来取消字符串两端的换行或者空格，不过这里好像不太需要了
        title[i] = re.sub('<.*?>', '', title[i])  # 核心，用re.sub()函数来替换不重要的内容
        if ('小时' in date[i]) or ('分钟' in date[i]):  # 下面这几行代码是对日期做了一个处理，如果包含小时或者分钟，就转为当天日期
            date[i] = time.strftime("%Y-%m-%d")
        else:
            date[i] = date[i]
        print(str(i + 1) + '.' + title[i] + '  ' + source[i] + '-' + date[i])
        print(href[i])

    for i in range(len(title)):
        db = pymysql.connect(host='localhost',port=3306,user='root',password='',database='pachong',charset='utf8')
        cur = db.cursor()
        sql = 'INSERT INTO test(company,title,href,date,source)VALUES(%s,%s,%s,%s,%s)'
        cur.execute(sql,(company,title[i],href[i],date[i],source[i]))
        db.commit()
        cur.close()
        db.close()

#baidu('上汽集团')
#print('数据爬取并导入数据库成功')
companys = ['阿里巴巴', '海尔智家', '福耀玻璃', '长城汽车', '三一重工']
for company in companys:
    try:
        baidu(company)
        print(company + '数据爬取并导入数据库成功')
    except:
        print(company + '数据爬取并导入数据库失败')
