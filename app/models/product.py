from app import db

class Product(db.Model):
    __tablename__ = 'products'

    id     = db.Column(db.Integer, primary_key=True)
    img    = db.Column(db.String(255))
    name   = db.Column(db.String(100), nullable=False)
    type   = db.Column(db.String(100), nullable=False)
    price  = db.Column(db.Integer)

    def __repr__(self):
        return f'<Product {self.name}>'