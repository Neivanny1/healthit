const fs = require('fs');

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
                village: villageName,
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

// Read village names from villages.json
fs.readFile('villages.json', 'utf8', async (err, data) => {
    if (err) {
        console.error("Error reading villages.json:", err);
        return;
    }
    try {
        const villages = JSON.parse(data);
        const villageCoordinates = [];

        for (const village of villages) {
            const villageName = village.village_name;
            const locationData = await getLatLon(villageName);
            if (locationData) {
                villageCoordinates.push(locationData);
            }
        }

        // Write village coordinates to a JSON file
        fs.writeFile('village_coordinates.json', JSON.stringify(villageCoordinates, null, 2), err => {
            if (err) {
                console.error("Error writing to village_coordinates.json:", err);
                return;
            }
            console.log("Village coordinates saved to village_coordinates.json");
        });
    } catch (error) {
        console.error("Error parsing JSON data from villages.json:", error);
    }
});
