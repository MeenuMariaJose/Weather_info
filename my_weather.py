import json, requests

def know_your_weather(API_KEY, location):
    
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
 # complete url address
    url = base_url + "appid=" + API_KEY + "&q=" + location
   
    response=requests.get(url)
    data=response.json()

    if data['cod']== 200:
      #  print(data['main'])

        weather={"Location":data['name'],
               "description":data['weather'][0]['description'],
               "weather info":data['main']

               }
        return weather
   
    else:
      return data

if __name__=="__main__":

  location = input("enter your location \n")
  api_key = "8c39a1117759d102e76aa34344b125eb"

  data=know_your_weather(api_key,location)
  print(data)



#sample data
    #  {'coord': {'lon': 76.7464, 'lat': 9.8367},
      #   'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}],
      #   'base': 'stations', 
      #   'main': {'temp': 309.46, 'feels_like': 308.42, 'temp_min': 309.46, 'temp_max': 309.46, 'pressure': 1012, 'humidity': 24, 'sea_level': 1012, 'grnd_level': 1004}, 
      #   'visibility': 10000, 'wind': {'speed': 1, 'deg': 30, 'gust': 3.99}, 
      #   'clouds': {'all': 100}, 
      #   'dt': 1709276061,
      #    'sys': {'country': 'IN', 'sunrise': 1709255241, 'sunset': 1709298221}, 
      #   'timezone': 19800, 'id': 1272022, 'name': 'Muttam', 'cod': 200} 
