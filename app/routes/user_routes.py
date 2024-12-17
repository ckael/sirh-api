# app/routes/user_routes.py
from flask import Blueprint
from app.controllers.user_controller import getAll, addUser

user_bp = Blueprint('user_bp', __name__,url_prefix='/user')

user_bp.route('/all', methods=['GET'])(getAll)
user_bp.route('/add', methods=['POST'])(addUser)
