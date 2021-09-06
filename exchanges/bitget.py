from typing import Any, Dict, List

from .utils import get_json


def fetch_markets(market_type: str) -> List[Dict[str, Any]]:
    '''Fetch all trading markets from a crypto exchage.'''
    if market_type == 'spot':
        return _fetch_spot_markets()
    elif market_type == 'swap':
        return _fetch_swap_markets()
    else:
        raise ValueError(f'Unknown market type: {market_type}')


def _fetch_spot_markets() -> List[Dict[str, Any]]:
    url = 'https://api.bitget.com/data/v1/common/symbols'
    return get_json(url)['data']


def _fetch_swap_markets() -> List[Dict[str, Any]]:
    url = 'https://capi.bitget.com/api/swap/v3/market/contracts'
    return get_json(url)
