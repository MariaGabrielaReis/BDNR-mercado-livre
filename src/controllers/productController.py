import simplejson as json
from bson.objectid import ObjectId
import src.connectDatabase as connectDB

mongoDB = connectDB.connectToMongoDB()
productCollection = mongoDB.product

def index():
    response = []
    for product in productCollection.find().sort("price"):
        response.append({"name": product['name'], "description": product['description'], "price": product['price']})
    
    return json.dumps(response)

def show(params):
    id = params.get("id")
    product = productCollection.find_one({ "_id": ObjectId(id) })

    return json.dumps(product, default=str)

def create(request):
    product = request.get_json()
    productCollection.insert_one(product)

    return json.dumps({"status": "OK"})

def update(request):
    updatedProduct = request.get_json()
    updatedProductData = {"$set": {"name": updatedProduct["name"], "description": updatedProduct["description"], "price": updatedProduct["price"]}}
    productCollection.update_one({ "_id": ObjectId(updatedProduct["id"]) }, updatedProductData)

    return json.dumps({"status": "OK"})
    
def delete(params):
    id = params.get("id")
    productCollection.delete_one({"_id": ObjectId(id)})
    
    return json.dumps({"status": "OK"})