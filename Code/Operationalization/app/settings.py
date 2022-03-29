def get_enviroment_variables(name):
    env = {}
    if name == "elian":
        env["ENDPOINT"] = "arx4clmj8o6k9-ats.iot.us-east-1.amazonaws.com"
    elif name == "shadow":
        env["ENDPOINT"] = "a1apbqincnemcr-ats.iot.us-east-1.amazonaws.com"
    else:
        env["ENDPOINT"] = None

    env["CLIENT_ID"] = "room"
    env["PATH_TO_CERTIFICATE"] = "./certificates/room.cert.pem"
    env["PATH_TO_PRIVATE_KEY"] = "./certificates/room.private.key"
    env["PATH_TO_AMAZON_ROOT_CA_1"] = "./certificates/root-CA.crt"
    env["TOPIC"] = "room/telemetry"
    
    return env