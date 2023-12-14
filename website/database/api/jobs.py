from flask import Blueprint, jsonify
from flask_cors import CORS
from .. import get_all_jobs

jobs_api = Blueprint("jobs_api", "jobs_api", url_prefix="/api/jobs")

CORS(jobs_api)


@jobs_api("/", methods=["GET"])
def api_get_jobs():
    return jsonify(get_all_jobs())
