from flask import Flask 
from flask import request
import requests

app = Flask(__name__)

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

@app.route("/")
def get_location():
    ip_address = get_ip()
    response=requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "IPv4 Address": ip_address, 
        "City": response.get("city"),
        "Region": response.get("region"),
        "Country": response.get("country_name"),
	    "Time Zone" : response.get("timezone"),
	    "ISP" : response.get("org"),
	    "Latitude" : response.get("latitude"),
<<<<<<< HEAD
	"Longitude" :response.get("longitude"),}
=======
	"Longitude" :response.get("longitude"), }
>>>>>>> 51bbe46395bcca663061a9c2a7f74a243fb57a33
    return location_data
if __name__ == "__main__":
    app.run()
