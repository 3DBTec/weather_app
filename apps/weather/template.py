def path(class_name):

    templates_map = {

        'WeatherSearchView':              ['weather/weather_search.html'],
        'WeatherResultsView':             ['weather/weather_results.html'],
    }

    return templates_map[class_name]
