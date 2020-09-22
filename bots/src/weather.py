
# Python program to find current 
# weather details of any city 
# using openweathermap api 

# import required modules 
import requests, json 

# Enter your API key here 
def kelvin_celcius(temp):
    return temp-273.15
def get_weather(value, city_name):
    api_key = "0c42f7f6b53b244c78a418f4f181282a"

    # base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Give city name 
    # city_name = input("Enter city name : ") 

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 


    x = response.json() 

    if x["cod"] != "404": 

        y = x["main"]	
        current_temperature = round(kelvin_celcius(y[value]),2)
        # print(" Temperature (in kelvin unit) = "+str(current_temperature)) 
        return (" Temperature (in celcius unit) = "+str(current_temperature)+ "C") 

    else: 
        # print(" City Not Found ") 
        return "City not found"
# print(get_weather("temp"))