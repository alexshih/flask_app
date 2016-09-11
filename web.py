# Flask allows developers to put Python code into html files

# Adding Weather into App
from flask import Flask, render_template, request
import weather
app = Flask(__name__)

@app.route("/")
def index():
    address = request.values.get('address')
    forecast = None
    if address:
        forecast = weather.get_weather(address)
    return render_template('index.html', forecast=forecast)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()

# From Creating an About Page
# from flask import Flask, render_template
# app = Flask(__name__)# 

# @app.route("/")
# def index():
#     return render_template('index.html')# 

# @app.route('/about')
# def about():
#     return render_template('about.html')# 

# if __name__ == "__main__":
#     app.run()

# Getting Python Variables into your HTML Code
# from flask import Flask, render_template, request
# app = Flask(__name__)# 

# @app.route("/")
# def index():
# 	# .get avoids a KeyError if there isn't a 'name' parameter
#     name = request.values.get('name')
#     return render_template('index.html', name=name)# 

# @app.route('/about')
# def about():
#     return render_template('about.html')# 

# if __name__ == "__main__":
#     app.run()
