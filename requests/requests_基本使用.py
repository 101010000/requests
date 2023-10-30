import requests
response = requests.get("https://www.baidu.com")
# 一个类型和六个属性
#response类型
# print(type(response))#<class 'requests.models.Response'>

#1.encoding设置响应的编码格式
response.encoding = 'utf-8'
#2.text以字符串形式返回网页源码
print(response.text)
#3.status_code返回状态码
print(response.status_code)
#4.url返回url
print(response.url)
#5.content返回的是2进制的数据
print(response.content)
#6.headers返回的是响应头
print(response.headers)