from flask import request
from configs.config import CONFIG
from services.db_manager import move_incident_to_backup


def get_incident_status(incident_id):
    """
    Busca o status do incidente no ServiceNow.
    """

    config = CONFIG["servicenow"]
    url = f"{config['url']}/{incident_id}"

    response = request.get(url, auth=(config['auth'], config['headers']))

    if response.status_code == 200:
        incident_data = response.json()
        return {
            "status": incident_data.get("state"),
            "queue": incident_data.get("assignment_group"),
        }
    else:
        return {"error": f"Erro ao buscar incidente {incident_id}"}


def check_and_correct_queue(incident_id):
    """
    Verifica se o incidente está na fila correta e move se necessário.
    """
    incident = get_incident_status(incident_id)

    if "error" in incident:
        return incident

    # Se o status for "Fechamento", mover para backup
    if incident["status"] == "Fechamento":
        return move_incident_to_backup(incident_id)

    return {"message": f"Incidente {incident_id} ainda está aberto."}
