import requests, re, json, random, pafy, urllib, traceback, base64, urllib, urllib.request, urllib3, html5lib, codecs, string, os, six, ast, time
import youtube_dl
from bs4 import BeautifulSoup
from re import match
from urllib.parse import urlparse
from urllib.parse import quote, unquote, re
from urllib.request import urlopen
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
    
_session = requests.session()
hander = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
}
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
#host = 'https://gxx.line.naver.jp'
#qrEndpoint = '/acct/lgn/sq/v1'
#verifierEndpoint = '/acct/lp/lgn/sq/v1'
	
#=========================================================
def getStr(string,start,end, index = 1):
	try:
		str = string.split(start)
		str = str[index].split(end)
		return str[0]
	except:pass
def tinyurl(query):
    link = "https://tinyurl.com/create.php"
    option = {'url': query, 'submit': 'Make TinyURL!'}
    ghd = requests.post(link,option, headers=headers).text
    urlnya = getStr(ghd,'<div id="success"></div><br><small>[<a href="','" target="_blank" rel="nofollow">')
    return urlnya
    
def apitiny(query):
    link = "https://tinyurl.com/create.php"
    option = {'url': query, 'submit': 'Make TinyURL!'}
    ghd = requests.post(link,option, headers=headers).text
    urlnya = getStr(ghd,'<div id="success"></div><br><small>[<a href="','" target="_blank" rel="nofollow">')
    result = {
        "statu": "OKE COK__!",
        "creator": "Rey",
        "result":{
            "url": "%s" % urlnya
        }
    }
    return(result)
    
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
    #headers = {"user-agent" : hander}
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
    	data ={
    		"result":{
    			"main": results
    		},
    		"creator": "geo, hans, fino",
    		"status": "OKE COK___!"
    	}
    	return(data)
    	
def stafa(search):
	try:
		results = []
		URL = f"https://m.stafabandt.site/mp3/{search}.html"
		resp = requests.get(URL, headers=headers)
		soup = BeautifulSoup(resp.content, "html5lib")
		data = soup.select("a")
		for b in data:
			if "https://m.stafabandt.site/link/" in str(b):
				title = b.get("title")
				link = b.get("href")
				linkny = str(link).replace("https://m.stafabandt.site/link/","").split(".")[0]
				item = {
    		  	"title": title,
    		  	"link": linkny
				}
				results.append(item)
		data ={
			"result":{
				"main": results
			},
			"creator": "geo, hans, fino",
			"status": "OKE COK___!"
		}
		return(data)
	except:
		data = {"result": "Error info id Iine denmas_geo"}
		return(data)
		
def komik(new):
    try:
        data = []
        smule = f"https://komiku.co.id/{new}/"
        resp = requests.get(smule, headers=headers)
        soup = BeautifulSoup(resp.content, "html.parser")
        hh = soup.findAll("div", class_="bgei")
        for idd in hh:
            a = idd.find_all("a")[0]["href"]
            dta = {
                "link": "%s" %(a)
            }
            data.append(dta)
        result = {
            "creator": "geo",
            "status": "OKE COK__!",
            "result": data
        }
        return(result)
    except:
        data = {"result": "Error info id Iine denmas_geo"}
        return(data)
        
def komikRes(new):
    try:
        data = []
        smule = f"{new}"
        resp = requests.get(smule, headers=headers)
        soup = BeautifulSoup(resp.content, "html.parser")
        hh = soup.findAll("div", class_="bc")
        for idd in hh:
            a = idd.find_all("img")
        for xc in a:
            beb = f'{xc["src"]}'
            dta = {
                "link": "%s" %(beb)
            }
            data.append(dta)
        result = {
            "creator": "geo",
            "status": "OKE COK__!",
            "result": data
        }
        return(result)
    except:
        #error = traceback.format_exc()
        result = {"result": "Error info id Iine denmas_geo"}
        return(result)
        
def komikList(query):
    try:
        data =[]
        link = f"{query}"
        resp = requests.get(link, headers=headers)
        soup = BeautifulSoup(resp.content, "html.parser")
        hh = soup.findAll('td', class_='judulseries')[:150]
        if resp.status_code == 200:
            for g in hh:
                Rest = g.find_all('a')[0]["href"]
                res = {
                    "linkResult": Rest
                }
                data.append(res)
            result = {
                "creator": "geo",
                "status": "OKE COK__!",
                "result": data
            }
            return(result)
    except:
        result = {"result": "Error info id Iine denmas_geo"}
        return(result)
def komikSearch(query):
    try:
        data =[]
        smule = f"https://komiku.co.id/?post_type=manga&s={query}"
        resp = requests.get(smule, headers=headers)
        soup = BeautifulSoup(resp.content, "html.parser")
        hh = soup.findAll("div", class_="daftar")
        for idd in hh:
            a = idd.find_all("a")[0]["href"]
            item ={
                "list": "%s" %(a)
            }
            data.append(item)
        result = {
           "creator": "geo",
           "status": "OKE COK__!",
           "result": data
        }
        return(result)
    except:
        result = {"result": "Error info id Iine denmas_geo"}
        return(result)
        
def dlStfa(url):
    try:
        video = f"{url}"
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(video, download=False)
        link = meta['thumbnail'].split("?")[0]
        res = requests.get('https://tinyurl.com/api-create.php?url=%s' % link)
        result = {
            "creator": "geo, hans, fino",
            "status": "OKE COK___!",
            "result":{
                "urlMp3": meta['formats'][0]['url'],
                "urlimg": res.text,
                "title": meta['title']
            },
        }
        return(result)
    except:
        data = {"result": "Error info id Iine denmas_geo"}
        return(data)
