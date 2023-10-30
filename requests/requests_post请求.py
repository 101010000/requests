import requests
import json
url = "https://fanyi.baidu.com/sug"
data = {
    'kw':'spider'
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.207.132.170 Safari/537.36"
}
response = requests.post(url=url,data=data,headers=headers)
js_content = json.loads(response.text)
print(js_content)
#总结
# (1)post请求 是不需要编解码
# (2)post请求 参数是data传递
# (3)不需要请求对象的定制