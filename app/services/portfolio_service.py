from app.services.lyzr_service import get_market_data
from app.config import Config

def generate_portfolio(risk_profile, financial_goals, timeline):
    market_data = get_market_data()

    # Check if market data is available
    if not market_data:
        return {"error": "Market data unavailable"}

    # Define portfolio allocation based on risk tolerance
    if risk_profile == "conservative":
        allocation = {"stocks": 20, "bonds": 60, "cash": 20}
    elif risk_profile == "moderate":
        allocation = {"stocks": 50, "bonds": 40, "cash": 10}
    else:
        allocation = {"stocks": 70, "bonds": 20, "cash": 10}

    # Calculate expected return adjusted for tax and inflation
    expected_return = sum([
        (allocation[asset] / 100) * market_data.get(asset, 0) * (1 - Config.DEFAULT_TAX_RATE)
        for asset in allocation
    ]) - Config.DEFAULT_INFLATION_RATE

    return {
        "allocation": allocation,
        "expected_return": max(0, round(expected_return, 2)),
        "message": f"Portfolio optimized for {financial_goals} over a {timeline} timeline."
    }
