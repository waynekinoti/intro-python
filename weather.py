import json
from datetime import datetime

file = open('weather.json', "r")

data = file.read()
# print(type(data))
json_data = json.loads(data)
# print(type(json_data))

# print(json_data['main']['temp'])

weather = json_data['weather'][0]['main']
# print(weather)

# print(json_data['wind']['speed'])

# sunrise
# fomart and print 10:30PM
# epoch

sunrise_time = json_data['sys']['sunrise']
value = datetime.fromtimestamp(sunrise_time).strftime('%H:%M')
print(value)
