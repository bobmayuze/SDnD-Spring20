from flask import Flask, request, Response, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

from template import Template
from database import Database
from deployment_job import deployment_job_service

app = Flask(__name__)
CORS(app)


db = Database()
job = deployment_job_service()


@app.route("/")
def root():
    return "initial page"


@app.route("/templates", methods=["GET"])
def get_template():
    template_id = request.args.get("template_id")
    keyword = request.args.get("key_word")
    if not template_id and not keyword:
        resp = Response(response=db.get_templates(), status=200, mimetype="application/json")
    elif template_id:
        resp = Response(response=db.get_single_template_by_id(template_id), status=200, mimetype="application/json")
    elif keyword:
        print('keyword searc', keyword)
        resp = Response(response=db.get_templates_by_keyword(keyword), status=200, mimetype="application/json")
    else:
        resp = {"msg": "Something went wrong, please try again"}
    return resp

@app.route("/templates", methods=["PUT"])
def create_template():
    f = request.files["files"]
    name = request.form.get("name")
    filename = f.filename
    description = request.form.get("description")
    tags = request.form.getlist("tags[]")
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

@app.route("/versions", methods=["PUT"])
def activate_version():
    origin_id = request.args.get("origin_id")
    version_id = request.args.get("version_id")
    resp = Response(response=db.activate_version(origin_id, version_id), status=200, mimetype="application/json")
    return resp

@app.route("/versions", methods=["DELETE"])
def delete_version():
    origin_id = request.args.get("origin_id")
    version_id = request.args.get("version_id")
    resp = Response(response=db.delete_version(origin_id, version_id), status=200, mimetype="application/json")
    return resp

# Endpoints for Jobs
@app.route("/jobs", methods=["PUT"])
def create_deployment_jobs():
    params = request.get_json()
    print(params)
    task = job.create_deployment_job(
        template_id=params['template_id'],
        region_id=params['region_id'],
        target_queue=params['target_queue'])
    print(task.id)
    return jsonify(request.get_json())

@app.route("/jobs", methods=["GET"])
def get_deployment_jobs():
    job_list = job.get_jobs()
    return jsonify(job_list)

@app.route('/jobs', methods=['DELETE'])
def revoke_job():
    params = request.get_json()
    result = job.revoke_job(params['task_id'])
    return jsonify(result)

if __name__ == '__main__':
    db.create_region('Beijing')
    app.run(debug=True, host='0.0.0.0', port=5000)
