from flask import Blueprint
from app.controllers.auth_controller import recognize

auth_bp = Blueprint('auth_bp',__name__,url_prefix='/auth')

auth_bp.route('/face',methods=['POST'])(recognize)