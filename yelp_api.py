# https://www.yelp.com/developers/documentation/v2/search_api

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_businesses(location, term):
	auth = Oauth1Authenticator(
		consumer_key=os.environ['CONSUMER_KEY'],
	    consumer_secret=os.environ['CONSUMER_SECRET'],
	    token=os.environ['TOKEN'],
	    token_secret=os.environ['TOKEN_SECRET']
    )

	client = Client(auth)

	# Only return 3 Yelp results
	params = {
		'term': term,
		'lang': 'en',
		'limit': 3,
		'sort': 2
	}

	response = client.search(location, **params)

	# Initialize this List variable
	businesses = []

	# Getting back something from Yelp API
	for business in response.businesses: 
		# print(business.name, business.rating, business.phone)
		
		# Adding business name to List variable
		businesses.append({"name": business.name,
			"rating": business.rating,
			"phone": business.phone
		})
	
	return businesses
