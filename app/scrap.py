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
	   imagedata.append(cok)
	ret = {
    	"linkUrl": "%s"%(imagedata),
    	"creator": "geo, rey and Fino",
    	"Status": "OKE COK___!"
	}
	return(ret)

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
		anu = line.getStr(response, '<b>ARTI NAMA</b><br><br>', '<TABLE>')
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
		result = {"linkUrl": "Error info id Iine denmas_geo"}
		return(result)
def instaprofile(user):
    uReq = requests
    bSoup = BeautifulSoup
    website = uReq.get("https://www.instagram.com/{}/".format(str(user)))
    data = bSoup(website.content, "lxml")
    for getInfoInstagram in data.findAll("script", {"type":"text/javascript"})[3]:
        getJsonInstagram = re.search(r'window._sharedData\s*=\s*(\{.+\})\s*;', getInfoInstagram).group(1)
        data = json.loads(getJsonInstagram)
        for instagramProfile in data["entry_data"]["ProfilePage"]:
    	    username = instagramProfile["graphql"]["user"]["username"]
    	    name = instagramProfile["graphql"]["user"]["full_name"]
    	    picture = instagramProfile["graphql"]["user"]["profile_pic_url_hd"]
    	    biography = instagramProfile["graphql"]["user"]["biography"]
    	    followers = instagramProfile["graphql"]["user"]["edge_followed_by"]["count"]
    	    following = instagramProfile["graphql"]["user"]["edge_follow"]["count"]
    	    private = instagramProfile["graphql"]["user"]["is_private"]
    	    media = instagramProfile["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]
    	    result = {
    			"result": {
    				"username": username,
    				"fullname": name,
    				"bio": biography,
    				"followers": followers,
    				"following": following,
    				"media": media,
    				"private": private,
    				"profile_img": picture
    			}
    		}
    	    return(result)