def VideoX(search, page):
	try:
	   resulte =[]
	   URL = "https://xnxx.uporbia.com/search/%s/%s"%(search,page)
	   headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"}
	   resp = requests.get(URL, headers=headers)
	   soup = BeautifulSoup(resp.content, "html5lib")
	   hh = soup.findAll('div', class_='thumb')
	   if resp.status_code == 200:
	       hh = soup.findAll('div', class_='thumb')
	       for g in hh:
	           anchors = g.find_all('a')
	           cari = anchors[0]['href'].split("/")[2].replace('_',' ').split("https")[0]
	           title = "{}".format(str(cari))
	           link = "https://xnxx.com"+anchors[0]['href']
	           data ={
	               "link": link,
	               "tilte": title
	           }
	           resulte.append(data)
	       results ={
	           "result":{
	               "main": resulte
	           },
	           "creator": "geo, hans, rey",
	           "status": "OKE CROT",
	           "info": "Gunakan <VPN> sesui karakter anda"
	       }
	       return(results)
	except:
		data = {"result": "Error info id Iine denmas_geo"}
		return(data)
def VideoDL(page):
	try:
	   headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"}
	   r = urllib.request.urlopen(page)
	   rs = r.read().decode();
	   eh ="%s"% getStr(rs,"html5player.setVideoUrlHigh('","');")
	   e ="%s"% getStr(rs,"html5player.setVideoTitle('","');")
	   title = f"{e}"
	   info = "Full videos Have to < VPN / Liff >"
	   link = f"{eh}"
	   res = requests.get('https://tinyurl.com/api-create.php?url=%s' % link)
	   result ={
            "result":{
                "linkUrl": res.text,
                "title": title,
                "info": info
            },
            "creator": "geo, rey, hans",
            "status": "OKE CROT...!"
	    }
	   return(result)
	except:
		result = {"result": "Error info id Iine denmas_geo"}
		return(result)
def sendIgram(url):
	try:
		headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"}
		link = "http://zasasa.com/en/download_instagram_videos_or_photos.php"
		option = {'url': url, 'submit': 'Download!'}
		ghd = requests.post(link,option, headers=headers).text
		if "All videos:" in ghd:
			type = "Video_Post"
			cikk = getStr(ghd,"All videos:<br><a href='","All photos of the post:")
			urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cikk)
		else:
			type = "Image_Post"
			cikk = getStr(ghd,">here</a><br><br><a href='","<br><textarea cols=60 rows=2")
			urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cikk)
		for url in urls:
			cok = url.split("'")[0]
			if "mp4?" in cok:
			     result = {
			         "result": {
			             "linkUrl": cok,
			             "type": type
			         },
			         "creator": "geo, rey, hans, fino",
			         "status": "OKE COK___!"
			     }
			     return(result)
			else:
			     result = {
			         "result": {
			             "linkUrl": cok,
			             "type": type
			         },
			         "creator": "geo, rey, hans, fino",
			         "status": "OKE COK___!"
			     }
			     return(result)
	except:
		result = {"result": "Error info id Iine denmas_geo"}
		return(result)
		
def Tzone(query):
	try:
	    url1 = f"https://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=31720ec755f54622a1e120030202009&q={query}&format=json&num_of_days=1"
	    url2 = f"https://api.worldweatheronline.com/premium/v1/search.ashx?key=31720ec755f54622a1e120030202009&q={query}&format=json"
	    url3 = f"http://api.worldweatheronline.com/premium/v1/tz.ashx?key=31720ec755f54622a1e120030202009&q={query}&format=json"
	    anu = json.loads(requests.get(url3).text)
	    data = json.loads(requests.get(url2).text)
	    data1 = json.loads(requests.get(url1).text)
	    gex ="%s"% data["search_api"]["result"][0]["latitude"]
	    ge ="%s"% data["search_api"]["result"][0]["longitude"]
	    ct = "%s" % anu["data"]["request"][0]["query"]
	    yt = "%s" % anu["data"]["time_zone"][0]["localtime"]
	    ytt = "%s" % anu["data"]["time_zone"][0]["utcOffset"]
	    ytg = "%s" % anu["data"]["time_zone"][0]["zone"]
	    City = "%s"% data1["data"]["request"][0]["query"]
	    Date = "%s"% data1["data"]["weather"][0]["date"]
	    Sunrise = "%s"% data1["data"]["weather"][0]["astronomy"][0]["sunrise"]
	    Sunset = "%s"% data1["data"]["weather"][0]["astronomy"][0]["sunset"]
	    Maxtempc = "%s"% data1["data"]["weather"][0]["maxtempC"]
	    Maxtempf = "%s"% data1["data"]["weather"][0]["maxtempF"]
	    MaintempC = "%s"% data1["data"]["weather"][0]["mintempC"]
	    MaintempF = "%s"% data1["data"]["weather"][0]["mintempF"]
	    area = "https://maps.google.com/maps?q=%s,%s" % (gex,ge)
	    result = {
	        "status": "OKE GREK....!",
	        "creator": "GEO",
	        "result":{
	            "latitude": "%s" % gex,
	            "longitude": "%s" % ge,
	            "localtime": "%s" % yt,
	            "zone_locations": "%s" % ytg,
	            "utcOffset": "%s" % ytt,
	            "city": "%s" % City,
	            "sunrise": "%s" % Sunrise,
	            "sunset": "%s" % Sunset,
	            "maxtempc": "%s °c" % Maxtempc,
	            "maxtempf": "%s °f" % Maxtempf,
	            "maintempc": "%s °c" % MaintempC,
	            "maintempf": "%s °f" % MaintempF,
	            "linkMaps": "%s" % area
	        }
	    }
	    return(result)
	except:
		result = {"result": "Error info id Iine denmas_geo"}
		return(result)
		
