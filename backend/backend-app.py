# Import Modules
import psutil
import platform
from flask import Flask
import json

application = Flask(__name__)

# REST API for '/' endpoint
@application.route('/')
def vm_info():
    cpu = str(psutil.cpu_percent()) + "%"
    ram = str(psutil.virtual_memory().percent) + "%"
    hostname = platform.node()
    json_result = json.dumps({"hostname": hostname, "cpu": cpu, "ram": ram}, indent=4)
    return json_result