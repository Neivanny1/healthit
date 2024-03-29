import requests

def get_lat_lon(village_name, state="Kenya", county_param=None):
    """
    Fetches latitude and longitude of a village in Kenya, handling potential duplicates.

    Args:
        village_name (str): The name of the village.
        state (str, optional): The country of the village. Defaults to "Kenya".
        county_param (str, optional): The state name to narrow down search.

    Returns:
        dict: A dictionary containing latitude, longitude, address, and disambiguation options
              if duplicates are found, or None if not found.

    Raises:
        requests.exceptions.RequestException: If an error occurs during the request.
    """

    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": village_name + ", " + state,
        "format": "json",
        "addressdetails": 1,
    }

    if county_param:
        params["state"] = county_param  # Add state parameter if provided

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for non-200 status codes
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

    data = response.json()

    if len(data) == 0:
        print(f"Village '{village_name}' not found in {state}")
        return None

    # Handle single result (no duplicates)
    elif len(data) == 1:
        return {
            "name": data[0]["name"],
            "latitude": data[0]["lat"],
            "longitude": data[0]["lon"],
            "address": data[0]["display_name"],
            "duplicates": False,
        }

    # Handle multiple results (potential duplicates) with state prioritization
    else:
        # Prioritize results within the specified state:
        county_results = [d for d in data if d.get("state", "") == county_param]
        if county_results:
            return county_results[0]

        # If no results within state, present disambiguation options from all results:
        print(f"Multiple locations found for '{village_name}' in {state}:")
        for i, location in enumerate(data):
            print(f"{i+1}. {location['display_name']}")
        return {
            "name": None,  # Indicate uncertainty due to duplicates
            "latitude": None,
            "longitude": None,
            "address": None,
            "duplicates": True,
            "disambiguation_options": data,
        }

# Example usage with state paramer
village_name = "Asego"
state = "Homa Bay"
location_data = get_lat_lon(village_name, state=state)

if location_data:
    if location_data["duplicates"]:
        print("Please choose the most relevant location:")
        for i, option in enumerate(location_data["disambiguation_options"]):
            print(f"{i+1}. {option['display_name']}")
    else:
        print(f"Latitude: {location_data['latitude']}")
        print(f"Longitude: {location_data['longitude']}")
        print(f"Address: {location_data['address']}")
else:
    print("Location not found.")
