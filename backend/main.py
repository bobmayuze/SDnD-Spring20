from flask import *
from flask_cors import CORS
import requests
import pymongo
from werkzeug.utils import secure_filename
from werkzeug.datastructures import ImmutableMultiDict

import os
import json

app = Flask(__name__)
CORS(app)
from template import Template
from database import Database

db = Database()

@app.route("/")
def root():
    return "initial page"

@app.route("/<string:page_name>/")
def hello(page_name):
    return render_template('%s.html' % page_name)

'''
Fetch the regions according to a list of all avaliable ip's

TODO
determine what fields to fetch and display
'''

@app.route('/allregions', methods=['GET'])
def all_regions():
    resp = Response(response=db.get_regions(), status=200, mimetype="application/json")
    return resp

'''
Fetch all the templates that have been uploaded with this system
'''
@app.route("/alltemplates", methods=['GET'])
def all_templates():
    resp = Response(
            response=db.get_templates(), status=200, mimetype="application/json")
    return resp



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
