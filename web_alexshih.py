# Assignment #4

# Import necessary libraries
from flask import Flask, render_template, request
import yelp_api
import os
app = Flask(__name__)

# Syntax for Flask app to create Homepage
@app.route("/")
def index():
    # Collect address input from user
    address = request.values.get('address')

    # Collect terms input from user
    terms = request.values.get('terms')
    
    # If `address` variable exists, call `get_businesses` function inside yelp_api.py script    
    if address:
    	businesses = yelp_api.get_businesses(address, terms)
    else:
    	businesses = None
    
    return render_template('index.html', businesses=businesses)

# Syntax for Flask app to create About page
@app.route('/about')
def about():
    return render_template('about.html')

# To run in command line
#if __name__ == "__main__":
#	app.run()

#To deploy to Heroku
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)