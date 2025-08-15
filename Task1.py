import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


# configurations
API_KEY="1588dbb996defb331caadb665c669cae"
CITY_NAME="London"
COUNTRY_CODE="44"
UNITS="metric"


# Fetch data
def fetch_weather(city,api_key, country_code,units="metric"):
    url= f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
    response=requests.get(url)
    response.raise_for_status()
    return response.json()


# processs data
def process_data(data):
    times=[]
    temps=[]
    weather_conditions=[]

    for entry in data ['list']:
        dt=datetime.strptime(entry['dt_txt'],'%Y-%m-%d %H:%M:%S')
        temp=entry['main']['temp']
        condition=entry['weather'][0]['main']

        times.append(dt)
        temps.append(temp)
        weather_conditions.append(condition)
    return times,temps,weather_conditions


# visulization
def plot_forecast(times,temps,weather_conditions,city):
    sns.set(style="darkgrid")
    plt.figure(figsize=(14,6))

    # plot
    sns.lineplot(x=times,y=temps,hue=weather_conditions,markers="o",palette="tab10")


    # lables
    plt.title(f'5-Day Temperature Forecast for {city}',fontsize=16)
    plt.xlabel("Date & Time")
    plt.ylabel("Temperture(°c)")
    plt.xticks(rotation=45)
    plt.legend(title="weather condition")
    plt.tight_layout()
    plt.show()


# main
if __name__=='__main__':
    print(f"Fetching weather data for {CITY_NAME}....")
    raw_data= fetch_weather(CITY_NAME,API_KEY,COUNTRY_CODE,UNITS)
    times,temps,weather_conditions=process_data(raw_data)
    plot_forecast(times,temps,weather_conditions,CITY_NAME)

