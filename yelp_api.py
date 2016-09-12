# Import necessary libraries
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os

# Import environment variables from .env file
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
	
	# Convert user inputted term(s) into a List, separated by ","
	terms = term.split(', ')

	# Combine List items into a single string joined together with a "+"
	terms_string = "+".join(terms)

	# Parameters to include in the response
	params = {
		'term': terms_string,
		'lang': 'en',
		'limit': 3, 	# Only return 3 Yelp results
		'sort': 2		# Sort by highest rated
	}

	response = client.search(location, **params)

	# Initialize `businesses` List variable
	businesses = []

	# Getting back something from Yelp API
	for business in response.businesses: 
		# print(business.name, business.rating, business.phone)
		
		# Adding business name to List variable
		businesses.append({"name": business.name,
			"rating": business.rating,
			"phone": business.display_phone,
			"address": business.location.display_address
		})

	return businesses
