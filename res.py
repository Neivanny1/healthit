import json
import requests

def getLatLon(villageName, country="Kenya"):
    url = f"https://nominatim.openstreetmap.org/search?q={villageName}, {country}&format=json&addressdetails=1"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        if data:
            return {
                'latitude': data[0]['lat'],
                'longitude': data[0]['lon'],
                'village_name': villageName
            }
        else:
            return {
                'latitude': None,
                'longitude': None,
                'village_name': villageName
            }
    except Exception as e:
        print("Error:", e)
        return {
            'latitude': None,
            'longitude': None,
            'village_name': villageName
        }

try:
    with open('villages.json') as f:
        villages_data = json.load(f)
    
    villages_with_coordinates = []
    for village in villages_data:
        village_name = village['village_name']
        lat_lon_data = getLatLon(village_name)
        villages_with_coordinates.append({
            'village_id': village['village_id'],
            'village_name': village['village_name'],
            'latitude': lat_lon_data['latitude'],
            'longitude': lat_lon_data['longitude']
        })
    
    with open('village_coordinates.json', 'w') as outfile:
        json.dump(villages_with_coordinates, outfile, indent=2)
    
    print("Data saved to village_coordinates.json")
    
except FileNotFoundError:
    print("Error: villages.json file not found.")
except Exception as e:
    print("Error:", e)
