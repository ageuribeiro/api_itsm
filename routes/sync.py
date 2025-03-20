from flask import Blueprint, request, jsonify
from services.jira import send_to_jira
from services.servicenow import send_to_servicenow
from services.siebel import send_to_siebel

sync_bp = Blueprint("sync", __name__)

@sync_bp.route('/sync', methods=['POST'])
def sync_data():
    data = request.json

    responses = {
        "jira": send_to_jira(data),
        "servicenow": send_to_servicenow(data),
        "siebel": send_to_siebel(data)
    }

    return jsonify(responses)
