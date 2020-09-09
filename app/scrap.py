import requests, re, json
from bs4 import BeautifulSoup
from re import match
from urllib.parse import urlparse
from urllib.parse import quote, unquote, re

hander = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

def img(query):
    Image =[]
    r = requests.get("https://api.qwant.com/api/search/images",
    	params={
        	'count': 50,
        	'q': query,
        	't': 'images',
        	'safesearch': 1,
        	'locale': 'en_US',
        	'uiv': 4
    	},
    	headers={
    		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    	}
    )
    response = r.json().get('data').get('result').get('items')
    urls = [r.get('media') for r in response]
    for cok in urls:
    	Image.append(cok)
    ret = {
    	'resulte': {'link': '%s'%(Image)},
    	'creator': 'geo Usa, rey and Fino',
        'status: 'OKE'
    }
    return(ret)
    
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
