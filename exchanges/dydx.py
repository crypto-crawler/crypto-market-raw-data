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
    url = "https://api.dydx.exchange/v3/markets"
    resp = get_json(url)
    markets = resp["markets"]
    markets = sorted(list(markets.values()), key=lambda x: x["market"])
    for market in markets:
        del market["indexPrice"]
        del market["oraclePrice"]
        del market["priceChange24H"]
        del market["volume24H"]
        del market["trades24H"]
        del market["openInterest"]
        del market["nextFundingRate"]
    return markets
