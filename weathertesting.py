import random
from citipy import citipy
import numpy as np
import requests as req
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date
import time

#empty list to contain all randomly generated city names and their country names
cities_list = []
#for the lats
lat_list = []

# might have to use your own api keys. it only ever let me run 500 locations once.
api_key = "fb020e65e37a62649123a9dd49f47d84"
temp_type = "imperial"

#counter 
x = 0

#empty lists to contain all the weather data
temp = []
humidity = []
cloudiness = []
wind = []

while x < 500:
	#generating random numbers to create the geocodes and then storing the lat coordinates into list
	lat_coor = random.uniform(-90.0, 90.0)
	long_coor = random.uniform(-180, 180)
	lat_list.append(lat_coor)

	#assigns city and country codenames to the variables
	city = citipy.nearest_city(lat_coor, long_coor).city_name
	country = citipy.nearest_city(lat_coor, long_coor).country_code
	
	#if this city is not already in cities_list, add it in and add 1 to x
	# skips this code if city already exists within this list
	if city not in cities_list:
		cities_list.append([city, country])
		x += 1

		#creating the url for each location and requesting the json files
		url = "http://api.openweathermap.org/data/2.5/weather?q=%s,%s&APPID=%s&units=%s" % (cities_list[x-1][0], cities_list[x-1][1], api_key, temp_type)
		get_weather = req.get(url).json()
		
		#adding into the empty lists
		temp.append(get_weather['main']['temp'])
		humidity.append(get_weather['main']['humidity'])
		cloudiness.append(get_weather["clouds"]["all"])
		wind.append(get_weather['wind']['speed'])

		#prints out city number, city + country, and its respective api url to get the api
		print(str(x) + ". " + str(cities_list[x-1][0]) + ", " + str(cities_list[x-1][1]) + "   \n" + url + "\n")
		time.sleep(5)





#finding the absolute values of the latidude so they are all positive
#regardless if they're above or below equator
abs_lat = [abs(number) for number in lat_list]


#making the grids light grey
sns.set_style("darkgrid", {"axes.facecolor": ".9"})


#temp vs latitude

title = "Temperature (F) by distance from equator for %s" % (date.today())

plt.scatter(abs_lat, temp)
plt.xlabel("absolute latitude")
plt.ylabel("temp")
plt.xlim(-20, 100)
plt.ylim(-20, 120) 
plt.title(title)
plt.show()

sns.distplot(temp)

#humidity vs latitude

title = "Humidity levels by distance from equator for %s" % (date.today())

plt.scatter(abs_lat, humidity)
plt.xlabel("absolute latitude")
plt.ylabel("humidity")
plt.xlim(-20, 100)
plt.ylim(-20, 120)
plt.title(title)
plt.show()


#cloudiness vs latitude
title = "Cloudiness by distance from equator for %s" % (date.today())

plt.scatter(abs_lat, cloudiness)
plt.xlabel("absolute latitude")
plt.ylabel("cloudiness")
plt.xlim(-20, 100)
plt.ylim(-20, 120)
plt.title(title)
plt.show()

#windspeed vs latitude
title = "Windspeed by distance from equator for %s" % (date.today())

plt.scatter(abs_lat, wind)
plt.xlabel("absolute latitude")
plt.ylabel("windspeed")
plt.xlim(-20, 100)
plt.ylim(-20, 120)
plt.title(title)
plt.show()


print("The only noticable trend is with temperature vs latitude. As you travel further away from the equator (higher absolute lat), temperature slowly decreased")










