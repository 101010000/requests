#通过登录接口我们发现登录的时候需要参数很多
# __VIEWSTATE: ggu2SAw3CgJWxT6qwvy4EAu4Joicb7z32ijKtlWy9viymdW3O9IlnsFDiRYK9hWbwryyNePgynF3E+SnbqKHrU4JctEalzN//2gWEicW/IIILNBhzirRjfyjNNe8xsO2Dhr9Eh85is6ocqMbj7vCUl8jz0k= #变量
# __VIEWSTATEGENERATOR: C93BE1AE  #变量
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 13545278436
# pwd: lz0607..
# code:  #变量
# denglu: 登录
#难点：
# 1、__VIEWSTATE、__VIEWSTATEGENERATOR查找
# 2、验证码code查找
# 3、session的返回
import requests
import urllib.request
from bs4 import BeautifulSoup
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.207.132.170 Safari/537.36'
}
response = requests.get(url=url,headers=headers)
content = response.text
soup = BeautifulSoup(content,'lxml')
viewstate = soup.select("#__VIEWSTATE")[0].attrs.get("value")
viewstategenerator = soup.select("#__VIEWSTATEGENERATOR")[0].attrs.get("value")
code_url = "https://so.gushiwen.cn" + soup.select("#imgCode")[0].attrs.get("src")#验证码code查找
#获取验证码到本地的图片之后 下载到本地 如何观察验证码 然后再控制台输入这个验证码 就可以将这个值给code参数 就可以登录
#有坑 可以用Session
# urllib.request.urlretrieve(code_url,"code.png")
#requests里面有一个方法Session(),通过session的返回值 就可以使请求变成一个对象
session = requests.Session()
#验证码url的内容
response_code = session.get(code_url)
#此时要使用二进制数据 因为我们要使用的是图片的下载 【注意】
content_code = response_code.content
with open("requests/code.jpg","wb") as fp:
    fp.write(content_code)
code_name = input("请输入验证码：")
#点击登录
url_post = "https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx"
data_post = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '13545278436',
    'pwd': 'lz0607..',
    'code': code_name, 
    'denglu': '登录',
}
#session返回的是同一个
response_post = session.post(url=url_post,data=data_post,headers=headers)
content_post = response_post.text
with open("requests/gushiwen.html","w",encoding="utf-8") as fp:
    fp.write(content_post)
print("登录成功")