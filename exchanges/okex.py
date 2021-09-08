from typing import Any, Dict, List

from .utils import get_json


def fetch_markets(market_type: str) -> List[Dict[str, Any]]:
    '''Fetch all trading markets from a crypto exchage.'''
    if market_type == 'future':
        return _fetch_future_markets()
    elif market_type == 'option':
        return _fetch_option_markets()
    elif market_type == 'spot':
        return _fetch_spot_markets()
    elif market_type == 'swap':
        return _fetch_swap_markets()
    else:
        raise ValueError(f'Unknown market type: {market_type}')


def _fetch_future_markets() -> List[Dict[str, Any]]:
    url = 'https://www.okex.com/api/futures/v3/instruments'
    return get_json(url)


def _fetch_spot_markets() -> List[Dict[str, Any]]:
    url = 'https://www.okex.com/api/spot/v3/instruments'
    symbols = get_json(url)
    symbols.sort(key=lambda x: x['instrument_id'])
    return symbols


def _fetch_swap_markets() -> List[Dict[str, Any]]:
    url = 'https://www.okex.com/api/swap/v3/instruments'
    return get_json(url)


def _fetch_option_markets_underlying(underlying: str) -> List[Dict[str, Any]]:
    url = f'https://www.okex.com/api/option/v3/instruments/{underlying}'
    return get_json(url)


def _fetch_option_markets() -> List[Dict[str, Any]]:
    underlying = ["BTC-USD", "ETH-USD", "EOS-USD"]
    lst: List[Dict[str, Any]] = []
    for underlying_symbol in underlying:
        lst.extend(_fetch_option_markets_underlying(underlying_symbol))
    return lst
