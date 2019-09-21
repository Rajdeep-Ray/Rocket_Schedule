import requests
from bs4 import BeautifulSoup 
c=0
for s in range(1,8):
    s=str(s)
    URL = str("https://www.rocketlaunch.live/?page="+s)
    r = requests.get(URL) 
    soup = BeautifulSoup(r.content, 'html.parser') 
    #print(soup.prettify())
    f=soup.find_all("h4",{"itemprop":"name"})
    f1=soup.find_all("div",{"class":"launch_date rlt_date"})
    for j in range(1,len(f),2):
        print(f[j].a.text,end=" : ")
        print(f[j-1].a.text,end=" -> ")
        if(c<len(f1)):
            print(f1[c].a.text)
        else:
            c=0
        print('\n')
        c+=1
