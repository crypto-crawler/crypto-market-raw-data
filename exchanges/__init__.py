from typing import Any, Dict, List

from .binance import fetch_markets as binance_fetch_markets
from .bitfinex import fetch_markets as bitfinex_fetch_markets
from .bitget import fetch_markets as bitget_fetch_markets


def fetch_markets(exchange: str, market_type: str) -> List[Dict[str, Any]]:
    '''Fetch all trading markets from a crypto exchage.'''
    if exchange == 'binance':
        return binance_fetch_markets(market_type)
    if exchange == 'bitfinex':
        return bitfinex_fetch_markets(market_type)
    elif exchange == 'bitget':
        return bitget_fetch_markets(market_type)
    else:
        raise ValueError(f"Unknown exchange {exchange}")
