import json
import requests

# Load data from village_coordinates.json
try:
    with open('village_coordinates.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: village_coordinates.json file not found.")
    exit()

# API endpoint
url = 'https://training.digimal.uonbi.ac.ke/api/posts_data'

# Make POST request to API endpoint
try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # Raise exception for HTTP errors
    print("Data posted successfully.")
except requests.exceptions.RequestException as e:
    print("Error posting data:", e)
