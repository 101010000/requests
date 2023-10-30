import requests
url = 'http://www.baidu.com/s?'
data = {
    'wd':'ip'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.207.132.170 Safari/537.36'
}
proxy = {
    'http':'140.124.72.74:8088'
}
response = requests.get(url,params=data,headers=headers,proxies=proxy)
content = response.text
with open('request/daili.html','w',encoding='utf-8') as fp:
    fp.write(content)