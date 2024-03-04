import requests

def get_ip():
    response = requests.get('https://api.ipify.org?format=json').json()
    return response["ip"]

def get_location():
    ip_address = get_ip()
    response=requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "IPv4 Address": ip_address, 
        "City": response.get("city"),
        "Region": response.get("region"),
        "Country": response.get("country_name"),
        
    }
    return location_data


print("The user's IPv4 address and current location is as follows:")
print(get_location())