def textVideo(query):
	try:
		link = "https://photooxy.com/league-of-legends/create-avatar-video-with-animation-lol-champions-180.html"
		numku = str(random.randint(1, 23))
		option = {'optionNumber_0': numku, 'optionNumber_1': '1', 'text_2': query, 'login': 'OK'}
		geo = requests.post(link,option, headers=headers).text
		recu = getStr(geo,'<div class="alert alert-info" role="alert">','<a class = "btn btn-default"')
		requ = recu.split("-")[0]
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', requ)
		for url in urls:
			mek = unquote(url).replace("%", "")
			res = requests.get('https://tinyurl.com/api-create.php?url=%s' % mek)
			result = {
				"result": {
					"linkUrl": res.text
				},
				"creator": "geo, rey",
				"status": "OKE COK___!"
			}
		return(result)
	except:
		result = {"result": "Error info id Iine denmas_geo"}
		return(result)
def smulid(name):
	try:
	    url = f"https://www.smule.com/{name}"
	    r = urllib.request.urlopen(url)
	    rs = r.read().decode()
	    rc ="%s"% getStr(rs,'"pic_url":"','",')
	    a ="%s"% getStr(rs,'"handle":"','",')
	    ret ="%s"% getStr(rs,'"followers":"','","followees"')
	    res ="%s"% getStr(rs,'"followees":"','","num_performances":')
	    cok ="%s"% getStr(rs,',"num_performances":"','","blurb":')
	    e ="%s"% getStr(rs,',"blurb":"','","is_following":')
	    vip ="%s"% getStr(rs,'"is_vip":',',"is_verified"')
	    result ={
	        "result":{
	            "name": a,
	            "followers": ret,
	            "followings": res,
	            "song": cok,
	            "bio": e,
	            "statusVip": vip,
	            "pict_url": rc
	        },
	        "status": "OKE COK__!",
	        "creator": "geo, fino"
	    }
	    return(result)
	except:
		result = {"result": "Error info id Iine denmas_geo"}
		return(result)
def ingempa(detil):
	try:
	    dsa ="https://www.bmkg.go.id/berita/?p=gempabumi-tektonik-m-50-tidak-berpotensi-tsunami&lang=ID&s={detil}"
	    res = requests.get(dsa, headers=headers).text
	    a = getStr(res, '<li><span class="waktu">', '</li>')
	    b = getStr(res, '<li><span class="ic magnitude"></span>', '</li>')
	    c = getStr(res, '<li><span class="ic kedalaman"></span>', '</li>')
	    d = getStr(res, '<li><span class="ic koordinat"></span>', '</li>')
	    e = getStr(res, '<li><span class="ic lokasi"></span>', '</li>')
	    f = getStr(res, '<li><span class="ic dirasakan"></span>', '</li>')
	    g = getStr(res, '<li><a class="more" href="', '">')
	    img = getStr(res, '<img class="img-responsive" src="', '"')
	    result ={
	        "result":{
	            "waktu": "%s"%(a),
	            "magnitude": "%s"%(b),
	            "kedalaman": "%s"%(c),
	            "kordinat": "%s"%(d),
	            "lokasi": "%s"%(e),
	            "dirasakan": "%s"%(f),
	            "link_sumber": "https://www.bmkg.go.id/berita/%s"%(g),
	            "link_image": " %s"%(img)
	        },
	        "creator": "geo",
	        "status": "OKE COK__!"
	    }
	    return(result)
	except:
		result = {"result": "Error info id Iine denmas_geo"}
		return(result)
		
def zodiak(search):
	try:
	    response = requests.get('https://www.fimela.com/zodiak/%s'%(search), headers=headers).text
	    Name = getStr(response, '<h5 class="zodiac__random__title">', '</h5>')
	    Tgll = getStr(response, '<span class="zodiac__random__date">','</span>')
	    Kesehatan = getStr(response, '<div class="zodiac__readpage__content"><p>', '</p>')
	    mGal = getStr(response, '<h5 class="zodiac__readpage__title-header">Love</h5></div><div class="zodiac__readpage__content"><p>', '</p>')
	    aTn = getStr(response, '<h5 class="zodiac__readpage__title-header">Keuangan</h5></div><div class="zodiac__readpage__content"><p>', '</p>')
	    saT = getStr(response, '<span class="zodiac__readpage-numbers">', '</span>')
	    wB = getStr(response, 'class="zodiac__random__img" data-src="', '</a>')
	    anu = str(mGal).replace("Couple: ","\nCouple: ").replace("<br><br>","").replace("Couple : ","\nCouple: ")
	    au = str(wB).replace('">','')
	    result = {
	        "status": "OKE COK___!",
	        "creator": "GEO",
	        "result": {
	            "zodiak": "%s"% (Name),
	            "tanggal": "%s"% (Tgll),
	            "kesehatan": "%s"% (Kesehatan),
	            "couple": "%s"% (anu),
	            "keuagan": "%s"% (aTn),
	            "nomer": "%s"% (saT),
	            "url_link": "%s"% (au)
	        }
	    }
	    return(result)
	except:
		result = {"result": "Error info id Iine denmas_geo"}
		return(result)
		
