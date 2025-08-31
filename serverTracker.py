from flask import *
import trackerConfiguration
import pymongo

def importTracker(app):
    MainDB = pymongo.MongoClient("mongodb://localhost:27017/")
    devTracker = MainDB["devTracker"]

    @app.route(trackerConfiguration.trackerPushURL, methods=["POST"])
    def push():
        JSON = request.json
        try:
            if "activeApps" not in JSON:
                raise Exception("Invalid [activeApps]")

            if JSON["secretCode"] != trackerConfiguration.secretCode:
                raise Exception("Invalid secret code")
        except Exception as e:
            return str(e), 400

        # if not exists "user" collection, create it
        if "devTracker" not in devTracker.list_collection_names():
            devTracker.create_collection("devTracker")

        DevTracker = devTracker["devTracker"]

        currentValue = DevTracker.find_one({"username": "dsvl0"})
        if currentValue:
            DevTracker.update_one({"username": "dsvl0"}, {"$set": {"activeApps": JSON["activeApps"]}})
        else:
            DevTracker.insert_one({"username": "dsvl0", "activeApps": JSON["activeApps"]})

        return "ok", 200