import logging
from pymongo import MongoClient
from configs.config import CONFIG
from datetime import datetime


logging.basicConfig(filename="logs/app.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

client = MongoClient(CONFIG["mongodb"]["uri"])
db = client[CONFIG["mongodb"]["database"]]


incidents_collection = db["incidents"]
backup_collections = db["backup"]
logs_collection = db["logs"]


def move_incident_to_backup(incident_id):
    """
    Move todas as transações relacionadas ao incidente para a coleção de backup.
    """
    transactions = list(incidents_collection.find_one({"_id": incident_id}))
    if not transactions:
        return {"message": f"Não há transações para o incidente {incident_id}."}

    # Mover transações para backup
    backup_collections.insert_many(transactions)
    incidents_collection.delete_one({"incident_id": incident_id})

    log_message = f"Incidente {incident_id} movido para a coleção de backup. {len(transactions)} transações movidas."

    # Registrar no arquivo de logs
    logging.info(log_message)

    # Registrar no MongoDB
    logs_collection.insert_one({
        "incident_id": incident_id,
        "timestamp": datetime.now(),
        "action": "move_to_backup",
        "transactions_moved": len(transactions),
        "details": log_message
    })
    return {"message": log_message}
