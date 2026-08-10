import requests
import pandas as pd
import psycopg2
import time
from datetime import datetime
latitudes="51.5074,40.7128,35.6762,19.0760,-33.8688,28.6139,19.2967,25.7464,10.8505,27.0844"
longitudes="-0.1278,-74.0060,139.6503,72.8777,151.2093,77.2090,73.0631,82.6837,76.2711,93.6053"


url = f"https://api.open-meteo.com/v1/forecast?latitude={latitudes}&longitude={longitudes}&current_weather=true&timezone=auto"
headers = {"User-Agent": "Mozilla/5.0"}

cities = ["London", "New York", "Tokyo", "Mumbai", "Sydney","Delhi","Bhiwandi","Jaunpur","kerala","Arunachal Pradesh"]


# 1. PREPARE THE DATABASE (Log in to PostgreSQL)
connection = psycopg2.connect(
    dbname="weather_data",
    user="postgres",
    password="Aman4321#",
    host="localhost",
    port="5432"
)
cursor = connection.cursor()

# Create a customized table for your weather records
cursor.execute(""" CREATE TABLE weather_records_8August (
    id serial PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    temperature DECIMAL(5, 2),
    wind_speed DECIMAL(5, 2),
    winddirection VARCHAR(20),
    api_time TIMESTAMP,
    time_saved TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
    

""")
connection.commit() 

print("🚀 Starting live weather data collection loop...")

# 2. COLLECT Data
for i in range(3):
    
    # Grab the data from your weather URL
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        raw_json = response.json()
        clean_data = []
        current_time = str(datetime.now()) # The exact time we write to SQL
        
        # --- Your loop from image 1000009748.jpg ---
        for index, weather_location in enumerate(raw_json):
            live_weather = weather_location['current_weather']
            
            # Create your data dictionary
            weather_format = {
                'City' : cities[index],
                'Temperature' : live_weather['temperature'],
                'Wind speed' : live_weather['windspeed'],
                'winddirection' : live_weather['winddirection'],
                'time' : live_weather['time']
            }
            clean_data.append(weather_format)
            
            # SAVE THIS CITY TO POSTGRESQL (Right here inside the city loop!)
            cursor.execute("""
                INSERT INTO weather_records_8August (city, temperature, wind_speed, winddirection, api_time, time_saved) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                weather_format['City'], 
                weather_format['Temperature'], 
                weather_format['Wind speed'], 
                weather_format['winddirection'], 
                weather_format['time'],
                current_time
            ))
        
        # Permanently save all cities for this cycle
        connection.commit()
        print(f"succesfull api ")
        
        # Convert to Pandas and print to terminal (Just like your image!)
        data = pd.DataFrame(clean_data)
        print(f"\n📊 [Cycle #{i + 1}] Live Terminal View:")
        print(data.to_string(index=False))
        print("-" * 50)
        
    else:
        # Fixed the little "status_cose" typo from line 47 of the image!
        print(f"api not working program error({response.status_code})")
    
    # Wait 5 seconds before checking the weather again
    time.sleep(5)

# 3. CLOSE EVERYTHING
cursor.close()
connection.close()
print("Done! 15 minute  is up. All live data safely stored.")


