from flask import Blueprint, request
from flask_cors import cross_origin

import src.controllers.wishlistController as wishlistController

wishlist = Blueprint('wishlist', __name__)



@voucher.route("/create", methods=['POST'])
@cross_origin()
def create():
	return wishlistController.create(request)

@voucher.route("/update", methods=['PUT'])
@cross_origin()
def update():
	return wishlistController.update(request)

@voucher.route("/delete", methods=['DELETE'])
@cross_origin()
def delete():
	return wishlistController.delete(request.args)