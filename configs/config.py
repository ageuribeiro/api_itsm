from configparser import ConfigParser

# Inicializa o objeto ConfigParser
config = ConfigParser()

# Lê o arquivo de configuração
config.read("configs/config.cfg")


# verifica se as seções estão presentes
required_sections = ["JIRA", "SERVICENOW", "SIEBEL"]
for section in required_sections:
    if section not in config:
        raise KeyError(
            f"Seção '{section}' não encontrada no arquivo de configuração.")

# criando o dicionario de configuração
CONFIG = {
    "jira": {
        "url": config["JIRA"]["URL"],
        "auth": (config["JIRA"]["USER"], config["JIRA"]["API_KEY"]),
        "headers": {"Content-Type": "application/json"}
    },
    "servicenow": {
        "url": config["SERVICENOW"]["URL"],
        "auth": (config["SERVICENOW"]["USER"], config["SERVICENOW"]["PASSWORD"]),
        "headers": {"Content-Type": "application/json"}
    },
    "siebel": {
        "url": config["SIEBEL"]["URL"],
        "auth": (config["SIEBEL"]["USER"], config["SIEBEL"]["PASSWORD"]),
        "headers": {"Content-Type": "application/json"}

    },
    "mongodb": {
        "uri": config["MONGODB"]["uri"]
    }
}
