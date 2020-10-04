import urllib.request as req
import bs4

global arr

def getData(url):
    #url 

    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"        
       # ,"cookie":"over18=1"
    })
    
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    root=bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")
    
    for title in titles:
        if title.a != None:
            if "考研" in title.a.string:
                arr.append(title.a.string)
    
        
    nextLink=root.find("a", string="‹ 上頁")
    return nextLink["href"]
        
    





if __name__=='__main__' :
    arr = []
    Pageurl = "https://www.ptt.cc/bbs/graduate/index.html"
    for i in range(10):
        Pageurl = "https://www.ptt.cc" + getData(Pageurl)
        
        
    
    f1 = open('C:/Users/09520/OneDrive/桌面/ptt.txt','w')
    for i in range(len(arr)):
        f1.write(arr[i])
        f1.write('\n')

    f1.close()
    
arr



