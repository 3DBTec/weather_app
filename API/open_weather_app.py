import requests


def get_current_weather_by_city_name(city_name):

    api_key = "f7c6ca0448a4bb6b626a01a57e60274e"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city_name}&units=metric"

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
    complete_url = f"{base_url}appid={api_key}&q={city_name}&units=metric&cnt={period}"

    response = requests.get(complete_url)
    request = response.json()
    results = {}
    graphs = {}

    categories  = []
    series_min  = []
    series_max  = []
    series_temp = []

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

            categories.append(day)
            series_min.append(main_result["temp_min"])
            series_max.append(main_result["temp_max"])
            series_temp.append(main_result["temp"])

    graphs['categories']  = categories
    graphs['series_min']  = series_min
    graphs['series_max']  = series_max
    graphs['series_temp'] = series_temp

    return results, graphs
