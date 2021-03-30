from flask import Flask, request, render_template
//pip install uber-rides
from uber_rides.auth import AuthorizationCodeGrant
auth_flow = AuthorizationCodeGrant(
    <YYWIwFNEDhAk-jn7hmV73pU55RlznK9P>,
    <SCOPES>,
    <u_oa_8pT-ksFwKg4kUKIBf4sGSLeFuaahcubS-J4>,
    <REDIRECT_URI>
)
auth_url = auth_flow.get_authorization_url()
from uber_rides.session import Session
from uber_rides.client import UberRidesClient

session = Session(server_token=<TOKEN>)
client = UberRidesClient(session)

//Get a list of available products
response = client.get_products(37.77, -122.41)
products = response.json.get('products')

//Get price and time estimates
response = client.get_products(37.77, -122.41)
products = response.json.get('products')
response = client.get_price_estimates(
    start_latitude=37.770,
    start_longitude=-122.411,
    end_latitude=37.791,
    end_longitude=-122.405,
    seat_count=2
)

estimate = response.json.get('prices')

app = Flask(__name__)

session = Session(server_token=<TOKEN>)
client = UberRidesClient(session)

@app.route('/')
def hello():
    return 'Hello, World!'
