from pymongo import MongoClient
import ssl


# This should be used to connect to the database remotely
# username and password should be called externally


# connects to the mongo atlas
def get_database_connection():
    with open("MongoURL", "r") as f:
        MongoURL = f.readline()
    client = MongoClient(MongoURL, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
    db = client["OverLunchDB"]
    return db