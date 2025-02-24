import requests


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Access-Control-Allow-Headers": "Origin, Content-Type, Accept, Authorization",
    "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
    "Access-Control-Allow-Origin": "*",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "http://103.20.220.93:5000/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}
cookies = {
    "courseEvaluationFilled": "true"
}
def get(teacher='',course=""):
    url = "http://103.20.220.93:5000/search"
    params = {
        "course_name": course,
        "instructor": teacher
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params, verify=False)
    res = [' '.join(i.values()) for i in response.json()]
    return res

if __name__ =='__main__':
    print(get(teacher='卢本伟',course=''))