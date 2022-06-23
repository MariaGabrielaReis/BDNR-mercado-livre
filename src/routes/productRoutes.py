from flask import Blueprint, request
from flask_cors import cross_origin

import src.controllers.productController as productController

product = Blueprint('product', __name__)

@product.route("/", methods=['GET'])
@cross_origin()
def index():
	return productController.index()

@product.route("/show", methods=['GET'])
@cross_origin()
def show():
	return productController.show(request.args)

@product.route("/create", methods=['POST'])
@cross_origin()
def create():
	return productController.create(request)

@product.route("/update", methods=['PUT'])
@cross_origin()
def update():
	return productController.update(request)

@product.route("/delete", methods=['DELETE'])
@cross_origin()
def delete():
	return productController.delete(request.args)


