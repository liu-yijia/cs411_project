from flask import Flask, request, render_template
from uber_rides.session import Session
from uber_rides.client import UberRidesClient

session = Session(server_token=<TOKEN>)
client = UberRidesClient(session)

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
