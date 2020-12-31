# import sqlite3
from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    items = db.relationship("ItemModel", lazy="dynamic")

    def __init__(self, name):
        self.name = name

    def json(self):
        return {"name": self.name, "items": [x.json() for x in self.items.all()]}

    @classmethod
    def findByName(cls, name):
        return cls.query.filter_by(
            name=name
        ).first()  # select * from items where name=name limit 1

    def saveToDb(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDb(self):
        db.session.delete(self)
        db.session.commit()
