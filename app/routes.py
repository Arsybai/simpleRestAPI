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
	return json.dumps(this_rest, indent=4)

@app.route('/randomimg',methods=['POST','GET'])
def rest_randomimg():
	this_query = request.args['query']
	this_rest = scrap.randomimg(this_query)
	return json.dumps(this_rest, indent=4)

@app.route('/artiname',methods=['POST','GET'])
def rest_artiName():
	this_query = request.args['query']
	this_rest = scrap.artiName(this_query)
	return json.dumps(this_rest, indent=4)

@app.route('/googlesearch',methods=['POST','GET'])
def rest_goSearch():
	this_query = request.args['query']
	this_rest = scrap.goSearch(this_query)
	return json.dumps(this_rest, indent=4)
	
@app.route('/textavatar',methods=['POST','GET'])
def rest_textVideo():
	this_query = request.args['query']
	this_rest = scrap.textVideo(this_query)
	return json.dumps(this_rest, indent=4)

@app.route('/photofun',methods=['POST','GET'])
def rest_sendValday():
	this_path = request.args['path']
	this_query = request.args['query']
	this_rest = scrap.sendValday(this_path, this_query)
	return json.dumps(this_rest, indent=4)

@app.route('/instagram',methods=['POST','GET'])
def rest_insta():
	this_user = request.args['username']
	this_rest = scrap.instaprofile(this_user)
	return json.dumps(this_rest, indent=4)
