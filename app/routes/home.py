from flask import Blueprint
HomeRoutes = Blueprint('home', __name__)


@HomeRoutes.route('/', methods=['GET'])
def home():
    return 'API running'
