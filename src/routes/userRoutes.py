from flask import Blueprint, request
from flask_cors import cross_origin

import src.controllers.userController as userController

user = Blueprint('user', __name__)

@user.route("/", methods=['GET'])
@cross_origin()
def index():
	return userController.index()

@user.route("/show", methods=['GET'])
@cross_origin()
def show():
	return userController.show(request.args)

@user.route("/create", methods=['POST'])
@cross_origin()
def create():
	return userController.create(request)

@user.route("/update", methods=['PUT'])
@cross_origin()
def update():
	return userController.update(request)

@user.route("/addToBag", methods=['PUT'])
@cross_origin()
def addToBag():
	return userController.addToBag(request.args, request)

@user.route("/addToWishlist", methods=['PUT'])
@cross_origin()
def addToWishlist():
	return userController.addToWishlist(request.args, request)

@user.route("/delete", methods=['DELETE'])
@cross_origin()
def delete():
	return userController.delete(request.args)


