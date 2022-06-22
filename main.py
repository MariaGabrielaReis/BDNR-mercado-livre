from flask import Flask, jsonify
from flask_cors import CORS

from src.routes.buyRoutes import buy
from src.routes.productRoutes import product
from src.routes.userRoutes import user

from src.routes.mercalivreCassandra import cassandra

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(buy, url_prefix='/buy')
app.register_blueprint(product, url_prefix='/product')
app.register_blueprint(user, url_prefix='/user')

app.register_blueprint(cassandra, url_prefix='/cassandra')

@app.route('/')
def test():
  jsonTest = {"status": "API Online"}
  return jsonify(jsonTest)

if __name__ == '__main__':
	app.run(debug=True)