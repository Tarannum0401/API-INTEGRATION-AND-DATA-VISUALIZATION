import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set seaborn style
sns.set(style="whitegrid")

# --- 1. Set up API credentials and parameters ---
API_KEY = '1588dbb996defb331caadb665c669cae'  
CITY = 'Mumbai'
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# --- 2. Fetch data from OpenWeatherMap API ---
response = requests.get(URL)

if response.status_code != 200:
    raise Exception("API request failed with status code: " + str(response.status_code))

data = response.json()

# --- 3. Parse the data for temperatures and timestamps ---
forecast_list = data['list']

# Extract time and temperature data
dates = [datetime.strptime(item['dt_txt'], "%Y-%m-%d %H:%M:%S") for item in forecast_list]
temperatures = [item['main']['temp'] for item in forecast_list]
humidity = [item['main']['humidity'] for item in forecast_list]

# --- 4. Create visualizations ---

plt.figure(figsize=(14, 6))

# Temperature Line Plot
plt.subplot(1, 2, 1)
plt.plot(dates, temperatures, color='tomato', marker='o')
plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Date and Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()

# Humidity Line Plot
plt.subplot(1, 2, 2)
sns.lineplot(x=dates, y=humidity, color='skyblue', marker='o')
plt.title(f"Humidity Forecast for {CITY}")
plt.xlabel("Date and Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.suptitle(f"5-Day Weather Forecast for {CITY}", fontsize=16)
plt.subplots_adjust(top=0.85)
plt.show()
