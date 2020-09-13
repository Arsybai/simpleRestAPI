from app import app, scrap
from flask import render_template, send_file ,flash, url_for
from flask import request
from app.forms import LoginForm
import requests, json, random

@app.route('/')
@app.route('/index')
def home():
	return render_template('index.html',title='LESSON')
	
@app.route('/image',methods=['POST','GET'])
def rest_image():
	this_query = request.args['query']
	this_rest = scrap.img(this_query)
	return json.dumps(this_rest, indent=4, sort_keys=True)
	#json.dumps(this_rest, indent=4, sort_keys=True
	
@app.route('/stafa',methods=['POST','GET'])
def rest_stafa():
	this_query = request.args['search']
	this_rest = scrap.stafa(this_query)
	return json.dumps(this_rest, indent=4, sort_keys=True)
	
@app.route('/xvideos',methods=['POST','GET'])
def rest_VideoX():
	this_query = request.args['search']
	this_query1 = request.args['page']
	this_rest = scrap.VideoX(this_query,this_query1)
	return json.dumps(this_rest, indent=4, sort_keys=True)
	
@app.route('/xdownload',methods=['POST','GET'])
def rest_VideoDL():
	this_query = request.args['url']
	this_rest = scrap.VideoDL(this_query)
	return json.dumps(this_rest, indent=4, sort_keys=True)
	
@app.route('/randomimg',methods=['POST','GET'])
def rest_randomimg():
	this_query = request.args['query']
	this_rest = scrap.randomimg(this_query)
	return json.dumps(this_rest, indent=4, sort_keys=True)

@app.route('/artiname',methods=['POST','GET'])
def rest_artiName():
	this_query = request.args['query']
	this_rest = scrap.artiName(this_query)
	return json.dumps(this_rest, indent=4, sort_keys=True)

@app.route('/googlesearch',methods=['POST','GET'])
def rest_goSearch():
	this_query = request.args['query']
	this_rest = scrap.goSearch(this_query)
	return json.dumps(this_rest, indent=4, sort_keys=True)
	
@app.route('/textavatar',methods=['POST','GET'])
def rest_textVideo():
	this_query = request.args['query']
	this_rest = scrap.textVideo(this_query)
	return json.dumps(this_rest, indent=4, sort_keys=True)
	
@app.route('/photofun/valentines_day',methods=['POST','GET'])
def rest_sendValday():
	this_path = request.args['path']
	this_query = request.args['text']
	this_rest = scrap.sendValday(this_path, this_query)
	return json.dumps(this_rest, indent=4, sort_keys=True)
	
@app.route('/photofun/summer-diary',methods=['POST','GET'])
def rest_sendSummer():
	this_path = request.args['path']
	this_path1 = request.args['path1']
	this_query = request.args['text']
	this_rest = scrap.sendSummer(this_path, this_path1, this_query)
	return json.dumps(this_rest, indent=4, sort_keys=True)
	
@app.route('/photofun/flowers',methods=['POST','GET'])
def rest_sendClowers():
	this_path = request.args['path']
	this_query = request.args['text']
	this_rest = scrap.sendClowers(this_path, this_query)
	return json.dumps(this_rest, indent=4, sort_keys=True)
	
@app.route('/photofun/memories_of_paris',methods=['POST','GET'])
def rest_sendParis():
	this_path = request.args['path']
	this_query = request.args['text']
	this_rest = scrap.sendParis(this_path, this_query)
	return json.dumps(this_rest, indent=4, sort_keys=True)
	
@app.route('/photofun/very-old-book',methods=['POST','GET'])
def rest_sendbook():
	this_path = request.args['path']
	this_query = request.args['text']
	this_query1 = request.args['text1']
	this_rest = scrap.sendbook(this_path, this_query, this_query1)
	return json.dumps(this_rest, indent=4, sort_keys=True)
	
@app.route('/photofun/open-book',methods=['POST','GET'])
def rest_sendopen():
	this_path = request.args['path']
	this_query = request.args['text']
	this_query1 = request.args['text1']
	this_rest = scrap.sendopen(this_path, this_query, this_query1)
	return json.dumps(this_rest, indent=4, sort_keys=True)
	
@app.route('/photofun/daily-newspaper',methods=['POST','GET'])
def rest_senddaily():
	this_path = request.args['path']
	this_query = request.args['text']
	this_query1 = request.args['text1']
	this_rest = scrap.senddaily(this_path, this_query, this_query1)
	return json.dumps(this_rest, indent=4, sort_keys=True)
	
@app.route('/photofun/morning_news',methods=['POST','GET'])
def rest_sendmorning():
	this_path = request.args['path']
	this_query = request.args['text']
	this_query1 = request.args['text1']
	this_query2 = request.args['text2']
	this_rest = scrap.sendmorning(this_path, this_query, this_query1, this_query2)
	return json.dumps(this_rest, indent=4, sort_keys=True)
	
@app.route('/photofun/back_cover',methods=['POST','GET'])
def rest_sendcover():
	this_path = request.args['path']
	this_rest = scrap.sendcover(this_path)
	return json.dumps(this_rest, indent=4, sort_keys=True)
@app.route('/legends/avatar',methods=['POST','GET'])
def rest_sendPhotoxy_128():
	this_path = request.args['text']
	this_rest = scrap.sendPhotoxy_128(this_path)
	return json.dumps(this_rest, indent=4, sort_keys=True)
@app.route('/legends/wings',methods=['POST','GET'])
def rest_sendPhotoxy_143():
	this_path = request.args['text']
	this_rest = scrap.sendPhotoxy_143(this_path)
	return json.dumps(this_rest, indent=4, sort_keys=True)
@app.route('/instadl',methods=['POST','GET'])
def rest_sendIgram():
	this_path = request.args['url']
	this_rest = scrap.sendIgram(this_path)
	return json.dumps(this_rest, indent=4, sort_keys=True)
	
@app.route('/photofun/breaking-news',methods=['POST','GET'])
def rest_sendNews():
	this_path = request.args['path']
	this_text = request.args['text']
	this_text2 = request.args['text2']
	this_text3 = request.args['text3']
	this_rest = scrap.sendNews(this_path, this_text, this_text2, this_text3)
	return json.dumps(this_rest, indent=4, sort_keys=True)
	 #json.dumps(this_rest, indent=4)
