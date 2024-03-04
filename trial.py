import requests  # Importing the requests module which is used to send HTTP requests

def get_ip():
    # Sending a GET request to retrieve the public IP address of the user
    response = requests.get('https://api.ipify.org?format=json').json()
    return response["ip"]  # Extracting and returning the IP address from the JSON response

def get_location():
    ip_address = get_ip()  # Getting the user's IP address using the get_ip() function
    # Sending a GET request to retrieve location information based on the IP address
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    # Creating a dictionary to store location data
    location_data = {
        "IPv4 Address": ip_address,  # Storing the IPv4 address
        "City": response.get("city"),  # Storing the city name
        "Region": response.get("region"),  # Storing the region name
        "Country": response.get("country_name"),  # Storing the country name
    }
    return location_data  # Returning the location data dictionary

location_data = get_location()  # Getting location data using the get_location() function
print("The user's IPv4 address and current location is as follows:")
# Iterating through the location data dictionary and printing each key-value pair
for key, value in location_data.items():
    print(f"{key}: {value}")  # Printing each key-value pair with a formatted string
