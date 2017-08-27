In this homework, we find the location of 500 different cities across the world. 

We obtain different geocoordinates created by using two different random functions that we imported with random, one for the latitude and another for longitude. They are then stored into list within a bigger list

Using an api key from Openweathermap, we find the url for each of those cities located by the geocoords and grab their temp, humidity, cloudiness, and wind speed to place into empty lists.

Using those now filled lists, we graph all 500 cities to measure correlation between the distance from the equator and each of those parameters. Of the four parameters, we find that a negative correlation exists between temperature and absolute latitude, but no correlation exists between distance and the three other parameters.
