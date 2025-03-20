from flask import request
from configs.config import CONFIG

# Define quais campos serão enviados para o Jira
FIELD_MAPPING = ["id", "operation", "body", "status"]


def prepare_data(data):
    formatted_data = {key: data[key] for key in FIELD_MAPPING if key in data}

    if data["status"] == "open":
        formatted_data["priority"] = "High"

    return formatted_data


def send_to_jira(data):
    config = CONFIG["jira"]
    formatted_data = prepare_data(data)

    response = request.post(
        config["url"],
        json=formatted_data,
        auth=config["auth"],
        headers=config["headers"]
    )

    return response.json()
