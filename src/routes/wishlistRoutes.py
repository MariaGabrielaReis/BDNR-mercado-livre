from flask import Blueprint, request
from flask_cors import cross_origin

import src.controllers.wishlistController as wishlistController

wishlist = Blueprint('wishlist', __name__)

@wishlist.route("/addWishlistToRedis", methods=['POST'])
@cross_origin()
def addWishlistToRedis():
	return wishlistController.addWishlistToRedis(request.args, request)

@wishlist.route("/showWishlist", methods=['PUT'])
@cross_origin()
def showWishlist():
	return wishlistController.showWishlist(request.args)

@wishlist.route("/updateWishlist", methods=['PUT'])
@cross_origin()
def updateWishlist():
	return wishlistController.updateWishlist(request.args, request)