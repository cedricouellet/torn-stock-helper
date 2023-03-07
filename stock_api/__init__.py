from flask import Flask
from stock_lib.database import load_db, db


def register_session(app: Flask): 
    load_db()

    @app.teardown_appcontext
    def remove_session(*args, **kwargs):
        db.remove()

def register_blueprints(app: Flask):
    from stock_api.home import home
    app.register_blueprint(home, url_prefix='/api')
    
    from stock_api.stocks import stocks
    app.register_blueprint(stocks, url_prefix='/api/stocks')

    from stock_api.snapshots import snapshots
    app.register_blueprint(snapshots, url_prefix='/api/snapshots')

    from stock_api.predictions import predictions
    app.register_blueprint(predictions, url_prefix='/api/predictions')


def create_app():
    app = Flask(__name__)

    with app.app_context():
        register_session(app)        
        register_blueprints(app)
        return app

        