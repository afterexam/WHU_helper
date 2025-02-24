import time

from DrissionPage import Chromium
import os
import requests
from api.taokela import taokela


print('来自qq:1430097658,本程序免费,造成后果与本人无关,查询接口来自淘课啦,请校园网访问')

# 启动或接管浏览器，并创建标签页对象
tab = Chromium().latest_tab

tab.listen.start('https://jwgl.whu.edu.cn/xsxk/zzxklbb_cxZzxkLbbPartDisplay.html?gnmkdm=N253517')
def extra_left(response,keyword=''):
    for i in response['items']:
        cur_man = i['yxzrs']
        cur_total = i['jxbrl']
        class_name = i['kcmc']
        id = i['jxb_id']
        teacher = i['jsxx'].split('/')[1]
        if cur_man < cur_total and not keyword:
            print(f'{cur_total}>{cur_man} {teacher} 的 {class_name} 有{int(cur_total) - int(cur_man)}个余量了')

        if cur_man < cur_total and keyword in teacher and keyword:
            print(f'{teacher} 的课 {class_name} 有 {int(cur_total) - int(cur_man)}个余量了!')
    if not keyword:
        print('-'*100)
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
    tab.ele('css:#tysfyzdl').click()
    tab.ele('text:查询',timeout=100).click()
    res = tab.listen.wait()

    r = res.request

    headers = r.headers
    cookies = tab.cookies().as_dict()
    params = r.params
    data = r.postData.replace('showCount=15', 'showCount=114514')
    tab.close()
    url = "https://jwgl.whu.edu.cn/xsxk/zzxklbb_cxZzxkLbbPartDisplay.html"

    choose = input('查余量扣1, 查自己有关的课程评价扣2:---->')
    if choose =='1':
        keyword = input('你要哪个老师的课,不需要就直接按空格')
        while True:
            response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data).json()
            extra_left(response,keyword=keyword)
            time.sleep(10)

    elif choose == '2':
        response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data).json()
        extra_info(response)

    else:
        print('别瞎选孩子')

    return res
if __name__ == '__main__':

    _ = main()
    os.system("pause")

