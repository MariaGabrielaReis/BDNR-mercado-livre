import json
import src.connectDatabase as connectDB

mongoDB = connectDB.connectToMongoDB()
userCollection = mongoDB.usuario

redis = connectDB.connectToRedis()

cassandra = connectDB.connectToCassandra()
  
def addWishlistToRedis(params):
  userCpf = params.get("userCpf")
  user = userCollection.find_one({ "cpf": userCpf })
  redis.set(f'wishlist:{userCpf}', user['wishlist'])

  return json.dumps({"status": "OK"})

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
 
def addWishlistToCassandra(params):
  userCpf = params.get("userCpf")
  redisWishlist = redis.get(f'wishlist:{userCpf}')

  cassandra.execute(f'INSERT INTO mercadolivre.wishlist (userCpf, products) VALUES ({userCpf}, {str(redisWishlist)})')

  return json.dumps({"status": "OK"})

def showCassandraWishlist(params):
  userCpf = params.get("userCpf")
  response = cassandra.execute(f'SELECT * FROM mercadolivre.wishlist WHERE userCpf = {userCpf}')
  
  if (not response):
    return json.dumps({"hasError": True, "Message": "Lista de desejos não encontrada!"})

  response = response[0]
  return json.dumps({
    "userCpf": response.userCpf,
    "products": json.dumps({response.products})
  })

def deleteWishlistFromCassandra(params):
  userCpf = params.get("userCpf")
  cassandra.execute(f'DELETE FROM mercadolivre.wishlist WHERE userCpf = {userCpf} IF EXISTS')

  return json.dumps({"status": "OK"}) 
