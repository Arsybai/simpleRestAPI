import requests, re, json
from bs4 import BeautifulSoup
from re import match
from urllib.parse import urlparse
from urllib.parse import quote, unquote, re

hander = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

def img(query):
    Image =[]
    url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+query+'&ct=201326592&v=flip'
    result = requests.get(url)
    html = result.text
    pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
    for each in pic_url:
        Image.append(each)
    urel ={
        	"status": "OK",
        	"linkURL": "%s" %(Image)
    }
    return(urel)
    
def searchGoogle(query);
		URL = f"https://google.com/search?q={query}"
		headers = {"user-agent": hander}
		resp = requests.get(URL, headers=headers)
		if resp.status_code == 200:
			soup = BeautifulSoup(resp.content, "html.parser")
			anu =[]
			for g in soup.find_all('div', class_='r'):
				anchors = g.find_all('a')
				anu.append(anchors[0]['href'])
			result ={
				'link': '%s'%(anu),
				'title': '%s'%(g.find('h3').text)
			}
			return(result)
