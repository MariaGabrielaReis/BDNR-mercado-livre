import simplejson as json
import src.connectDatabase as connectDB

mongoDB = connectDB.connectToMongoDB()
userCollection = mongoDB.usuario

def index():
    response = []
    for x in userCollection.find().sort("name"):
        response.append({"name": x['name'], "email": x['email']})
    
    return json.dumps(response)

def show(params):
    cpf = params.get("cpf")
    user = userCollection.find_one({ "cpf": cpf })

    return json.dumps(user, default=str)    

def create(request):
    user = request.get_json()
    userCollection.insert_one(user)

    return json.dumps({"status": "OK"})

def update(request):
    updatedUser = request.get_json()
    updatedUserData = {"$set": {"name": updatedUser["name"], "email": updatedUser["email"], "address": updatedUser["address"]}}
    userCollection.update_one({ "cpf": updatedUser["cpf"] }, updatedUserData)

    return json.dumps({"status": "OK"})
    
def addToBag(params, request):
    userCpf = params.get("cpf")
    product = request.get_json()
    user = userCollection.find_one({ "cpf": userCpf })

    allProducts = user["bag"]
    allProducts.append(product)

    user = {"$set": {"bag": allProducts}}
    userCollection.update_one({ "cpf": userCpf }, user)

    return json.dumps({"status": "OK"})

def delete(params):
    cpf = params.get("cpf")
    userCollection.delete_one({"cpf": cpf})
    
    return json.dumps({"status": "OK"})