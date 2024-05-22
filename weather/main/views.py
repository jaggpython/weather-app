from django.shortcuts import render
import urllib.request
import json
from urllib.parse import quote

def index(request): 
    if request.method == 'POST': 
        city = request.POST['city'] 

        # URL encode the city name to handle special characters
        city_encoded = quote(city)

        # Construct the URL with the encoded city name
        api_key = "22aab0e265e16318e8c0f8eae84dd35c"  # Use your own API key
        url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_encoded}&appid={api_key}'

        try:
            # Source contains JSON data from API 
            source = urllib.request.urlopen(url).read() 

            # Converting JSON data to a dictionary 
            list_of_data = json.loads(source) 

            # Data for variable list_of_data 
            data = { 
                "country_code": str(list_of_data['city']['country']), 
                "coordinate": str(list_of_data['city']['coord']['lon']) + ' ' + str(list_of_data['city']['coord']['lat']), 
                "temp": str(list_of_data['list'][0]['main']['temp']) + 'K', 
                "pressure": str(list_of_data['list'][0]['main']['pressure']), 
                "humidity": str(list_of_data['list'][0]['main']['humidity']), 
            }
        except Exception as e:
            data = {"error": str(e)}
        print(data) 
    else: 
        data = {} 

    return render(request, "main/index.html", data)
