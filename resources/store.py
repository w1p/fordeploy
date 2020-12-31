from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        print("Store:Get entered")
        store = StoreModel.findByName(name)
        if store:
            return store.json()
        else:
            return {"message": "store not found"}, 404

    def post(self, name):
        if StoreModel.findByName(name):
            return {
                "message": "Store with the same name '{}' already exsits".format(name)
            }, 400

        store = StoreModel(name)
        try:
            store.saveToDb()
        except:
            return {"message": "Failed to create a new store"}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.findByName(name)
        if store:
            store.deleteFromDb()
        return {"message": "Store destroyed"}


class StoreList(Resource):
    def get(self):
        print("StoreList:get entered")
        return {"store": [x.json() for x in StoreModel.query.all()]}
