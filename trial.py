import requests
import socket

def get_ip():
    response = requests.get('https://api.ipify.org?format=json').json()
    return response["ip"]

def get_location():
    ip_address = get_ip()
    response=requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "Public IPv4 Address": ip_address, 
        "City": response.get("city"),
        "Region": response.get("region"),
        "Country": response.get("country_name"),
	"Time Zone" : response.get("timezone"),
	"ISP" : response.get("org"),
	"Latitude" : response.get("latitude"),
	"Longitude" :response.get("longitude"),

	
        
    }
    return location_data

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)


location_data = get_location()
print("The user's Public and Local IPv4 address and current location is as follows:")
for key, value in location_data.items():
    print(f"{key}: {value}")
