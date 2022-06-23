import src.connectDatabase as connectDB
import json

redis = connectDB.connectToRedis()
  
def addWishlistToRedis(params, request):
  userCpf = params.get("userCpf")
  wishlist = json.dumps(request.get_json())
  redis.set(f'wishlist:{userCpf}', wishlist)

  return json.dumps({"status": "ok"})

def showWishlist(params):
  userCpf = params.get("userCpf")  

  try:
    return json.loads(redis.get(f'wishlist:{userCpf}'))
  except:
    return json.dumps({"hasError": True, "Message": "Lista de desejos não encontrada!"})

def updateWishlist(params, request):
  userCpf = params.get("userCpf")
  wishlist = json.dumps(request.get_json())
  redis.set(f'wishlist:{userCpf}', wishlist)
 
  return json.dumps({"status": "ok"})
 