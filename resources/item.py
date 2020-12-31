# import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):

    p = reqparse.RequestParser()
    p.add_argument("price", type=float, required=True, help="Need a price")

    p.add_argument("store_id", type=int, required=True, help="Need a store_id")

    @jwt_required()
    def get(self, name):
        item = ItemModel.findByName(name)
        if item:
            return item.json()
        return {"message": "Item not found"}, 404

    def post(self, name):
        if ItemModel.findByName(name):
            return {
                "message": "Item with the same name '{}' already exsits".format(name)
            }, 400

        d = Item.p.parse_args()
        item = ItemModel(name, **d)
        try:
            item.saveToDb()
        except:
            return {"message": "Failed to insert the item"}, 500

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.findByName(name)
        if item:
            item.deleteFromDb()
        return {"message": "Item deleted"}

    def put(self, name):

        d = Item.p.parse_args()
        item = ItemModel.findByName(name)

        if item is None:
            item = ItemModel(name, **d)
        else:
            item.price = d["price"]
            item.store_id = d["store_id"]
        item.saveToDb()
        return item.json()


class ItemList(Resource):
    def get(self):
        return {"items": [x.json() for x in ItemModel.query.all()]}