def sendSmule(text):
	try:
		smule = "https://sing.salon/smule-downloader/?url={}".format(urllib.parse.quote(text))
		r = urllib.request.urlopen(text)
		rs = r.read().decode()
		type = "%s"% getStr(rs,'"type":"','"')
		title = "%s"% getStr(rs,'"title":"','"')
		mseg = "%s"% getStr(rs,'"message":"','"')
		type1 = "%s"% getStr(rs,'"ensemble_type":"','"')
		perforby = "%s"% getStr(rs,'"performed_by":"','"')
		loves = "%s"% getStr(rs,'"truncated_loves":"','"')
		listens = "%s"% getStr(rs,'"truncated_listens":"','"')
		comments = "%s"% getStr(rs,'"truncated_comments":"','"')
		performers = "%s"% getStr(rs,'"truncated_other_performers":"','"')
		tuu = urllib.request.urlopen(smule)
		dus = tuu.read().decode()
		aku = "%s"% getStr(dus,'<img src="https://www.smule.com/redir?','"')
		anu = str(aku).replace("amp;","")
		mek = f'https://www.smule.com/redir?{anu}'
		with requests.session() as s:
		  	s.headers=[{
		  		'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
		  		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		  		'Accept-Language': 'id,en-US;q=0.7,en;q=0.3',
		  		'Connection': 'keep-alive',
		  		'Upgrade-Insecure-Requests': '1',
		  		'Pragma': 'no-cache',
		  		'Cache-Control': 'no-cache',
		  		'TE': 'Trailers',
		  	}]
		  	r = s.get(smule)
		  	data = BeautifulSoup(r.content, 'html5lib')
		  	get = data.select("a[href*=https://www.smule.com/redir?]")[0]
		  	data1 = {"type":type}
		  	if 'audio' in data1["type"]:
		  	    result = {
		  	        "status": "OKE COK__!",
		  	        "creator": "GEO",
		  	        "result":{
		  	            "urlmusic": get['href'],
		  	            "urlimg":mek,
		  	            "title":title,
		  	            "message":mseg,
		  	            "type":type,
		  	            "type_sing":type1,
		  	            "singBy":perforby,
		  	            "start":{
		  	                "loves":loves,
		  	                "listens":listens,
		  	                "comments":comments,
		  	                "performers":performers
		  	            },
		  	        }
		  	    }
		  	    return(result)
		  	else:
		  	    result = {
		  	        "status": "OKE COK__!",
		  	        "creator": "GEO",
		  	        "result":{
		  	            "urlmusic": get['href'],
		  	            "urlimg":mek,
		  	            "title":title,
		  	            "message":mseg,
		  	            "type":type,
		  	            "type_sing":type1,
		  	            "singBy":perforby,
		  	            "start":{
		  	                "loves":loves,
		  	                "listens":listens,
		  	                "comments":comments,
		  	                "performers":performers
		  	            },
		  	        }
		  	    }
		  	    return(result)
	except:
		result = {"result": "Error info id Iine denmas_geo"}
		return(result)
#========================
def sendLogo(text):
	try:
		link = "https://photooxy.com/logo-and-text-effects/illuminated-metallic-effect-177.html"
		option = {
		    'text_1': text,
		    'submit': 'OKE'
		}
		ck = requests.post(link,option, headers=headers).text
		cok = getStr(ck,'<input type="hidden"  style= "padding:3px; width:100%;" name="share_link" value="','" id="share_link">')
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
		for url in urls:
			mek = unquote(url).replace("['", "")
			su = str(mek).split('-')[0]
			res = requests.get('https://tinyurl.com/api-create.php?url=%s' % su)
			result = {
				"result": {
					"linkUrl": res.text
				},
				"creator": "geo, rey",
				"status": "OKE COK___!"
			}
			return(result)
	except:
		result = {"result": "Error info id Iine denmas_geo"}
		return(result)
def sendChamp(text):
	numku = str(random.randint(1, 44))
	try:
		link = "https://photooxy.com/league-of-legends/make-avatar-lol-with-your-main-champions-138.html"
		option = {
		    'optionNumber_0': numku,
		    'text_2': text,
		    'submit': 'OKE'
		}
		ck = requests.post(link,option, headers=headers).text
		cok = getStr(ck,'<input type="hidden"  style= "padding:3px; width:100%;" name="share_link" value="','" id="share_link">')
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
		for url in urls:
			mek = unquote(url).replace("['", "")
			su = str(mek).split('-')[0]
			res = requests.get('https://tinyurl.com/api-create.php?url=%s' % su)
			result = {
				"result": {
					"linkUrl": res.text
				},
				"creator": "geo, rey",
				"status": "OKE COK___!"
			}
			return(result)
	except:
		result = {"result": "Error info id Iine denmas_geo"}
		return(result)
def sendPhotoxy_143(text):
	try:
	    link = "https://photooxy.com/league-of-legends/wings-avatar-lol-effect-143.html"
	    numku = str(random.randint(1, 444))
	    option = {'optionNumber_0': numku , 'text_2': text, 'login': 'OK'}
	    ghd = requests.post(link,option, headers=headers).text
	    rey = getStr(ghd,'<div class="alert alert-info" role="alert">','<a class = "btn btn-default"')
	    cok = rey.split("-")[0]
	    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
	    for url in urls:
	        mek = unquote(url).replace("%", "")
	        res = requests.get('https://tinyurl.com/api-create.php?url=%s' % mek)
	        result = {
		        "result": {
		            "linkUrl": res.text
		        },
		        "creator": "geo, rey, hans, fino",
		        "status": "OKE COK___!"
	        }
	        return(result)
	except:
	    result = {"result": "Error info id Iine denmas_geo"}
	    return(result)
def sendPhotoxy_231(path1,text):
	try:
	    link = "https://photooxy.com/league-of-legends/make-flame-avatar-with-your-photo-231.html"
	    option = {'selectImage_1': 'btn btn-primary selectButton style_button_1', 'image_1': path1, 'text_4': text, 'login': 'OK'}
	    ghd = requests.post(link,option, headers=headers).text
	    mek = getStr(ghd,'<div class="alert alert-info" role="alert">','<a class = "btn btn-default"')
	    cok = mek.split("-")[0]
	    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
	    for url in urls:
	        mek = unquote(url).replace("%", "")
	        res = requests.get('https://tinyurl.com/api-create.php?url=%s' %mek)
	        result = {
                "result": {
                    "linkUrl": res.text
                },
                "creator": "geo, rey",
                "status": "OKE COK___!"
	        }
	        return(result)
	except:
	       result = {"result": "Error info id Iine denmas_geo"}
	       return(result)
        
