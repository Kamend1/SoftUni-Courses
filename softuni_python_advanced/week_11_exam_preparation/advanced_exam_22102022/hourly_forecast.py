def forecast(*forecasts):
    for forecast in forecasts:
        location, weather = forecast
        locations_dict[weather].append(location)

    result = ''
    for k, v in locations_dict.items():
        for location in sorted(v):
            result += f"{location} - {k}\n"

    return result

locations_dict = {'Sunny': [], 'Cloudy': [], 'Rainy': []}


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
