from flask import Blueprint, render_template, abort, request, Response
from database import Database 
from models.Template import Template
from werkzeug.utils import secure_filename

template_controller = Blueprint('template_controller', __name__, template_folder='templates')
db = Database()

@template_controller.route("/templates", methods=["GET"])
def get_template():
    template_id = request.args.get("template_id")
    keyword = request.args.get("key_word")
    deployed_regions_required = request.args.get("deployed_regions_required")
    if not template_id and not keyword:
        resp = Response(response=db.get_templates(), status=200, mimetype="application/json")
    elif template_id:
        resp = Response(response=db.get_single_template_by_id(template_id, deployed_regions_required), status=200, mimetype="application/json")
    elif keyword:
        resp = Response(response=db.get_templates_by_keyword(keyword), status=200, mimetype="application/json")
    else:
        resp = {"msg": "Something went wrong, please try again"}
    return resp



@template_controller.route("/templates", methods=["POST"])
def create_template():
    f = request.files["files"]
    name = request.form.get("name")
    filename = f.filename
    description = request.form.get("description")
    tags = request.form.getlist("tags[]")
    template = Template(name, filename, tags, description)
    status = db.create_template(template, filename)
    f.save("files/" + secure_filename(filename))
    return {'msg': 'template created!'}