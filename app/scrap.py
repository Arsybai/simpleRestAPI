import requests, re, json
from bs4 import BeautifulSoup
from re import match
from urllib.parse import urlparse
from urllib.parse import quote, unquote, re

hander = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

def img(query):
	imagedata = []
	link = 'https://www.google.co.in/search?q={}&source=lnms&tbm=isch'.format(query)
	soup = requests.get(link)
	soup = BeautifulSoup(soup.content,"lxml")
	for clu in soup.findAll('img'):
		if 'textinput' not in clu['src']:
			imagedata.append(clu['src'])
	result = {
		'status':'OK',
                'creato': 'geo, rey, fino'
		'result':imagedata
		}
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
