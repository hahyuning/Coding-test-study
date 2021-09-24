import requests
import json

# get 방식
host = "https://search.naver.com"
# r = requests.get(url)

path = "/search.naver"
params = {"query":"hello"}

url = host + path
response = requests.get(url, params=params)

# print(response.status_code)
# print(response.url)
# print(response.text)
# print(response.content)
# print(response.encoding)
# print(response.headers)

# data = response.json()
# data = response.raise_for_status()

# 봇 감지
url = "http://www.ichangtou.com/#company:data_000008.html"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"}
response = requests.get(url, headers=headers)
print(response.content)

# post 방식
data = {"key":"val"}
r = requests.post("https://httpbin.org/post", data=data)

url = "https://api.github.com/some/endpoint"
payload = {"some":"data"}
r = requests.post(url, json=payload)


# curl 읽는 법
# -d: data와 함께 전달할 파라미터값 설정
# -f: files
# -j: json
# -H: header
# -A: 헤더의 user-agent 안내
# -X: 요청시 필요한 메소드 방식 안내
# -G: 전송할 사이트 url 및 ip 주소
# -i: 사이트의 header 정보만 가져오기
# -I: 사이트의 header 와 바디 정보를 함께 가져오기
# -u: 사용자 정보

json1 = '{"id": 1, "name": "hello"}'
jsonObject = json.loads(json1)
print(jsonObject.get("name"))

json2 = '{"id": 1, "name": ["hello", "world"]}'
jsonObject = json.loads(json2)
jsonArray = jsonObject.get("name")
for list in jsonArray:
    print(list)

json3 = '{"id": 1, "info": {"name": "hello", "email": "world@gmail.com"}}'
jsonObject = json.loads(json3)
print(jsonObject.get("info").get("email"))

json4 = '{"id": 1, "info": [{"name": "helloalpaca", "email": "jms393497@gmail.com"}, {"name": "choppermask", "email": "abcde@abcde.com"}]}'
jsonObject = json.loads(json4)
jsonArray = jsonObject.get("info")
for list in jsonArray:
    print(list.get("email"))

# file = open('example.json')
# jsonString = json.load(file)
# print(jsonString.get("info"))

# 덤프
json_data = json.dumps(json4, indent=4, sort_keys=True)
print(json_data)