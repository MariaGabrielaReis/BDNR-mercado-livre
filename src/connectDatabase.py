from pymongo import MongoClient
import redis
from astrapy.client import create_astra_client

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

# get Astra connection information from environment variables
ASTRA_DB_ID = ''
ASTRA_DB_REGION = ''
ASTRA_DB_APPLICATION_TOKEN = ''

def connectToCassandra():
  # setup an Astra Client and create a shortcut to our test colllection
  astra_client = create_astra_client(
    astra_database_id=ASTRA_DB_ID,
    astra_database_region=ASTRA_DB_REGION,
    astra_application_token=ASTRA_DB_APPLICATION_TOKEN
  )

  return astra_client.rest
