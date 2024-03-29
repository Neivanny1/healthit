async function getLatLon(villageName, country = "Kenya") {
    const url = `https://nominatim.openstreetmap.org/search?q=${villageName}, ${country}&format=json&addressdetails=1`;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }

        const data = await response.json();
        if (data.length > 0) {
            return {
                latitude: data[0].lat,
                longitude: data[0].lon,
                address: data[0]
            };
        } else {
            console.log(`Village '${villageName}' not found in ${country}`);
            return null;
        }
    } catch (error) {
        console.error(error);
        return null;
    }
}

// Example usage
const villageName = "Nyawita";
getLatLon(villageName)
    .then(locationData => {
        if (locationData) {
            console.log(`Latitude: ${locationData.latitude}`);
            console.log(`Longitude: ${locationData.longitude}`);
            console.log(`Address: ${JSON.stringify(locationData.address)}`);
        }
    });
