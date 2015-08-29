#appcfg.py -A enduring-grid-600 update appengine-try-python
from flask import Flask, render_template, request, jsonify
from flask import Flask
import datetime
import flask
import csv,sys
import MySQLdb
from flask import g


import time
from flask.ext.cache import Cache
app = Flask(__name__)
# Check Configuring Flask-Cache section for more details
cache = Cache(app,config={'CACHE_TYPE': 'simple'})
#cache = Cache(app,config={'CACHE_TYPE': 'simple'})
details = {}
listings_based_on_price = {}
listings_based_on_locality = {}
# main index
@app.route("/")
def index():
	return "seqhack api for voice to text"
"""
def connect_it():
	db = MySQLdb.connect("us-cdbr-iron-east-02.cleardb.net","be225b633c476c","4843cd70","heroku_e5b2294f4b320d3" )
	return db
"""

  
@app.route("/VoiceToText", methods=["GET","POST"])
def VoiceToText():
  import sys
  import urllib
  import json
  import requests
  audiourl = request.args.get('url')
  speech_url = "https://api.wit.ai/speech?v=20141022"

  headers = {
      "Authorization": "Bearer BAK2V3KXFQG6UIVQXCOLVK2NEEMAUOXL",
    "Content-Type": "audio/wav",

        }

  urllib.urlretrieve(audiourl, "testfile")

  #print requests.post(speech_url, headers=headers, data=file("testfile",'rb').read()).text
  ares = requests.post(speech_url, headers=headers, data=file("testfile",'rb').read())
  aresjs = json.loads(ares.text)
  print aresjs["_text"]
  return aresjs["_text"]

if __name__ == "__main__":
	app.run(debug=True)