def sendPhotoxy_118(path1,text):
    try:
        link = "https://photooxy.com/other-design/create-your-own-mastery-7-avatar-181.html"
        option = {'selectImage_1': 'btn btn-primary selectButton style_button_1', 'image_1': path1, 'text_4': text, 'login': 'OK'}
        ghd = requests.post(link,option, headers=headers).text
        mek = getStr(ghd,'<div class="alert alert-info" role="alert">','<a class = "btn btn-default"')
        cok = mek.replace(' ','').replace('\n','').split("-")[0]
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
        for url in urls:
            mek = unquote(url).replace("%", "")
            res = requests.get('https://tinyurl.com/api-create.php?url=%s' %mek)
            result = {
                "result": {
                    "linkUrl": res.text
                },
                "creator": "geo, rey",
                "status": "OKE COK___!"
            }
            return(result)
    except:
        result = {"result": "Error info id Iine denmas_geo"}
        return(result)
def sendPhotoxy_384(path1):
	try:
	    link = "https://photooxy.com/photo-frames/beautiful-pine-leaf-frame-384.html"
	    option = {'selectImage_1': 'btn btn-primary selectButton style_button_1', 'image_1': path1, 'login': 'OK'}
	    ghd = requests.post(link,option, headers=headers).text
	    mek = getStr(ghd,'<div class="alert alert-info" role="alert">','<a class = "btn btn-default"')
	    cok = mek.replace(' ','').replace('\n','').split("-")[0]
	    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
	    for url in urls:
	        mek = unquote(url).replace("%", "")
	        res = requests.get('https://tinyurl.com/api-create.php?url=%s' %mek)
	        result = {
                "result": {
                    "linkUrl": res.text
                },
                "creator": "geo, rey",
                "status": "OKE COK___!"
	        }
	        return(result)
	except:
	       result = {"result": "Error info id Iine denmas_geo"}
	       return(result)
#===================================
def sendPhotoxy_128(text):
	try:
	    link = "https://photooxy.com/league-of-legends/make-your-logo-pentakill-lol-128.html"
	    numku = str(random.randint(1, 7))
	    anu = ['ff0066','00c6ff','00ff0c','ff5a00','ba00ff','ff00f6']
	    wr = random.choice(anu)
	    option = {'optionNumber_0': numku , 'text_3': text, 'filter_3_1': wr,'login': 'OK'}
	    ghd = requests.post(link,option, headers=headers).text
	    rey = getStr(ghd,'<div class="alert alert-info" role="alert">','<a class = "btn btn-default"')
	    cok = rey.split("-")[0]
	    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
	    for url in urls:
	        mek = unquote(url).replace("%", "")
	        res = requests.get('https://tinyurl.com/api-create.php?url=%s' % mek)
	        result = {
                "result": {
                    "linkUrl": res.text
                },
                "creator": "geo, rey, hans, fino",
                "status": "OKE COK___!"
	        }
	        return(result)
	except:
	    result = {"result": "Error info id Iine denmas_geo"}
	    return(result)
def sendPhotoxy_170(text):
	try:
	    link = "https://photooxy.com/logo-and-text-effects/smoke-typography-text-effect-170.html"
	    option = {'text_1': text, 'login': 'OK'}
	    ghd = requests.post(link,option, headers=headers).text
	    mek = getStr(ghd,'<input type="hidden"  style= "padding:3px; width:100%;" name="share_link" value="','" id="share_link">')
	    cok = mek.split("-")[0]
	    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
	    for url in urls:
	        mek = unquote(url).replace("%", "")
	        res = requests.get('https://tinyurl.com/api-create.php?url=%s' %mek)
	        result = {
	            "result": {
	                "linkUrl": res.text
	            },
	            "creator": "geo, rey","status": "OKE COK___!"
	        }
	        return(result)
	except:
	       result = {"result": "Error info id Iine denmas_geo"}
	       return(result)
#def sendPhotoxy_188(path1):
#    try:

def sendPhotoxy_188(path1):
	try:
	    link = "https://photooxy.com/other-design/create-metallic-text-glow-online-188.html"
	    option = {'text_1': text, 'login': 'OK'}
	    ghd = requests.post(link,option, headers=headers).text
	    mek = getStr(ghd,'<input type="hidden"  style= "padding:3px; width:100%;" name="share_link" value="','" id="share_link">')
	    cok = mek.split("-")[0]
	    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
	    for url in urls:
	        mek = unquote(url).replace("%", "")
	        res = requests.get('https://tinyurl.com/api-create.php?url=%s' %mek)
	        result = {
	            "result": {
	                "linkUrl": res.text
	            },
	            "creator": "geo, rey","status": "OKE COK___!"
	        }
	        return(result)
	except:
	    result = {"result": "Error info id Iine denmas_geo"}
	    return(result)
#===============================[][][][][][][][][]========
def sendPhotoxy_222(text):
    try:
	    link = "https://photooxy.com/banner-cover/graffiti-text-cover-222.html"
	    option = {'text_1': text, 'login': 'OK'}
	    ghd = requests.post(link,option, headers=headers).text
	    mek = getStr(ghd,'<input type="hidden"  style= "padding:3px; width:100%;" name="share_link" value="','" id="share_link">')
	    cok = mek.split("-")[0]
	    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
	    for url in urls:
	        mek = unquote(url).replace("%", "")
	        res = requests.get('https://tinyurl.com/api-create.php?url=%s' %mek)
	        result = {
	            "result": {
	                "linkUrl": res.text
	            },
	            "creator": "geo, rey","status": "OKE COK___!"
	        }
	        return(result)
    except:
	       result = {"result": "Error info id Iine denmas_geo"}
	       return(result)
	       
