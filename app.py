
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import pymongo 
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# create mongo connection

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)


db = client.mars_db
collection = db.mars_data_collection
mars_info = scrape_mars.scrape()

collection.insert_many(mars_info)

@app.route("/")


def home():
    mars_ = db.collection.find_one()
    return  render_template('index.html', mars_=mars_)

@app.route("/scrape")

def scrape():


    mars_info = scrape_mars.scrape()
    collection.insert_many(mars_info)
    return  redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)