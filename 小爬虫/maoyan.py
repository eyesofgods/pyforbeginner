import requests
import re

def get_information(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36'}
    r = requests.get(url,headers=headers)
    result = re.findall(
        '<a.*?title="(.*?)".*?class="image-link".*?class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>.*?<i class="integer">(.*?)</i><i class="fraction">(.*?)</i></p> ',
        r.text, re.S)
    for i in result:
        with open('top100.txt', 'a',encoding='utf-8') as f:
            f.write(i[0] + ' ' + re.sub('\n\s+', '', str(i[1])) + ' ' + i[2] + ' ' + '评分：' + i[3] + i[4] + '\n')
for i in range(0,110,10):
    url = 'http://maoyan.com/board/4?offset=' + str(i)
    get_information(url)
