import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set Seaborn theme
sns.set_theme()

# Your API key and base URL
API_KEY = 'a7edadef313fb80cb9d0612367de8edb'
CITY = 'Mumbai'
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetching the data
response = requests.get(URL)
data = response.json()

# Check for errors
if response.status_code != 200:
    print("Failed to fetch data:", data.get("message", "Unknown error"))
    exit()

# Parse the forecast list
forecast_list = data['list']

# Extracting required data
weather_data = {
    "datetime": [],
    "temperature": [],
    "humidity": [],
    "weather": []
}

for forecast in forecast_list:
    weather_data["datetime"].append(datetime.strptime(forecast['dt_txt'], '%Y-%m-%d %H:%M:%S'))
    weather_data["temperature"].append(forecast['main']['temp'])
    weather_data["humidity"].append(forecast['main']['humidity'])
    weather_data["weather"].append(forecast['weather'][0]['main'])

# Convert to DataFrame
df = pd.DataFrame(weather_data)

# 📊 Visualization

# 1. Temperature over time
plt.figure(figsize=(12, 6))
sns.lineplot(x='datetime', y='temperature', data=df, marker='o')
plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()

# 2. Humidity over time
plt.figure(figsize=(12, 6))
sns.lineplot(x='datetime', y='humidity', data=df, marker='s', color='orange')
plt.title(f"Humidity Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()

# 3. Weather condition frequency
plt.figure(figsize=(8, 5))
sns.countplot(x='weather', data=df, palette='Set2')
plt.title("Weather Condition Frequency")
plt.xlabel("Weather Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
