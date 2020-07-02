from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.your_beer_is
bjcps = list(db.bjcp.find({}, {'_id': False}))



for bjcp in bjcps:
    # for i in range(1, 20):
        print(bjcp['title'])

