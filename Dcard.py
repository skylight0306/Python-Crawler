import urllib.request as req
import bs4

global arr

def getData(url):
    #url = "https://www.dcard.tw/f"

    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"        
    })
    
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    root=bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("h2", class_="sc-1v1d5rx-2 kZjhSU")
    hearts = root.find_all("div", class_="sc-1kuvyve-3 bIYJbX")
 
    for title in titles:
        if title.a != None:
            #if "問卦" in title.a.string:
                arr.append(title.a.string)
    
        
 
    for heart in hearts:
        if heart != None:
            #if "問卦" in title.a.string:
                arr.append(heart.a.string)
        
    





if __name__=='__main__' :
    arr = []
    Pageurl = "https://www.dcard.tw/f"
    getData(Pageurl)
        
        
    f1 = open('C:/Users/09520/OneDrive/桌面/ptt.txt','w')
    for i in range(len(arr)):
        f1.write(arr[i])
        f1.write('\n')

    f1.close()



arr



