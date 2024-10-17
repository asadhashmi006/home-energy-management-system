import requests
import json

# Your ElectricityMaps API Key
API_KEY = 'j7zIBZxAhICwi'  # Replace with your actual API key

# Endpoint for electricity zones
url = 'https://api.electricitymap.org/v3/zones'

# Set headers for authentication
headers = {
    'Authorization': f'Bearer {API_KEY}',
}

# Fetch the data
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    zones_data = response.json()
    print(json.dumps(zones_data, indent=2))  # Pretty print the JSON response
else:
    print(f'Error fetching data: {response.status_code} - {response.text}')
