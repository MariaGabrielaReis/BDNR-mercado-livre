import simplejson as json
from bson.objectid import ObjectId
import src.connectDatabase as connectDB

mongoDB = connectDB.connectToMongoDB()
buyCollection = mongoDB.buy

def show(params):
    id = params.get("id")
    buy = buyCollection.find_one({ "_id": ObjectId(id) })
    
    return json.dumps(buy, default=str)    

def create(request):
    buy = request.get_json()
    total = 0
    for product in buy["products"]:
        total += product['price']

    buy["total"] = total
    buyCollection.insert_one(buy)

    return json.dumps({"status": "OK"})