def sendPhotoxy_171(text):
    try:
	    link = "https://photooxy.com/logo-and-text-effects/carved-wood-effect-online-171.html"
	    option = {'text_1': text, 'login': 'OK'}
	    ghd = requests.post(link,option, headers=headers).text
	    mek = getStr(ghd,'<input type="hidden"  style= "padding:3px; width:100%;" name="share_link" value="','" id="share_link">')
	    cok = mek.split("-")[0]
	    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
	    for url in urls:
	        mek = unquote(url).replace("%", "")
	        res = requests.get('https://tinyurl.com/api-create.php?url=%s' %mek)
	        result = {
	            "result": {
	                "linkUrl": res.text
	            },
	            "creator": "geo, rey","status": "OKE COK___!"
	        }
	        return(result)
    except:
	       result = {"result": "Error info id Iine denmas_geo"}
	       return(result)
	       
def sendPhotoxy_174(text):
    try:
	    link = "https://photooxy.com/logo-and-text-effects/put-your-text-on-a-coffee-cup--174.html"
	    option = {'text_1': text, 'login': 'OK'}
	    ghd = requests.post(link,option, headers=headers).text
	    mek = getStr(ghd,'<input type="hidden"  style= "padding:3px; width:100%;" name="share_link" value="','" id="share_link">')
	    cok = mek.split("-")[0]
	    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
	    for url in urls:
	        mek = unquote(url).replace("%", "")
	        res = requests.get('https://tinyurl.com/api-create.php?url=%s' %mek)
	        result = {
	            "result": {
	                "linkUrl": res.text
	            },
	            "creator": "geo, rey","status": "OKE COK___!"
	        }
	        return(result)
    except:
	       result = {"result": "Error info id Iine denmas_geo"}
	       return(result)
	       
def sendPhotoxy_116(text):
    try:
	    link = "https://photooxy.com/logo-and-text-effects/bevel-text-between-royal-patterns-166.html"
	    option = {'text_1': text, 'login': 'OK'}
	    ghd = requests.post(link,option, headers=headers).text
	    mek = getStr(ghd,'<input type="hidden"  style= "padding:3px; width:100%;" name="share_link" value="','" id="share_link">')
	    cok = mek.split("-")[0]
	    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
	    for url in urls:
	        mek = unquote(url).replace("%", "")
	        res = requests.get('https://tinyurl.com/api-create.php?url=%s' %mek)
	        result = {
	            "result": {
	                "linkUrl": res.text
	            },
	            "creator": "geo, rey","status": "OKE COK___!"
	        }
	        return(result)
    except:
	       result = {"result": "Error info id Iine denmas_geo"}
	       return(result)
	       
#==========================================
def sendPhotoxy_349(path1):
    try:
	    link = "https://photooxy.com/photo-frames/simple-pip-frame-349.html"
	    option = {'selectImage_2': 'btn btn-primary selectButton style_button_2', 'image_2': path1,'login': 'OK'}
	    ghd = requests.post(link,option, headers=headers).text
	    mek = getStr(ghd,'<input type="hidden"  style= "padding:3px; width:100%;" name="share_link" value="','" id="share_link">')
	    cok = mek.split("-")[0]
	    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
	    for url in urls:
	       mek = unquote(url).replace("%", "")
	       res = requests.get('https://tinyurl.com/api-create.php?url=%s' %mek)
	       result = {
                "result": {
                    "linkUrl": res.text
                },
                "creator": "geo, rey",
                "status": "OKE COK___!"
	       }
	       return(result)
    except:
	       result = {"result": "Error info id Iine denmas_geo"}
	       return(result)
	       
def sendPhotoxy_301(path1,text):
    try:
	    link = "https://photooxy.com/other-design/combined-cover-and-avatar-301.html"
	    option = {'selectImage_0': 'btn btn-primary selectButton style_button_0', 'image_0': path1,'text_3': text, 'login': 'OK'}
	    ghd = requests.post(link,option, headers=headers).text
	    mek = getStr(ghd,'<div class="alert alert-info" role="alert">','<a class = "btn btn-default"')
	    cok = mek.split("-")[0]
	    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
	    for url in urls:
	        mek = unquote(url).replace("%", "")
	        res = requests.get('https://tinyurl.com/api-create.php?url=%s' %mek)
	        result = {
                "result": {
                    "linkUrl": res.text
                },
                "creator": "geo, rey",
                "status": "OKE COK___!"
	        }
	        return(result)
    except:
	       result = {"result": "Error info id Iine denmas_geo"}
	       return(result)

def sendPhotoxy_398(path1):
    try:
	    link = "https://photooxy.com/other-design/iphone-xs-mockup-online-398.html"
	    option = {
            "selectImage_0": "btn btn-primary selectButton style_button_0", 
            "image_0": path1,
            "login": "OK"
	    }
	    ghd = requests.post(link,option, headers=headers).text
	    mek = getStr(ghd,'<div class="alert alert-info" role="alert">','<a class = "btn btn-default"')
	    cok = mek.split("-")[0]
	    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
	    for url in urls:
	        mek = unquote(url).replace("%", "")
	        res = requests.get('https://tinyurl.com/api-create.php?url=%s' %mek)
	        result = {
                "result": {
                    "linkUrl": res.text
                },
                "creator": "geo, rey",
                "status": "OKE COK___!"
	        }
	        return(result)
    except:
	       result = {"result": "Error info id Iine denmas_geo"}
	       return(result)

def sendPhotoxy_193(path1):
    try:
	    link = "https://photooxy.com/art-effects/burned-photo-on-table-193.html"
	    option = {
            "selectImage_0": "btn btn-primary selectButton style_button_0", 
            "image_0": path1,
            "login": "OK"
	    }
	    ghd = requests.post(link,option, headers=headers).text
	    mek = getStr(ghd,'<input type="hidden"  style= "padding:3px; width:100%;" name="share_link" value="','" id="share_link">')
	    cok = mek.split("-")[0]
	    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
	    for url in urls:
	        mek = unquote(url).replace("%", "")
	        res = requests.get('https://tinyurl.com/api-create.php?url=%s' %mek)
	        result = {
                "result": {
                    "linkUrl": res.text
                },
                "creator": "geo, rey",
                "status": "OKE COK___!"
	        }
	        return(result)
    except:
	       result = {"result": "Error info id Iine denmas_geo"}
	       return(result)
		
