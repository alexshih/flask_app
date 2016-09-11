# Assignment #4

from flask import Flask, render_template, request
import yelp_api
import os
app = Flask(__name__)

@app.route("/")
def index():
    address = request.values.get('address')
    terms = request.values.get('terms')
    #if terms:
    #	terms = request.values.get('terms').split(',')
    if address:
    	businesses = yelp_api.get_businesses(address, terms)
    else:
    	businesses = None
    return render_template('index.html', businesses=businesses)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
	app.run()