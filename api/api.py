import requests as rq

api = '274fa086b0cf276bc98ea138d51ed25a'


def deg_to_direction(deg):
    directions = [
        "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
        "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW", "N"
    ]
    index = round(deg / 22.5) % 16
    return directions[index]


def get_all_city_info(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric'

    response = rq.get(url).json()

    weather_data = {
        'general': response["weather"][0]["main"],
        'description': response["weather"][0]["description"],
        'temperature': f'{response["main"]["temp"]}°C',
        'feels_like': f'{response["main"]["feels_like"]}°C',
        'temp_min': f'{response["main"]["temp_min"]}°C',
        'temp_max': f'{response["main"]["temp_max"]}°C',
        'pressure': f'{response["main"]["pressure"]} hPa',
        'humidity': f'{response["main"]["humidity"]}%',
        'wind_speed': f'{response["wind"]["speed"]} m/s',
        'wind_dir': f'{deg_to_direction(float(response["wind"]["deg"]))}',
        'clouds': f'{response["clouds"]["all"]}%',
        'visibility': f'{response.get("visibility", "N/A")} m',
        'timezone': f'{response["timezone"] // 3600} UTC',
        'city': response["name"],
        'country': response["sys"]["country"]
    }

    if 'gust' in response["wind"]:
        weather_data['gust'] = f'{response["wind"]["gust"]} m/s'
    else:
        weather_data['gust'] = f'no gust'

    if 'rain' in response:
        weather_data['rain'] = f'{response["rain"].get("1h", 0)} mm'

    return weather_data


def get_all_cords_info(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}&units=metric"

    response = rq.get(url).json()

    weather_data = {
        'general': response["weather"][0]["main"],
        'description': response["weather"][0]["description"],
        'temperature': f'{response["main"]["temp"]}°C',
        'feels_like': f'{response["main"]["feels_like"]}°C',
        'temp_min': f'{response["main"]["temp_min"]}°C',
        'temp_max': f'{response["main"]["temp_max"]}°C',
        'pressure': f'{response["main"]["pressure"]} hPa',
        'humidity': f'{response["main"]["humidity"]}%',
        'wind_speed': f'{response["wind"]["speed"]} m/s',
        'wind_deg': f'{deg_to_direction(float(response["wind"]["deg"]))}',
        'clouds': f'{response["clouds"]["all"]}%',
        'visibility': f'{response.get("visibility", "N/A")} m',
        'timezone': f'{response["timezone"] // 3600} UTC',
        'city': response["name"],
        'country': response["sys"]["country"]
    }

    if 'gust' in response["wind"]:
        weather_data['gust'] = f'{response["wind"]["gust"]} m/s'
    else:
        weather_data['gust'] = f'no gust'

    if 'rain' in response:
        weather_data['rain'] = f'{response["rain"].get("1h", 0)} mm'

    return weather_data


def check_city_exists(city):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api}"
    response = rq.get(url).json()
    cities = 0

    for _ in response:
        cities += 1

    if cities == 0:
        return False
    else:
        return True


def get_all_locations(city_name):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={api}"
    response = rq.get(url).json()

    locations = []
    city_lower = city_name.lower()

    for x in response:
        if x['name'].lower() == city_lower:
            location_data = {
                'country': x['country'],
                'state': x.get('state', ''),
                'lat': x['lat'],
                'lon': x['lon'],
                'city': x['name']
            }
            locations.append(location_data)

    return locations
