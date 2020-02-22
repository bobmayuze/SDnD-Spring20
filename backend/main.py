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

@app.route("/templates", methods=["GET"])
def get_template():
    template_id = request.args.get("template_id")
    key_word = request.args.get("key_word")
    if not template_id and not key_word:
        resp = Response(response=db.get_templates(), status=200, mimetype="application/json")
    elif template_id:
        resp = Response(response=db.get_single_template_by_id(template_id), status=200, mimetype="application/json")
    return resp

@app.route("/templates", methods=["PUT"])
def create_template():
    f = request.files["files"]
    name = request.form.get("name")
    filename = f.filename
    description = request.form.get("description")
    tags = request.form.get("tags")
    origin_id = request.form.get("origin_id")
    template = Template(name, filename, tags) 
    if description:
        template.set_description(description)
    if origin_id:
        template.set_origin(origin_id)
    template.save_to_db()
    f.save("files/" + secure_filename(filename))
    return {"msg": "file uploaded succesfully"}

@app.route("/versions", methods=["GET"])
def get_versions():
    origin_id = request.args.get("origin_id")
    resp = Response(response=db.get_versions(origin_id), status=200, mimetype="application/json")
    return resp  

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
