#appcfg.py -A enduring-grid-600 update appengine-try-python
from flask import Flask, render_template, request, jsonify
from flask import Flask
import datetime
import flask
import csv,sys
import MySQLdb
from flask import g
from flask import Flask, render_template, request, redirect, Response, url_for
import time, os, json, base64, hmac, urllib
from hashlib import sha1

import time
#from flask.ext.cache import Cache
app = Flask(__name__)
# Check Configuring Flask-Cache section for more details
#cache = Cache(app,config={'CACHE_TYPE': 'simple'})
#cache = Cache(app,config={'CACHE_TYPE': 'simple'})
details = {}
listings_based_on_price = {}
listings_based_on_locality = {}
# main index
@app.route("/")
def index():
	return "Ask Me Anything"
"""
def connect_it():
	db = MySQLdb.connect("us-cdbr-iron-east-02.cleardb.net","be225b633c476c","4843cd70","heroku_e5b2294f4b320d3" )
	return db
"""

@app.route("/wol", methods=["GET","POST"])
def wol():
  import wolframalpha
  query = request.args.get('query')
  client = wolframalpha.Client('9L89KG-Y23X6THEA8')
  res = client.query(query)
  result_text = ""
  for each in res.pods:
    result_text += each.text
  print "+++++++", result_text
  return str(result_text)

@app.route("/wiki", methods=["GET","POST"])
def wiki():
  import wikipedia,re

  query = request.args.get('query')
  try:
    array = wikipedia.search(query)
    if len(array) > 0:
      var = wikipedia.summary(array[0], sentences = 1)
      var = var.encode('ascii','ignore')
      k = re.sub(r'\([^)]*\)', '',var)
      word1 = " ".join(re.findall("[a-zA-Z]+", k))
      return str(word1)
    else:
      return str('Sorry, we could not find any match.')
  except:
    return str('Sorry, we could not find any match.')




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
  ares = requests.post(speech_url, headers=headers, data=file("testfile",'rb').read())
  aresjs = json.loads(ares.text)

  print aresjs["_text"]
  return str(aresjs["_text"])




@app.route("/UploadFile", methods=["POST"])
def UploadFile():

  import sys
  import urllib
  import json
  import boto
  from boto.s3.connection import S3Connection
  from boto.s3.key import Key
  from werkzeug import secure_filename
  import time


  aws_key = ''
  aws_secret = ''
  seqhack = "seqhack2015"
  file = request.files['file']
  if file :
      filename = secure_filename(file.filename)
      s3 = boto.connect_s3(aws_key, aws_secret)
      bucket = s3.get_bucket(seqhack)
      key = bucket.new_key(filename)
      key.set_contents_from_file(file, headers=None, replace=True, cb=None, num_cb=10, policy=None, md5=None)

      time.sleep(3)

      key.make_public()


      url = key.generate_url(expires_in=0, query_auth=False)


      return str(url)


if __name__ == "__main__":
	app.run(debug=True)
