# you need an api key to run this program http://sunlightfoundation.com/api/accounts/register/

import json
# install this later
import requests

apikey = # get your own at http://sunlightfoundation.com/api/accounts/register/

# /legislators/locate?zip=11216

endpoint = 'https://congress.api.sunlightfoundation.com/legislators/locate'

zip = raw_input("give me a zipcode: ")

query_params = {'zip': zip, 'apikey': apikey}

response = requests.get(endpoint, params=query_params)

print(response.url)

data = response.json()

for result in data['results']:
	name = result['title'] + " " +  result['last_name'] 
	print name
