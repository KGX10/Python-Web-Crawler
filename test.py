import requests,urllib,socket, pprint,os
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
if __name__ == "__main__":
    url = "https://www.firstpost.com/category/sports"
    request = Request(url, headers = {'USer-agent': 'Mozilla/5.0'})
    html = urlopen(request).read()
    # fhand = urllib.request.urlopen(url)
    html = html.decode()
    soup = BeautifulSoup(html,'html.parser')
    contents = soup('div',class_='big-thumb')
    print(contents[0]('div',class_='title-wrap')[0].h3.a.get('href',None))
    print(contents[0]('div',class_='title-wrap')[0].p.text.strip())
    # tag = soup.find_all(class_="article NEWS")
    # print(tag[0].h3.a.text)
    # print(tag[0].p.text)
    # print(tag[0].h3.a.get('href',None))
    # file = open('textfile.txt',mode='a')
    # # file.write(" ")
    # print(os.path.getsize(r"C:\Users\Koustav\Desktop\Projects\Web Crawler\textfile.txt"))