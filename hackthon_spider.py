# -*- coding: utf-8 -*-
import urllib.request as req
import bs4
from urllib.parse import quote

global arr
global inf
global web
global img


def getLoc(url): # url = officeweb 
    
    b = b'/:?=&'
    url = quote(url,b )
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36"        
       
    })
    

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    
    root=bs4.BeautifulSoup(data, "html.parser")
    
    
    titles = root.find_all("p",class_="address")
    inf.append(titles[0].string)
    
    pdf = root.find_all("div",class_="gallery-img")
    for i in range(1,len(pdf)):
        img.append(pdf[i]['style'][22:53])






def getData(url): #url = Pageurl
    names = []

    request=req.Request(url, headers={
        "User-Agent":"ozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36"        
        ,"cookie":"XSRF-TOKEN=eyJpdiI6ImF5dVhQXC90TzBOZTNjNlBjNTVuVmdRPT0iLCJ2YWx1ZSI6ImdLV1V2SVpreTJ2ZStJcHk1Rzl5T2ZxOHNGTXFRQ1wvZ3JPd08yY0V6TGFzdU52RjZjdnhoOHBvRFVTMVVQSFhaIiwibWFjIjoiMTk0MjZkMjFjNTI4NzFiZmIxNzNhMjEzYzA1MjM5ZjI4MTJkYmIxZmExZjU0NjI3OTg5NjMzZDk0MDEyZDg3MSJ9"
    })

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    root=bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("a",class_="logProgramClick")

    for title in titles:    #title = titles[1]
        
        officeweb = title['href']
        hasExist = False
        for i in range(1,len(web)): #i =111
            if web[i] == officeweb :
                hasExist = True
        if not hasExist:
            web.append(officeweb)
            getLoc(officeweb)
        names += title.find_all("h3")
       
     
    for i in range(len(names)):  #.append(names.a)
        arr.append(names[i].string)
    
def getLink(num):
    url = "https://www.pickoneplace.com/search/program?county=%E5%8F%B0%E5%8C%97%E5%B8%82&district=%E4%BF%A1%E7%BE%A9%E5%8D%80&page="
    url += str(num)
    

    return url
    


if __name__=='__main__' :
    arr = []
    inf = []
    web = []
    img = []
    Pageurl = "https://www.pickoneplace.com/search/program?uses=&max_people=&county=%E5%8F%B0%E5%8C%97%E5%B8%82&district=%E4%BF%A1%E7%BE%A9%E5%8D%80&maxHrPrice=&minHrPrice=&keywords="

    getData(Pageurl)
    for i in range(2,20):     #i = 2
        Pageurl = getLink(i)
        getData(Pageurl)
        
        

    f1 = open('C:/Users/09520/OneDrive/桌面/office.txt','w',encoding="utf-8")
    len(inf)
    for i in range(1,len(arr)): #i = 1
        f1.write(arr[i])
        f1.write("   ")
        f1.write(inf[i])
        f1.write('\n')

    f1.close()
    f2 = open('C:/Users/09520/OneDrive/桌面/img.txt','w',encoding="utf-8")
    
    for i in range(1, len(img)):
        f2.write(img[i])
    f2.close()
arr



