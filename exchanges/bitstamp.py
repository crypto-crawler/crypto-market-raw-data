from typing import Any, Dict, List

from .utils import get_json


def fetch_markets(market_type: str) -> List[Dict[str, Any]]:
    """Fetch all trading markets from a crypto exchage."""
    if market_type == "spot":
        return _fetch_spot_markets()
    else:
        raise ValueError(f"Unknown market type: {market_type}")


def _fetch_spot_markets() -> List[Dict[str, Any]]:
    url = "https://www.bitstamp.net/api/v2/trading-pairs-info/"
    return get_json(url)
