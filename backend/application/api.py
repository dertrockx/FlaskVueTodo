from flask import Blueprint, jsonify
from flask_restful import Api, Resource, reqparse, request
from application.models import List, Item, db

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)


class ListResource(Resource):
	def get(self):
		parser = reqparse.RequestParser()
		parser.add_argument('id')
		data = parser.parse_args()

		_id = data.get('id', None)
		if _id is not None:
			response = List.query.filter_by(id=_id).first()
			if response is None:
				response = {
					'message' : "Error! List cannot be found"
				}
			else:
				response = response.to_dict()
		else:
			response = [list.to_dict() for list in List.query.all()]
		return response

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('name', required=True, help='This filed is required')
		data = parser.parse_args()
		list = List()
		list.name = data.get('name')
		db.session.add(list)
		db.session.commit()
		return list.to_dict()

	def put(self):
		parser = reqparse.RequestParser()
		parser.add_argument('name', required=True)
		parser.add_argument('id', required=True)
		data = parser.parse_args()
		name = data.get('name', None)
		_id = data.get('id', None)
		if name is not None and _id is not None:
			list = List.query.filter_by(id=_id).first()
			list.name = name
			db.session.add(list)
			db.session.commit()
			return list.to_dict()
		return {
			'message': "You sent a blank data"
		}

	def delete(self):
		parser = reqparse.RequestParser()
		parser.add_argument('id', help="This field is required")
		data = parser.parse_args()
		args = request.args
		_id = data.get('id') or args.get('id')
		list = List.query.filter_by(id=_id).first()
		if list is not None:
			db.session.delete(list)
			db.session.commit()
			return {"message": "Succesfully deleted list!"}
		return {"message" : "List cannot be found"}

		
class ItemResource(Resource):
	def get(self):
		parser = reqparse.RequestParser()
		parser.add_argument('id')
		parser.add_argument('list_id')

		args = request.args

		data = parser.parse_args()
		print(data)
		_id = data.get('id') or args.get('id') or None
		list_id = data.get('list_id') or args.get('list_id') or None

		status_code = 200 # the status code to return

		if _id is None and list_id is None:
			response = [item.to_dict() for item in Item.query.all()]
		elif _id is not None:
			response = Item.query.filter_by(id=_id).first()
			if response is None:
				response = {
					"message" : "Error! Item cannot be found!"
				}
				# status_code = 404
			else:
				response = response.to_dict()
		elif list_id is not None:
			response = [item.to_dict() for item in Item.query.filter_by(list_id=list_id)]
			if len(response) == 0:
				response = {
					'message' : "Items cannot be found with list_id {}".format(list_id)
				}
				# status_code = 404
		return response, status_code


	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('title', required=True, help="This field is required")
		parser.add_argument('list_id', required=True, help="This field is required")
		data = parser.parse_args()
		title = data.get('title')
		list_id = data.get('list_id')

		item = Item(title=title, list_id=list_id)
		db.session.add(item)
		db.session.commit()
		return item.to_dict()

	def put(self):
		# Users can't change the list_id parameter
		parser = reqparse.RequestParser()
		parser.add_argument('id', required=True, help="This field is required")
		parser.add_argument('title', required=True, help="This field is required")
		data = parser.parse_args()
		_id = data.get('id')
		title = data.get('title')
		item = Item.query.filter_by(id=_id).first()
		if item is None:
			return {"message" : "Item cannot be found"}, 404
		item.title = title
		db.session.add(item)
		db.session.commit()
		return item.to_dict()

	def patch(self):
		# Users can't change the list_id parameter
		parser = reqparse.RequestParser()
		parser.add_argument('id', required=True, help="This field is required")
		parser.add_argument('title', required=True, help="This field is required")
		data = parser.parse_args()
		_id = data.get('id')
		title = data.get('title')
		item = Item.query.filter_by(id=_id).first()
		if item is None:
			return {"message" : "Item cannot be found"}, 404
		item.title = title
		db.session.add(item)
		db.session.commit()
		return item.to_dict()

	def delete(self):
		parser = reqparse.RequestParser()
		parser.add_argument('id', required=True, help="This field is required to delete an item")
		data = parser.parse_args()
		_id = data.get('id')
		item = Item.query.filter_by(id=_id).first()
		if item is None:
			return {
				"message" : "Error! Item cannot be found"
			}, 404



api.add_resource(ListResource, '/lists')
api.add_resource(ItemResource, '/items')