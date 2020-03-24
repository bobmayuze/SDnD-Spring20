from flask import Flask, request, Response, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

from deployment_job import deployment_job_service

from controllers import TemplateController, VersionController
app = Flask(__name__)
CORS(app)

job = deployment_job_service()

@app.route("/")
def root():
    return "initial page"
# TODO: Move this to a Job Controller?
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
    app.register_blueprint(TemplateController.template_controller)
    app.register_blueprint(VersionController.version_controller)
    app.run(debug=True, host='0.0.0.0', port=5000)