def sendPhotoxy_226(path):
    try:
	    link = "https://photooxy.com/art-effects/sketch-your-picture-on-paper-226.html"
	    option = {'selectImage_1': 'btn btn-primary selectButton style_button_1', 'image_1': path, 'login': 'OK'}
	    ghd = requests.post(link,option, headers=headers).text
	    mek = getStr(ghd,'<input type="hidden"  style= "padding:3px; width:100%;" name="share_link" value="','" id="share_link">')
	    cok = mek.split("-")[0]
	    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
	    for url in urls:
	        mek = unquote(url).replace("%", "")
	        res = requests.get('https://tinyurl.com/api-create.php?url=%s' %mek)
	        result = {
                "result": {
                    "linkUrl": res.text
                },
                "creator": "geo, rey",
                "status": "OKE COK___!"
	        }
	        return(result)
    except:
	       result = {"result": "Error info id Iine denmas_geo"}
	       return(result)
	       
def sendPhotoxy_148(path):
    try:
	    link = "https://photooxy.com/other-design/catching-pokemon-simulator-148.html"
	    option = {'selectImage_1': 'btn btn-primary selectButton style_button_1', 'image_1': path, 'login': 'OK'}
	    ghd = requests.post(link,option, headers=headers).text
	    mek = getStr(ghd,'<div class="alert alert-info" role="alert">','<a class = "btn btn-default"')
	    cok = mek.split("-")[0]
	    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
	    for url in urls:
	        mek = unquote(url).replace("%", "")
	        res = requests.get('https://tinyurl.com/api-create.php?url=%s' %mek)
	        result = {
                "result": {
                    "linkUrl": res.text
                },
                "creator": "geo, rey",
                "status": "OKE COK___!"
	        }
	        return(result)
    except:
	       result = {"result": "Error info id Iine denmas_geo"}
	       return(result)
        
#==============================================
def sendValday(path,text):
	try:
		link = "https://m.photofunia.com/categories/valentines_day/valentine"
		option = {'effect-form js-effect-form': 'input-file', 'image': path,'text': text, 'button-container': 'GO'}
		ck = requests.post(link,option, headers=headers).text
		cok = getStr(ck,'<div class="image full-height-container">','</div>')
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
		for url in urls:
			mek = unquote(url).replace("%", "")
			res = requests.get('https://tinyurl.com/api-create.php?url=%s' % mek)
			result = {
				"result": {
					"linkUrl": res.text
				},
				"creator": "geo, rey, hans, fino",
				"status": "OKE COK___!"
			}
		return(result)
	except:
		result = {"result": "Error info id Iine denmas_geo"}
		return(result)
def sendNews(path,text,text2,text3):
	try:
		link = "https://m.photofunia.com/categories/all_effects/breaking-news"
		option = {'effect-form js-effect-form': 'input-file', 'image': path,'field text-field': 'text', 'channel': text,'title1': text2,'title2': text3, 'button-container': 'GO'}
		usa = requests.post(link,option, headers=headers).text
		cok = getStr(usa,'<div class="image full-height-container">','</div>')
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
		for url in urls:
			mek = unquote(url).replace("%", "")
			res = requests.get('https://tinyurl.com/api-create.php?url=%s' % mek)
			result = {
				"result": {
					"linkUrl": res.text
				},
				"creator": "geo, rey, hans, fino",
				"status": "OKE COK___!"
			}
		return(result)
	except:
		result = {"result": "Error info id Iine denmas_geo"}
		return(result)
def sendSummer(path,path1,text):
	try:
		hander = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
		headers = {"user-agent": hander}
		link = "https://m.photofunia.com/categories/photography/summer-diary"
		option = {
			'effect-form js-effect-form': 'input-file',
			'image': path,
			'image2': path1,
			'text': text,
			'button-container': 'GO'
		}
		ck = requests.post(link,option, headers=headers).text
		cok = getStr(ck,'<div class="image full-height-container">','</div>')
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
		for url in urls:
			mek = unquote(url).replace("%", "")
			res = requests.get('https://tinyurl.com/api-create.php?url=%s' % mek)
		result = {
			"result":{
				"linkUrl": res.text
			},
			"creator": "geo, rey, hans, fino",
			"status": "OKE COK___!"
		}
		return(result)
	except:
		result = {"result": "Error info id Iine denmas_geo"}
		return(result)
		
def sendParis(path,text):
	try:
		hander = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
		headers = {"user-agent": hander}
		link = "https://m.photofunia.com/effects/memories_of_paris"
		option = {
			'effect-form js-effect-form': 'input-file',
			'image': path,
			'text': text,
			'button-container': 'GO'
		}
		ck = requests.post(link,option, headers=headers).text
		cok = getStr(ck,'<div class="image full-height-container">','</div>')
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
		for url in urls:
			mek = unquote(url).replace("%", "")
			res = requests.get('https://tinyurl.com/api-create.php?url=%s' % mek)
			result = {
				"result":{
					"linkUrl": res.text
				},
				"creator": "geo, rey, hans, fino",
				"status": "OKE COK___!"
			}
		return(result)
	except:
		result = {"result": "Error info id Iine denmas_geo"}
		return(result)

