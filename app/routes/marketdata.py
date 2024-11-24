from flask import Blueprint, jsonify
from app.services.lyzr_service import get_market_data

bp = Blueprint('marketdata', __name__, url_prefix='/marketdata')

@bp.route('/', methods=['GET'])
def marketdata():
    response = get_market_data()
    return jsonify(response)
