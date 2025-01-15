from flask import Blueprint
from app.controllers.ia_controller import text_correction,generate_qrcode,resume_text,translate_text,listen

ia_bp = Blueprint('ia_bp',__name__,url_prefix='/ia')

ia_bp.route('/correct',methods=['POST'])(text_correction)
ia_bp.route('/qr',methods=['POST'])(generate_qrcode)
ia_bp.route('/resume',methods=['POST'])(resume_text)
ia_bp.route('/translate',methods=['POST'])(translate_text)
ia_bp.route('/listen',methods=['POST'])(listen)
