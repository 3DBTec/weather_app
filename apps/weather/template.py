def path(class_name):

    templates_map = {

        'WeatherSearchView':              ['weather/weather_search.html'],
        'WeatherResultsView':             ['weather/weather_results.html'],
        'BarChartJSONView':               ['weather/weather_results.html'],
        'LineChartJSONView':              ['weather/line_chart.html'],
    }

    return templates_map[class_name]
