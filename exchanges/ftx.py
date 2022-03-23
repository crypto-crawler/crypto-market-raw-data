import json
import logging
from typing import Any, Dict, List

from .utils import get_json


def fetch_markets(market_type: str) -> List[Dict[str, Any]]:
    """Fetch all trading markets from a crypto exchage."""
    if market_type == "all":
        return _fetch_all_markets()
    else:
        raise ValueError(f"Unknown market type: {market_type}")


def _fetch_all_markets() -> List[Dict[str, Any]]:
    url = "https://ftx.com/api/markets"
    resp = get_json(url)
    if not resp["success"]:
        logging.error(json.dumps(resp))
        return []
    symbols = resp["result"]
    for symbol in symbols:
        del symbol["last"]
        del symbol["bid"]
        del symbol["ask"]
        del symbol["price"]
        del symbol["change1h"]
        del symbol["change24h"]
        del symbol["changeBod"]
        del symbol["quoteVolume24h"]
        del symbol["volumeUsd24h"]
    return symbols
