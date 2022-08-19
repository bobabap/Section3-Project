from flask import Blueprint

bp = Blueprint('user', __name__, url_prefix='/main')

@bp.route('/')
def index():
    return 'welcome to main index'