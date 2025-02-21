

from DrissionPage import Chromium
import os
import requests
from api.taokela import taokela


print('来自qq:1430097658,本程序免费,造成后果与本人无关,查询接口来自淘课啦,校请园网访问')

# 启动或接管浏览器，并创建标签页对象
tab = Chromium().latest_tab

tab.listen.start('https://jwgl.whu.edu.cn/xsxk/zzxklbb_cxZzxkLbbPartDisplay.html?gnmkdm=N253517')
def extra_left(response):
    for i in response['items']:
        cur_man = i['yxzrs']
        cur_total = i['jxbrl']
        class_name = i['kcmc']
        id = i['jxb_id']
        teacher = i['jsxx'].split('/')[1]
        if cur_man < cur_total:
            print(f'{cur_total}>{cur_man} {teacher} 的 {class_name} 有余量了')

def extra_info(response):
    for i in response['items']:
        cur_man = i['yxzrs']
        cur_total = i['jxbrl']
        class_name = i['kcmc']
        id = i['jxb_id']
        teacher = i['jsxx'].split('/')[1]
        info = taokela.get(teacher=teacher, course='')
        if not info:
            continue
        for i in info:
            print(i)
            print()
        print('-'*50)
def main():
    # 跳转到登录页面
    tab.get(f'https://jwgl.whu.edu.cn/xsxk/zzxklbb_cxZzxkLbbIndex.html?gnmkdm=N253517&layout=default&su=')
    tab.ele('text:查询',timeout=100).click()
    res = tab.listen.wait()

    r = res.request

    headers = r.headers
    cookies = tab.cookies().as_dict()
    params = r.params
    data = r.postData.replace('showCount=15', 'showCount=114514')
    tab.close()
    url = "https://jwgl.whu.edu.cn/xsxk/zzxklbb_cxZzxkLbbPartDisplay.html"

    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data).json()
    extra_left(response)
    print()
    print()
    extra_info(response)


    return res
if __name__ == '__main__':

    _ = main()
    os.system("pause")

