# you need an api key to run this program http://sunlightfoundation.com/api/accounts/register/
# This prrogram will find the members of Congress that represent a given zipcode

# the json module will help us use the information we get as lists and dictionaries
import json
# install this if you don't have it, use pip install or easy_install
import requests

# this lets us access Sunlight APIs
apikey = # get your own at http://sunlightfoundation.com/api/accounts/register/

# We structure api calls by reading documentaion about them: 
# The documentation for the Congress API is at https://sunlightlabs.github.io/congress/
# We can also use Sunlight's query builder to help us understand how to format our query http://tryit.sunlightfoundation.com/congress

# This is the url that we are going to use to contact the API
# The legislators/locate part is the methoid we are using, we can think of it as part as telling the API what kind of information we are interested in
endpoint = 'https://congress.api.sunlightfoundation.com/legislators/locate'

# We started out with this hard coded but we made this something the users can decide
zip = raw_input("give me a zipcode: ")

# These are the arguements we want to pass in. These variables are the way we ask the API questions.
query_params = {'zip': zip, 'apikey': apikey}

# Here we are using the requests package to format our url for us and get the information from the website.
# .get is a function in the requests package we are using.
# We pass in a dictionary of variables we want after the endpoint. (Check out the Requests documentation for more informaion.) 
response = requests.get(endpoint, params=query_params)

# The requests library makes it easy for us to check what url it is using for its request. This is great for debugging! Put this url into a browser and see your result.
print(response.url)
# it should look something like:
# https://congress.api.sunlightfoundation.com/legislators/locate?zip=92886&apikey=your_key 

# We are using the json module to get the data into a format python can easily use.
data = response.json()

# Looping through each person in the results list that was returned from the API
for result in data['results']:
	# for each person we are going to concatinate their title and name. Concatinate just means add strings.
	name = result['title'] + " " +  result['last_name'] 
	print name
