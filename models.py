from config import db, ma

class Item(db.Model):
    __tablename__ = "item"
    id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String(32), unique=True)
    quantity = db.Column(db.Integer(32))


class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Item
        load_instance = True
        sqla_session = db.session

item_schema = ItemSchema()
inventory_schema = ItemSchema(many=True)