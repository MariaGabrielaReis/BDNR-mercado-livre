from pymongo import MongoClient
import redis
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def connectToMongoDB():
  db = MongoClient('mongodb+srv://<user>:<password>@fa-starting-no-sql.6vnsq.mongodb.net/')

  return db['mercado-livre']

def connectToRedis():
  db = redis.Redis(host='<host>', port="<port-number>", password='<password>')

  return db

def connectToCassandra():
  auth_provider = PlainTextAuthProvider('<user>', '<password>')
  cluster = Cluster(auth_provider=auth_provider)
  db = cluster.connect()

  return db
