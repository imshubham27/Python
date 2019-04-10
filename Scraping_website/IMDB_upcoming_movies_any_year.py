import requests
from datetime import datetime as dt
from bs4 import BeautifulSoup
import pandas as pd
base_url = requests.get('https://www.imdb.com/movies-coming-soon/?ref_=inth_cs').text

soup = BeautifulSoup(base_url,'html.parser')

all1=soup.find_all("div",{"class":"list_item odd"})
all2=soup.find_all("div",{"class":"list_item even"})


l=[]

for item in all1:
    d={}
    try:
        d["Title"]=(item.find("h4").find("a").text)
    except:
        d["Title"]="Not mentioned"
    try:
        d["Genre"]=(item.find("span").text)
    except:
        d["Genre"]="Not mentioned"
    try:
        d["Description"]=(item.find("div",{"class":"outline"}).text)
    except:
        d["Description"]="Not mentioned"
    try:
        d["Directors"]=(item.find("div",{"class":"txt-block"}).find("span").find("a").text)
    except:
        d["Directors"]="Not mentioned"
    try: 
        d["Running Time"]=(item.find("p",{"class":"cert-runtime-genre"}).find("time").text)
    except:
        d["Running Time"]="Not mentioned"
    print(" ")
    l.append(d)
    
for i in range(dt.now().month+1,13,1):
    print("https://www.imdb.com/movies-coming-soon/2019-"+f"{i:02d}"+"/?ref_=cs_dt_nx")
    web_url = requests.get("https://www.imdb.com/movies-coming-soon/2019-"+f"{i:02d}"+"/?ref_=cs_dt_nx").text
    soup = BeautifulSoup(web_url,'html.parser')
    all1=soup.find_all("div",{"class":"list_item odd"})
    all2=soup.find_all("div",{"class":"list_item even"})
    for item in all1:
        d={}
        try:
            d["Title"]=(item.find("h4").find("a").text)
        except:
            d["Title"]="Not mentioned"
        try:
            d["Genre"]=(item.find("span").text)
        except:
            d["Genre"]="Not mentioned"
        try:
            d["Description"]=(item.find("div",{"class":"outline"}).text)
        except:
            d["Description"]="Not mentioned"
        try:
            d["Directors"]=(item.find("div",{"class":"txt-block"}).find("span").find("a").text)
        except:
            d["Directors"]="Not mentioned"
        try: 
            d["Running Time"]=(item.find("p",{"class":"cert-runtime-genre"}).find("time").text)
        except:
            d["Running Time"]="Not mentioned"
        print(" ")
        l.append(d)
    
df=pd.DataFrame(l)
print(df)
df.to_csv("Output.csv")