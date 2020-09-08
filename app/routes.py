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
	
@app.route('/searchGoogle',methods=['POST','GET'])
def rest_Google():
	this_search = request.args['search']
	this_rest = scrap.searchGoogle(this_search)
	return json.dumps(this_rest, indent=4)