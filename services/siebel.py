from flask import request
from configs.config import CONFIG

FIELD_MAPPING = ["id", "operation", "tt_primessys"]

def prepare_data(data):
    return {key: data[key] for key in FIELD_MAPPING if key in data}

def send_to_siebel(data):
    config = CONFIG["siebel"]
    formatted_data = prepare_data(data)

    response = request.post(
        config["url"],
        json=formatted_data,
        auth=config["auth"],
        headers=config["headers"]
    )

    return response.json()
