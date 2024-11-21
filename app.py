import requests
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])  # Ensure POST method is specified
def index():
    # Get the JSON data sent from Dialogflow
    data = request.get_json()

    # Extract the city name from JSON data
    city = data['queryResult']['parameters']['geo-city']

    # Get weather info
    weather_info = get_weather_info(city)

    # Return the weather info to Dialogflow
    return jsonify({
        "fulfillmentText": weather_info
    })


def get_weather_info(city):
    api_key = "9af8fe35d12baf4ce48634f3821e40e3"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # Make the GET request to fetch weather data
    response = requests.get(url)

    data = response.json()

    # Extract the weather description and temperature
    description = data['weather'][0]['description']
    temperature = data['main']['temp']

    return f"The temperature in {city} is {temperature}°C and the weather is {description}."


if __name__ == '__main__':
    app.run(debug=True)

