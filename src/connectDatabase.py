from pymongo import MongoClient
import redis

def connectToMongoDB():
  db = MongoClient("mongodb+srv://<user>:<password>@fa-starting-no-sql.6vnsq.mongodb.net/")
  return db['mercado-livre']

def connectToRedis():
  db = redis.Redis(
    host='<host>',
    port="<port-number>",
    password='<password>'
  )

  return db
