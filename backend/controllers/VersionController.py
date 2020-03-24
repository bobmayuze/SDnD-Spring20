from flask import Blueprint, render_template, abort, request, Response
from database import Database
from models.Template import Template
from werkzeug.utils import secure_filename

db = Database.getDB()
version_controller = Blueprint('versoin_controller', __name__, template_folder='templates')
@version_controller.route("/versions", methods=["GET"])
def get_versions():
    origin_id = request.args.get("origin_id")
    resp = Response(response=db.get_versions(origin_id), status=200, mimetype="version_controllerlication/json")
    return resp  

@version_controller.route("/versions", method=["POST"])
def create_versoin()

@version_controller.route("/versions", methods=["PUT"])
def activate_version():
    origin_id = request.args.get("origin_id")
    version_id = request.args.get("version_id")
    resp = Response(response=db.activate_version(origin_id, version_id), status=200, mimetype="version_controllerlication/json")
    return resp

@version_controller.route("/versions", methods=["DELETE"])
def delete_version():
    origin_id = request.args.get("origin_id")
    version_id = request.args.get("version_id")
    resp = Response(response=db.delete_version(origin_id, version_id), status=200, mimetype="version_controllerlication/json")
    return resp