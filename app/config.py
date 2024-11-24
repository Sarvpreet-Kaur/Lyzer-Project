import os

class Config:
    LYZR_API_KEY = os.getenv("LYZR_API_KEY", "lyzr-0ek3jRBSPk6vx5Qoh4Br86jT")
    AUTOMATA_URL = "https://api.lyzr.com"
    DEFAULT_TAX_RATE = 0.15
    DEFAULT_INFLATION_RATE = 3  # Default inflation rate
