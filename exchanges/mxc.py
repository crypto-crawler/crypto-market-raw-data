import logging
from typing import Any, Dict, List

from .utils import get_json


def fetch_markets(market_type: str) -> List[Dict[str, Any]]:
    """Fetch all trading markets from a crypto exchage."""
    if market_type == "spot":
        return _fetch_spot_markets()
    elif market_type == "swap":
        return _fetch_swap_markets()
    else:
        raise ValueError(f"Unknown market type: {market_type}")


def _fetch_spot_markets() -> List[Dict[str, Any]]:
    url = "https://www.mexc.com/open/api/v2/market/symbols"
    resp = get_json(url)
    if resp["code"] != 200:
        logging.error(json.dumps(resp))
        return []
    symbols = resp["data"]
    symbols.sort(key=lambda x: x["symbol"])
    return symbols


def _fetch_swap_markets() -> List[Dict[str, Any]]:
    url = "https://contract.mexc.com/api/v1/contract/detail"
    resp = get_json(url)
    if not resp["success"]:
        logging.error(json.dumps(resp))
        return []
    symbols = resp["data"]
    symbols.sort(key=lambda x: x["symbol"])
    return symbols
