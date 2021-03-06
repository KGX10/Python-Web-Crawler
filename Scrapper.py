from bs4 import BeautifulSoup
import urllib,requests,os
from urllib.request import Request,urlopen

def store_in_file(file,data):
    for line in data:
        file.write(line+'\n')
    file.write("\n\n")

def soup_maker(url):
    request = Request(url, headers = {'USer-agent': 'Mozilla/5.0'})
    html = urlopen(request).read()
    html = html.decode()
    soup = BeautifulSoup(html,'html.parser')
    return soup

if __name__ == "__main__":
    soup = soup_maker('https://in.ign.com/')
    tags = soup.find_all(class_="article NEWS")
    file = open('Web_Data_IGN.txt',mode='a')
    if os.path.getsize(r"C:\Users\Koustav\Desktop\Projects\Web Crawler\Web_Data_IGN.txt") == 0:
        file.write("IGN\n\n")
        for tag in tags:
            store_in_file(file,[tag.h3.a.text,tag.p.text,tag.h3.a.get('href',None)])
        file.write('\n\n')
        file.close()

        soup = soup_maker('https://www.firstpost.com/category/sports')
        contents = soup('div',class_='big-thumb')
        file = open('Web_Data_IGN.txt',mode='a')
        file.write("FIRSTSPORT\n\n")
        for content in contents:
            try:
                header = content('div',class_='title-wrap')[0].h3.a.text
                link = content('div',class_='title-wrap')[0].h3.a.get('href',None)
                textdata = content('div',class_='title-wrap')[0].p.text.strip()
                store_in_file(file,[header,textdata,link])
            except:
                pass
        file.write('\n\n')
        file.close()
    