#Importing flask for the application
import os
from flask import Flask, render_template , request, send_from_directory  #importing libraries to create a web app and display it on our browser.
from flask_cors import CORS

#Add API routes by decorating functions with @app.route(): for users
# app.py

#Importing routes from the routing files in the routes folder of the main folder "insights-dashboard-api\insights-dashboard-api\routes"
from routes.blogs import blog_routes
from routes.feeds import feeds_routes 
from routes.monthly_sales import monthly_sales_routes
from routes.top_cards import top_cards_routes
from routes.top_customers import top_customers_routes

app = Flask(__name__)
CORS(app)

# Configure Flask to serve the assets directory
app.config['STATIC_FOLDER'] = os.path.join(os.path.dirname(__file__), 'assets')

@app.route('/assets/<path:filename>')
def send_file(filename):
    return send_from_directory(app.config['STATIC_FOLDER'], filename)


@app.route('/')
def home():
    return 'This is the home page for the API'
# Registering the blueprints to the main app
app.register_blueprint(blog_routes)
app.register_blueprint(feeds_routes)
app.register_blueprint(monthly_sales_routes)
app.register_blueprint(top_cards_routes)
app.register_blueprint(top_customers_routes)

if __name__ == '__main__':
    app.run()


