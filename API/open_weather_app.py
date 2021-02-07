import requests
from datetime                   import datetime


def get_current_weather_by_city_name(city_name):

    api_key = "f7c6ca0448a4bb6b626a01a57e60274e"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=" + 'metric'

    response = requests.get(complete_url)
    request = response.json()
    results = {}

    print(request)
    if request["cod"] != "404":

        results['weather']  = request['weather'][0]['main']

        main_result         = request["main"]

        results['temp']     = main_result["temp"]
        results['min']      = main_result["temp_min"]
        results['max']      = main_result["temp_max"]

        results['pressure'] = main_result["pressure"]
        results['humidity'] = main_result["humidity"]

    return results


def get_period_weather_by_city_name(city_name, period):

    api_key = "f7c6ca0448a4bb6b626a01a57e60274e"
    base_url = "http://api.openweathermap.org/data/2.5/forecast?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=" + 'metric' + "&cnt=" + str(period)

    response = requests.get(complete_url)
    request = response.json()
    results = {}

    print(request)
    if request["cod"] != "404":

        for day, day_result in enumerate(request['list']):
            day = day + 1
            results[day] = {}

            results[day]['weather']  = day_result['weather'][0]['main']

            main_result              = day_result["main"]

            results[day]['temp']     = main_result["temp"]
            results[day]['min']      = main_result["temp_min"]
            results[day]['max']      = main_result["temp_max"]

            results[day]['pressure'] = main_result["pressure"]
            results[day]['humidity'] = main_result["humidity"]

    return results


def get_data_by_location(latitude, longitude):
    api_key = "f7c6ca0448a4bb6b626a01a57e60274e"

    base_url = "https://api.openweathermap.org/data/2.5/onecall?"

    lat = 28.6667
    lon = 77.2167

    # complete_url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}"

    complete_url = f"https://api.openweathermap.org/data/2.5/onecall?lat=33.441792&lon=-94.037689&appid={api_key}"
    #
    # Give city name
    city_name = input("Enter city name : ")

    # complete_url variable to store
    # complete url address

    #
    # complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()

    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    print(x)
    if x["cod"] != "404":

        # store the value of "main"
        # key in variable y

        y = x["main"]

        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]

        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]

        # store the value corresponding
        # to the "humidity" key of y
        current_humidiy = y["humidity"]

        # store the value of "weather"
        # key in variable z
        z = x["weather"]

        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]

        # print following values
        print(" Temperature (in kelvin unit) = " +
              str(current_temperature) +
              "\n atmospheric pressure (in hPa unit) = " +
              str(current_pressure) +
              "\n humidity (in percentage) = " +
              str(current_humidiy) +
              "\n description = " +
              str(weather_description))

    else:
        print \
            (" City Not Found ")