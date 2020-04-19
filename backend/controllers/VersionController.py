"""
Version controller handles all the traffic regarding versions
"""

from flask import Blueprint, render_template, abort, request, Response
from database import Database
from models.Template import Template
from models.Version import Version
from werkzeug.utils import secure_filename

db = Database.getDB()
version_controller = Blueprint('version_controller', __name__, template_folder='templates')

@version_controller.route("/versions", methods=["GET"])
def get_versions():
    """
    Return the versions of a template given the origin_id of the template
    """
    origin_id = request.args.get("origin_id")
    resp = Response(response=db.get_versions(origin_id), status=200, mimetype="version_controllerlication/json")
    return resp  

@version_controller.route("/versions", methods=["POST"])
def create_version():
    """
    Create a new version given the origin_id of the parent template.
    """
    origin_id = request.form.get("origin_id")
    name = request.form.get("name")
    f = request.files["files"]
    filename = f.filename
    f.save("files/" + secure_filename(filename))
    new_version = Version(name, filename, origin_id)
    template = Template.getTemplate(origin_id)
    template.add_version(new_version)
    db.update_template(template)
    return {'msg': 'version added succesfully'}

@version_controller.route("/versions", methods=["PUT"])
def activate_version():
    """
    Activate a version of a template given the origin_id of the template, and the version_id
    of the version
    """
    req_json = request.get_json()
    origin_id = req_json['origin_id']
    version_id = req_json['version_id'] 
    template = Template.getTemplate(origin_id)
    template.activate_version(version_id)
    # resp = Response(response=db.activate_version(origin_id, version_id), status=200, mimetype="version_controllerlication/json")
    return {'msg': 'version activated succesfully'}

@version_controller.route("/versions", methods=["DELETE"])
def delete_version():
    """
    Delete a version of a template given the origin_id of the template, and the version_id
    of the version
    """
    req_json = request.get_json()
    origin_id = req_json['origin_id'] 
    version_id = req_json['version_id']
    template = Template.getTemplate(origin_id)
    template.delete_version(version_id)
    db.update_template(template)
    return {"msg": "template deleted!"}