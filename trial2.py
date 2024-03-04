import requests  # Importing the requests module which is used to send HTTP requests

def get_location(ip_address):
    # Sending a GET request to retrieve location information based on the provided IP address
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    # Creating a dictionary to store location data
    location_data = {
        "IP Address": ip_address,  # Storing the IP address
        "City": response.get("city"),  # Storing the city name
        "Region": response.get("region"),  # Storing the region name
        "Country": response.get("country_name"),  # Storing the country name
    }
    return location_data  # Returning the location data dictionary

def main():
    ip_version = input("Do you want to use IPv4 or IPv6? (Enter 'ipv4' or 'ipv6'): ").lower()
    if ip_version not in ['ipv4', 'ipv6']:
        print("Invalid input. Defaulting to IPv4.")
        ip_version = 'ipv4'
        
    if ip_version == 'ipv4':
        ip_address = input("Insert your IPv4 address here: ")
    else:
        ip_address = input("Insert your IPv6 address here: ")
        
    location_data = get_location(ip_address)  # Getting location data using the get_location() function
    print("The provided IP address and its current location is as follows:")
    # Iterating through the location data dictionary and printing each key-value pair
    for key, value in location_data.items():
        print(f"{key}: {value}")  # Printing each key-value pair with a formatted string

if __name__ == "__main__":
    main()
