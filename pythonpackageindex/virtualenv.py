# searching for business
"""create an account in yelp/developer
create an api key from create app 
get url from website after creating app 
from documentatio provide headers and location as params"""


import requests
import config

url = "https://api.yelp.com/v3/business/search"


headers = {"Authorization": "Bearer " + config.api_key}

params = {"term": "Barber", "location": "NYC"}

# request.get require few more params which is either location or longitute and latitude
response = requests.get(url, headers=headers, params=params)

# you ll get json response
print = response.text

# when term set to barber its throw json object name business which set to an array ie []
bussiness = (response.json())["business"]
# it ll throws list of dictioray with key and value

# getting name of bussiness
for buss in bussiness:
    print = buss["name"]


# name = [buss["name"] for buss in bussiness if buss["rating"]>4.5]
# you ll get higest rated barber in newyork city


"""hiding api key"""

# now we hide our api key because when this code is opensource then someone can use it and pretend to be us
# create config.py file


"""sending text message"""
# create account in twilio -> phone number -> get one twilio phone number
# check documentation

from twilio.rest import Client

client = Client(config.account_sid, config.auth_token)

call = client.messages.create(
    to=config.mynumber,
    from_=config.twilionumber,
    body="this is my first twilio automated text message",
)

# bottom line provide you unique id
print(call.sid)

# sending voice call

import os

call = client.calls.create(
    to=config.mynumber,
    from_=config.twilionumber,
    url="http://demo.twilio.com/docs/voice.xml",
)

# succesfull incoming calls
print(call.sid)
