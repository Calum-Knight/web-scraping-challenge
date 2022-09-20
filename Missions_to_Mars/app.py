from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/Mars_mission"
mongo = PyMongo(app)


@app.route("/")
def index():
    # find one document from our mongo db and return it.
    listings = mongo.db.listings.find_one()
    # pass that listing to render_template
    return render_template("index.html", listings=listings)

# set our path to /scrape
@app.route("/scrape")
def scraper():
    # create a listings database
    listings = mongo.db.listings
    # call the scrape function in our scrape_phone file. This will scrape and save to mongo.
    listings_data = mission_to_mars.scrape()
    # update our listings with the data that is being scraped.
    listings.update({}, listings_data, upsert=True)
    # return a message to our page so we know it was successful.
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)