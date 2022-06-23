from flask import Blueprint, request
from flask_cors import cross_origin

import src.controllers.buyController as buyController

buy = Blueprint('buy', __name__)

@buy.route("/show", methods=['GET'])
@cross_origin()
def show():
	return buyController.show(request.args)

@buy.route("/create", methods=['POST'])
@cross_origin()
def create():
	return buyController.create(request)

