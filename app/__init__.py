from flask import Flask

app = Flask(__name__)
if app.config['ENV'] == 'production':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

from app.routes.sunat import SunatRoutes
from app.routes.home import HomeRoutes

app.register_blueprint(HomeRoutes, url_prefix='/')
app.register_blueprint(SunatRoutes, url_prefix='/sunat')
