import json
import src.connectDatabase as connectDB

mongoDB = connectDB.connectToMongoDB()
userCollection = mongoDB.usuario

redis = connectDB.connectToRedis()
  
def addWishlistToRedis(params):
  userCpf = params.get("userCpf")
  user = userCollection.find_one({ "cpf": userCpf })
  redis.set(f'wishlist:{userCpf}', user['wishlist'])

  return json.dumps({"status": "ok"})

def showRedisWishlist(params):
  userCpf = params.get("userCpf")  

  try:
    return json.loads(redis.get(f'wishlist:{userCpf}'))
  except:
    return json.dumps({"hasError": True, "Message": "Lista de desejos não encontrada!"})
 
def deleteWishlistFromRedis(params):
  userCpf = params.get("userCpf")
  redis.delete(f'wishlist:{userCpf}')

  return json.dumps({"status": "OK"}) 