def sendClowers(path,text):
	try:
		hander = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
		headers = {"user-agent": hander}
		link = "https://m.photofunia.com/effects/flowers"
		option = {
				'effect-form js-effect-form': 'input-file',
				'field imagelist-field': 'imagelist-collection',
				'image ': 'https://cdn.photofunia.com/effects/flowers/resources/5kj3w6.jpg',
				'image': path,
				'text': text,
				'button-container': 'GO'
		}
		ck = requests.post(link,option, headers=headers).text
		cok = getStr(ck,'<div class="image full-height-container">','</div>')
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
		for url in urls:
			mek = unquote(url).replace("%", "")
			res = requests.get('https://tinyurl.com/api-create.php?url=%s' % mek)
			result = {
				"result":{
					"linkUrl": res.text
				},
				"creator": "geo, rey, hans, fino",
				"status": "OKE COK___!"
			}
		return(result)
	except:
		result = {"result": "Error info id Iine denmas_geo"}
		return(result)
        
#==========================================
def sendPhotoxy_345(path1,text):
    try:
        link = "https://photooxy.com/photo-frames/photo-frame-on-beach-345.html"
        option = {'selectImage_0': 'btn btn-primary selectButton style_button_0', 'image_0': path1, 'text_2': text, 'login': 'OK'}
        ghd = requests.post(link,option, headers=headers).text
        mek = getStr(ghd,'<input type="hidden"  style= "padding:3px; width:100%;" name="share_link" value="','" id="share_link">')
        cok = mek.split("-")[0]
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
        for url in urls:
            mek = unquote(url).replace("%", "")
            res = requests.get('https://tinyurl.com/api-create.php?url=%s' %mek)
            result = {
                "result": {
                    "linkUrl": res.text
                },
                "creator": "geo, rey",
                "status": "OKE COK___!"
            }
            return(result)
    except:
        result = {"result": "Error info id Iine denmas_geo"}
        return(result)
        
 #===eeeerr!=====================================
def sendbook(path,text,text1):
	try:
		hander = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
		headers = {"user-agent": hander}
		link = "https://m.photofunia.com/effects/very-old-book"
		option = {
			'effect-form js-effect-form': 'input-file',
			'image': path,
			'text': text,
			'text2': text1,
			'image active': 'reed',
			'button-container': 'GO'
		}
		ck = requests.post(link,option, headers=headers).text
		cok = getStr(ck,'<div class="image full-height-container">','</div>')
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
		for url in urls:
			mek = unquote(url).replace("%", "")
			res = requests.get('https://tinyurl.com/api-create.php?url=%s' % mek)
			result = {
				"result":{
					"linkUrl": res.text
				},
				"creator": "geo, rey, hans, fino",
				"status": "OKE COK___!"
			}
		return(result)
	except:
		result = {"result": "Error info id Iine denmas_geo"}
		return(result)
		
def sendopen(path,text,text1):
	try:
		hander = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
		headers = {"user-agent": hander}
		link = "https://m.photofunia.com/effects/open-book"
		option = {
			'effect-form js-effect-form': 'input-file',
			'image': path,
			'text1': text,
			'text2': text1,
			'button-container': 'GO'
		}
		ck = requests.post(link,option, headers=headers).text
		cok = getStr(ck,'<div class="image full-height-container">','</div>')
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
		for url in urls:
			mek = unquote(url).replace("%", "")
			res = requests.get('https://tinyurl.com/api-create.php?url=%s' % mek)
			result = {
				"result":{
					"linkUrl": res.text
				},
				"creator": "geo, rey, hans, fino",
				"status": "OKE COK___!"
			}
		return(result)
	except:
		result = {"result": "Error info id Iine denmas_geo"}
		return(result)
		
def sendmorning(path,text,text1,text2):
	try:
		hander = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
		headers = {"user-agent": hander}
		link = "https://m.photofunia.com/effects/morning_news"
		option = {
			'effect-form js-effect-form': 'input-file',
			'image': path,
			'title': text,
			'section': text1,
			'date': text2,
			'button-container': 'GO'
		}
		ck = requests.post(link,option, headers=headers).text
		cok = getStr(ck,'<div class="image full-height-container">','</div>')
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
		for url in urls:
			mek = unquote(url).replace("%", "")
			res = requests.get('https://tinyurl.com/api-create.php?url=%s' % mek)
			result = {
				"result":{
					"linkUrl": res.text
				},
				"creator": "geo, rey, hans, fino",
				"status": "OKE COK___!"
			}
		return(result)
	except:
		result = {"result": "Error info id Iine denmas_geo"}
		return(result)
		
def sendcover(path):
	try:
		hander = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
		headers = {"user-agent": hander}
		link = "https://m.photofunia.com/effects/back_cover"
		option = {
			'effect-form js-effect-form': 'input-file',
			'image': path,
			'button-container': 'GO'
		}
		ck = requests.post(link,option, headers=headers).text
		cok = getStr(ck,'<div class="image full-height-container">','</div>')
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
		for url in urls:
			mek = unquote(url).replace("%", "")
			res = requests.get('https://tinyurl.com/api-create.php?url=%s' % mek)
			result = {
				"result":{
					"linkUrl": res.text
				},
				"creator": "geo, rey, hans, fino",
				"status": "OKE COK___!"
			}
		return(result)
	except:
		result = {"result": "Error info id Iine denmas_geo"}
		return(result)
		
def senddaily(path,text,text1):
	try:
		hander = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
		headers = {"user-agent": hander}
		link = "https://m.photofunia.com/effects/daily-newspaper"
		option = {
			'effect-form js-effect-form': 'input-file',
			'image': path,
			'text1': text,
			'text2': text1,
			'button-container': 'GO'
		}
		ck = requests.post(link,option, headers=headers).text
		cok = getStr(ck,'<div class="image full-height-container">','</div>')
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cok)
		for url in urls:
			mek = unquote(url).replace("%", "")
			res = requests.get('https://tinyurl.com/api-create.php?url=%s' % mek)
			result = {
				"result":{
					"linkUrl": res.text
				},
				"creator": "geo, rey, hans, fino",
				"status": "OKE COK___!"
			}
		return(result)
	except:
		result = {"result": "Error info id Iine denmas_geo"}
		return(result)
#====[qr login]=====
