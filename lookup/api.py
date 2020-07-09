import requests
import json
url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

querystring = {"lang":"en","lon":"31.1626","lat":"40.8387"}

headers = {
    'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com",
    'x-rapidapi-key': "#putyourkeyhere"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

datastore = json.loads(response.text)

timezone = datastore["data"][0]["timezone"] #Europe/Istanbul
ob_time = datastore["data"][0]["ob_time"]  #2020-07-09 12:46
city_name = datastore["data"][0]["city_name"] #Düzce
country_code = datastore["data"][0]["country_code"] #TR
app_temp = datastore["data"][0]["app_temp"] #24
icon = datastore["data"][0]["weather"]["icon"]
description = datastore["data"][0]["weather"]["description"]

import locale
import datetime
an = datetime.datetime.now()
day = datetime.datetime.strftime(an, '%d')
month = datetime.datetime.strftime(an, '%B')
year = datetime.datetime.strftime(an, '%Y')

