from typing import List

from .utils import get_json


def fetch_markets(market_type: str) -> List[str]:
    '''Fetch all trading markets from a crypto exchage.'''
    if market_type == 'spot':
        return _fetch_spot_markets()
    elif market_type == 'swap':
        return _fetch_swap_markets()
    else:
        raise ValueError(f'Unknown market type: {market_type}')


def _fetch_spot_markets() -> List[str]:
    return get_json('https://api-pub.bitfinex.com/v2/conf/pub:list:pair:exchange')[0]


def _fetch_swap_markets() -> List[str]:
    return get_json('https://api-pub.bitfinex.com/v2/conf/pub:list:pair:futures')[0]
