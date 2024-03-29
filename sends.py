import json
import mysql.connector

# Load villages data from JSON file
with open('villages.json', 'r') as file:
    villages_data = json.load(file)

# Initialize connection variable
conn = None

try:
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='cordinates',
        password='',  # Enter your MySQL password here
        database='healthit'
    )
    cursor = conn.cursor()

    # Create table if not exists
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Village (
        village_id INT PRIMARY KEY,
        village_name VARCHAR(255),
        latitude FLOAT,
        longitude FLOAT
    )
    """
    cursor.execute(create_table_query)
    conn.commit()

    # Insert data into the table
    for village in villages_data:
        village_id = village['village_id']
        village_name = village['village_name']
        latitude = village['latitude']
        longitude = village['longitude']
        insert_query = """
        INSERT INTO Village (village_id, village_name, latitude, longitude)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (village_id, village_name, latitude, longitude))
        conn.commit()

    print("Data inserted successfully into MySQL database.")

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    # Close cursor and connection
    if conn and conn.is_connected():
        cursor.close()
        conn.close()
