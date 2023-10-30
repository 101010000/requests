#urllib
# （1）一个类型和六个方法
# （2）get请求 quote() urlencode()
# （3）post请求 百度翻译
# （4）ajax的get请求
# （5）ajax的post请求
# （6）cookie登录 微博
# （7）代理 快代理

#requests
# （1）一个类型和六个属性
# （2）get请求
# （3）post请求
# （4）代理
# （5）cookie  破解验证码

import requests
url = 'https://www.baidu.com/s'

data = {
    'wd':'北京'
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.207.132.170 Safari/537.36'
}
#params 参数 kwargs字典
response = requests.get(url=url,params=data,headers=headers)
print(response.text)
#总结：
# 参数使用params传递
# 参数无需urlencode编码
# 不需要请求对象的定制
# 请求资源路径中的？可加可不加