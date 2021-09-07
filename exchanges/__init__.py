from typing import Any, Dict, List, Union

from .binance import fetch_markets as binance_fetch_markets
from .bitfinex import fetch_markets as bitfinex_fetch_markets
from .bitget import fetch_markets as bitget_fetch_markets
from .bithumb import fetch_markets as bithumb_fetch_markets
from .bitmex import fetch_markets as bitmex_fetch_markets
from .bitstamp import fetch_markets as bitstamp_fetch_markets
from .bitz import fetch_markets as bitz_fetch_markets


def fetch_markets(exchange: str, market_type: str) -> Union[Dict[str, Any], List[Any]]:
    '''Fetch all trading markets from a crypto exchage.'''
    if exchange == 'binance':
        return binance_fetch_markets(market_type)
    elif exchange == 'bitfinex':
        return bitfinex_fetch_markets(market_type)
    elif exchange == 'bitget':
        return bitget_fetch_markets(market_type)
    elif exchange == 'bithumb':
        return bithumb_fetch_markets(market_type)
    elif exchange == 'bitmex':
        return bitmex_fetch_markets(market_type)
    elif exchange == 'bitstamp':
        return bitstamp_fetch_markets(market_type)
    elif exchange == 'bitz':
        return bitz_fetch_markets(market_type)
    else:
        raise ValueError(f"Unknown exchange {exchange}")
