from flask import Blueprint, request, jsonify
from app.services.portfolio_service import generate_portfolio

bp = Blueprint('portfolio', __name__, url_prefix='/portfolio')

@bp.route('/', methods=['POST'])
def portfolio():
    data = request.json

    # Inputs from the client
    risk_profile = data.get('risk_tolerance', 'moderate')
    financial_goals = data.get('financial_goals', 'retirement')
    timeline = data.get('timeline', 'long-term')

    # Generate the portfolio
    response = generate_portfolio(risk_profile, financial_goals, timeline)
    return jsonify(response)
