import requests
import os
import re



dirs="D:/妹子图"
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36'}
def mkdir():    #创建文件夹
	if not os.path.exists(dirs):
		os.mkdir('D:/妹子图')
		os.chdir('D:/妹子图')
		print("D:/妹子图")
		return True
	else:
		print("妹子图文件夹已存在")
		return False

def get_max_page():#获取到最大的页面数
	url="https://www.mzitu.com/zipai/"
	r = requests.get(url,headers=headers)
	result=re.findall("<span aria-current='page' class='page-numbers current'>(.*?)</span>",r.text,re.S)
	return result[0]


def find_onepage_imgs(url):#匹配到一个页面里所有的图片地址以及上传时间
        r=requests.get(url,headers=headers)
        result=re.findall('<div class="comment-meta commentmetadata"><a href=".*?">(.*?)</a>.*?</div>.*?<p><img class="lazy".*?data-original="(.*?)".*?</p>',r.text,re.S)
        return result
def download_onepage(onepage_list):
        for j in onepage_list:
                global a
                path0=j[0].split()
                path=path0[0][0:4]+path[0][5:7]+path[0][8:10]+path[1]+path[2][0:2]+path[2][3:5]#把上传时间切片后作为文件名
                img=requests.get(j[1])
                if os.path.exists(path+".jpg"):#因为上传时间可能相同，所以判断一下，如果相同就a+1
                        a=a+1
                        path=path+str(a)
                        with open(path+".jpg", 'wb+') as f:
                                print("下载第"+str(i)+"页提交于"+path0+"的图片")
                                f.write(img.content)
                else:
                        a=1
                        with open(path+".jpg", 'wb+') as f:
                                print("下载第"+str(i)+"页提交于"+path0+"的图片")
                                f.write(img.content)


a=1
if __name__== '__main__':
        mkdir()
        max_page=get_max_page()
        for i in range(int(max_page),1,-1):
                onepage_list=find_onepage_imgs("http://www.mzitu.com/zipai/comment-page-"+ str(i)+"/#comments" )
                download_onepage(onepage_list)
                        
                                
                 
				


