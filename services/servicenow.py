from flask import request
from configs.config import CONFIG

FIELD_MAPPING = ["id", "description", "status"]


def prepare_data(data):
    formatted_data = {key: data[key] for key in FIELD_MAPPING if key in data}

    if data["status"] == "closed":
        formatted_data["resolution"] = "Incident resolved"

    return formatted_data


def send_to_servicenow(data):
    config = CONFIG["servicenow"]
    formatted_data = prepare_data(data)

    response = request.post(
        config["url"],
        json=formatted_data,
        auth=config["auth"],
        headers=config["headers"]
    )

    return response.json()
