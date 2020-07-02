# import required modules 
import requests, json 

# Enter your API key here 

def get_prayer(user_message):
    api_key = "0c42f7f6b53b244c78a418f4f181282a"

    # base_url variable to store url 
    base_url = "http://api.aladhan.com/v1/calendarByCity?"
    city = "Innopolis"
    country = "Russia"

    # Give city name 
    # city_name = input("Enter city name : ") 

    complete_url = "http://api.aladhan.com/v1/calendarByCity?city=Innopolis&country=Russia&method=1"

    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 


    x = response.json() 

    if x["code"] != "404": 

        y = x["data"][1]["timings"]
        l=['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']
        prayer_time= {key: y[key] for key in l}

        # for prayer in prayer_time.keys():
            # prayers = Fajr
        if user_message.capitalize() in l :
    # print(prayer_time)
            prayer= user_message.capitalize()
            return "The time for {} is {}".format(prayer, prayer_time[prayer])
        elif user_message.lower() =="magrib":
            prayer ="Maghrib"
            return "The time for {} is {}".format(prayer, prayer_time[prayer])
        else:            
            return "the time for prayers are {}".format( prayer_time)

        # return prayer_time
    else: 
        # print(" City Not Found ") 
        return "City not found"
# print(get_prayer())