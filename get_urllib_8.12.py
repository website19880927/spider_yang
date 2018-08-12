#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2018-2019 @yang.com Corporation Limited.
@contact: 659706575@qq.com
@software: garner
@file: get_urllib_8.12.py
@time: 2018/8/12 0012 13:18
@desc:url发送请求
'''
from urllib import request as req

#通过get请求连接
resp=req.urlopen(url='http://www.baidu.com',timeout=2)
con=resp.read()
with open('baidu.html','ab+') as f:
    f.write(con)
#通过post请求连接获取
from urllib import parse
data={
    'type':'1',
    'username':'17682181102',
    'password':'web121212'
}
# post 请求需要解析编码设置,将字典转换为字符串再转换为二进制
# 转换字符串
data1=parse.urlencode(data)
#转换二进制
data=data1.encode('utf-8')

print('@29',type(data1),type(data))
url='http://www.honestcareer.com/hr/dologin'
#返回的响应对象
resp2=req.urlopen(url,data)
print('@33',resp2,dir(resp2))
print('@34',resp2.code,resp2.info())
#连接对象的状态码
print(resp2.status)
#对象通过read 转换为 二进制数据
con=resp2.read()
print(con)
#再次转换为人读懂的语言
con1=con.decode('utf-8')


from  lxml import etree


html=con.decode('utf-8')
print(type(con),type(html))
#转换为HTML文档格式 ，对象HTML
html=etree.HTML(html)
#通过//div 获取node 获取所有的div
node=html.xpath('//div')
#同[]获取id=u1下面的a标签下面的name=tj_trnews的标签中的 href值,还有文本值
node2=html.xpath('//div[@id="u1"]/a[@name="tj_trnews"]/@href')#['http://news.baidu.com']
node3=html.xpath('//div[@id="u1"]/a[@name="tj_trnews"]/text()')#['新闻']
#取div 和a标签两个都有
node4=html.xpath('//div | //a')
#获取a中的内容使用 contains
node5=html.xpath('//div[@id="u1"] |//a[contains(@name,"tj") and starts-with(@name,"tj_trnews")]')

print(node5)
