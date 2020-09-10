import requests, re, json, random
from bs4 import BeautifulSoup
from re import match
from urllib.parse import urlparse
from urllib.parse import quote, unquote, re

hander = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Language': 'id,en-US;q=0.7,en;q=0.3',
	'Connection': 'keep-alive',
	'Upgrade-Insecure-Requests': '1',
	'Pragma': 'no-cache',
	'Cache-Control': 'no-cache',
	'TE': 'Trailers',
}

def getStr(string,start,end, index = 1):
	try:
		str = string.split(start)
		str = str[index].split(end)
		return str[0]
	except:pass
	
def img(query):
	imagedata = []
	link = requests.get("https://api.qwant.com/api/search/images",
	    params={
        	'count': 50,
        	'q': query,
        	't': 'images',
        	'safesearch': 1,
        	'locale': 'en_US',
        	'uiv': 4
	    },
	    headers = {
    		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
	    }
	)
	response = link.json().get('data').get('result').get('items')
	urls = [link.get('media') for link in response]
	for cok in urls:
	   ret = {
	   	"result": "%s"%(cok),
	   	"Status": "OKE COK___!",
	   	"creator":"geo, rey and Fino"
	   }
	   imagedata.append(ret)
	return(imagedata)

def randomimg(query):
	link = f"https://source.unsplash.com/random/900×700/?{query}"
	res = requests.get('https://tinyurl.com/api-create.php?url=%s' % link)
	result = {
		"linkUrl": res.text,
		"creator": "geo",
		"status": "OKE COK___!"
	}
	return(result)

def artiName(nama):
	try:
		dsa ="http://primbon.com/arti_nama.php?nama1={}&proses=+Submit%21+".format(nama)
		response = requests.get(dsa, headers=headers).text
		anu = getStr(response, '<b>ARTI NAMA</b><br><br>', '<TABLE>')
		text=str(anu).replace("<b><i>",": ").replace("</i></b>","").replace("<br><br>","").replace(".<br><br>","").replace("memiliki arti:","")
		result = {
			"result":{
				"arti": text,
				"name": nama
			},
			"creator": "geo",
			"status": "OKE COK___!"
		}
		return(result)
	except:
		result = {"result": "Error info id Iine denmas_geo"}
		return(result)
		
def goSearch(query):
    headers = {"user-agent" : hander}
    resp = requests.get(f"https://google.com/search?q={query}", headers=headers)
    if resp.status_code == 200:
    	soup = BeautifulSoup(resp.content, "html.parser")
    	results = []
    	for g in soup.find_all('div', class_='r'):
    		anchors = g.find_all('a')
    		if anchors:
    		  link = anchors[0]['href']
    		  title = g.find('h3').text
    		  item = {
    		  	"title": title,
    		  	"link": link
    		  }
    		  results.append(item)
    	return(results)
