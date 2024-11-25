import requests
from app.config import Config

def get_market_data():
    try:
        response = requests.get(
            f"{Config.AUTOMATA_URL}/market-data",
            headers={"Authorization": f"Bearer {Config.LYZR_API_KEY}"}
        )
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch market data: {response.status_code}")
            return {}
    except Exception as e:
        print(f"Error connecting to Lyzr: {e}")
        return {}
