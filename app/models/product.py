from app import db

class Product(db.Model):
    __tablename__ = 'products'

    id     = db.Column(db.Integer, primary_key=True)
    name   = db.Column(db.String(100), nullable=False)
    type   = db.Column(db.String(100), nullable=False)
    price  = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'