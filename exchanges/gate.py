from typing import Any, Dict, List

from .utils import get_json


def fetch_markets(market_type: str) -> List[Dict[str, Any]]:
    '''Fetch all trading markets from a crypto exchage.'''
    if market_type == 'inverse_future':
        return _fetch_future_markets('btc')
    elif market_type == 'inverse_swap':
        return _fetch_swap_markets('btc')
    elif market_type == 'linear_future':
        return _fetch_future_markets('usdt')
    elif market_type == 'linear_swap':
        return _fetch_swap_markets('usdt')
    elif market_type == 'spot':
        return _fetch_spot_markets()
    else:
        raise ValueError(f'Unknown market type: {market_type}')


def _clean_fields(symbols: List[Dict[str, Any]]) -> None:
    for symbol in symbols:
        symbol.pop('basis_rate', None)
        symbol.pop('basis_value', None)
        symbol.pop('funding_next_apply', None)
        symbol.pop('funding_rate', None)
        symbol.pop('funding_rate_indicative', None)
        symbol.pop('index_price', None)
        symbol.pop('last_price', None)
        symbol.pop('long_users', None)
        symbol.pop('mark_price', None)
        symbol.pop('orderbook_id', None)
        symbol.pop('position_size', None)
        symbol.pop('short_users', None)
        symbol.pop('trade_id', None)
        symbol.pop('trade_size', None)


def _fetch_future_markets(currency: str) -> List[Dict[str, Any]]:
    url = f'https://api.gateio.ws/api/v4/delivery/{currency}/contracts'
    symbols = get_json(url)
    _clean_fields(symbols)
    return symbols


def _fetch_swap_markets(currency: str) -> List[Dict[str, Any]]:
    url = f'https://api.gateio.ws/api/v4/futures/{currency}/contracts'
    symbols = get_json(url)
    _clean_fields(symbols)
    return symbols


def _fetch_spot_markets() -> List[Dict[str, Any]]:
    url = 'https://api.gateio.ws/api/v4/spot/currency_pairs'
    return get_json(url)
