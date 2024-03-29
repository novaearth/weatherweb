from flask import Flask, render_template, redirect
import requests

app = Flask(__name__)
app.debug = True

# Function to get weather information from an API
def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return None

# Function to display weather information
def display_weather(weather_data):
    if weather_data is not None and 'main' in weather_data:
        temperature = weather_data['main']['temp']
        unit = "Celsius"
        city_name = weather_data['name']
        return f"Temperature in {city_name} is at: {temperature} {unit}"
    else:
        return "Failed to retrieve weather information."

# Route for home page
@app.route('/')
def home():
    api_key = '3adebbf04afecd3bdfb24870b9258984'
    city = 'São Paulo'
    weather_data = get_weather(api_key, city)
    weather_info = display_weather(weather_data)
    return render_template('index.html', weather_info=weather_info)

# Custom route for the Earth Weather link
@app.route('/earth/weather')
def custom_link():
    return redirect('/')

if __name__ == "__main__":
    app.run(ssl_context='adhoc')
