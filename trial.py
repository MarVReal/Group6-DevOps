from flask import Flask 
from flask import request
import requests

app = Flask(__name__)

def test_getip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

@app.route("/")
def test_getlocation():
    ip_address = test_getip()
    response=requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "IPv4 Address": ip_address, 
        "City": response.get("city"),
        "Region": response.get("region"),
        "Country": response.get("country_name"),
	    "Time Zone" : response.get("timezone"),
	    "ISP" : response.get("org"),
	    "Latitude" : response.get("latitude"),
	"Longitude" :response.get("longitude"),
    }
	
    return location_data
if __name__ == "__main__":app.run()
