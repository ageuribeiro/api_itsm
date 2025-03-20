from flask import Blueprint, request, jsonify
from services.status_checker import check_and_correct_queue

status_bp = Blueprint("status", __name__)


@status_bp.route('/check_status/<incident_id>', methods=['GET'])
def check_status(incident_id):
    """
    Verifica o status do incidente e, se estiver fechado, move para backup.
    """
    result = check_and_correct_queue(incident_id)
    return jsonify(result)
