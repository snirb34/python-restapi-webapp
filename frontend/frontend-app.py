import requests
from flask import Flask
import random

application = Flask(__name__)

@application.route('/vmdetails')
def get_vmdetails():
    urls_list = ["http://localhost:5000", "http://localhost:5002"]
    url = random.choice(urls_list)
    response = requests.get(url).text
    return response