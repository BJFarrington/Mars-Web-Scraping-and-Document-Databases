
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars_adjusted

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars")


@app.route("/")
def home():
    
    mars_data = mongo.db.mars_collection.find_one()
    return render_template("index.html", mars=mars_data)

@app.route("/scrape")
def scraper():
    mars_scrape = mission_to_mars_adjusted.scrape()
    mongo.db.mars_collection.update({}, mars_scrape, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)