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
    key_word = request.args.get("key_word")
    if not template_id and not key_word:
        resp = Response(response=db.get_templates(), status=200, mimetype="application/json")
    elif template_id:
        resp = Response(response=db.get_single_template_by_id(template_id), status=200, mimetype="application/json")
    return resp

@app.route("/templates", methods=["PUT"])
def create_template():
    f = request.files["files"]
    name = request.args.get("name")
    filename = f.filename
    description = request.args.get("description")
    tags = request.args.get("tags")
    result = db.create_template(name, filename, tags, description)
    print(result)
    f.save("files/" + secure_filename(filename))
    return {"msg": "file uploaded succesfully"}


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
    app.run(debug=True, host='0.0.0.0', port=5000)
