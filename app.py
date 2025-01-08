import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Clé API OpenWeatherMap (remplace-la par ta propre clé si nécessaire)
api_key = "673f5bbe15b1a94a502550359930545f"

def get_weather_data(city):
    """
    Récupère les données météo à partir de l'API OpenWeatherMap.
    """
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",  # Unités en Celsius
        "cnt": 10  # Nombre de prévisions (par exemple, 10 prévisions)
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if response.status_code == 200:
        return data
    else:
        st.error(f"Erreur lors de la récupération des données : {data.get('message', '')}")
        return None

def plot_temperature(data):
    """
    Trace un graphique de température à partir des données récupérées.
    """
    # Extraire les temps et les températures
    times = []
    temps = []
    for forecast in data['list']:
        times.append(datetime.datetime.fromtimestamp(forecast['dt']))
        temps.append(forecast['main']['temp'])
    
    # Créer un DataFrame pandas pour les données
    df = pd.DataFrame({
        'Time': times,
        'Temperature (°C)': temps
    })
    
    # Tracer le graphique
    plt.figure(figsize=(10, 6))
    plt.plot(df['Time'], df['Temperature (°C)'], marker='o', linestyle='-', color='b')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.title('Prévisions de température')
    plt.xticks(rotation=45)
    st.pyplot(plt)

def main():
    st.title("Application Météo avec OpenWeatherMap")
    st.write("Bienvenue dans l'application Streamlit utilisant OpenWeatherMap pour afficher les prévisions météo!")

    # Saisir la ville
    city = st.text_input("Entrez le nom de votre ville:", "Paris")
    
    if city:
        st.write(f"Récupération des prévisions météo pour {city}...")
        
        # Récupérer les données météo pour la ville
        data = get_weather_data(city)
        
        if data:
            # Afficher un graphique de la température
            plot_temperature(data)

if __name__ == "__main__":
    main()
