from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db          = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'mysql+pymysql://root:@localhost/flask_products'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'click2drive_secret_key'

    db.init_app(app)
    migrate.init_app(app, db)

    # Import ALL models so Flask-Migrate can detect them
    from app.models.product import Product

    from app.controllers.product import product_bp
    app.register_blueprint(product_bp)

    return app