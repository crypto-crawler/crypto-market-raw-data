import logging
from typing import Any, Dict, List

from .utils import get_json


def fetch_markets(market_type: str) -> List[Dict[str, Any]]:
    '''Fetch all trading markets from a crypto exchage.'''
    if market_type == 'all':
        return _fetch_all_markets()
    else:
        raise ValueError(f'Unknown market type: {market_type}')


def _fetch_all_markets() -> List[Dict[str, Any]]:
    url = 'https://api.bybit.com/v2/public/symbols'
    resp: Dict[str, Any] = get_json(url)
    if resp['ret_code'] != 0:
        logging.error(f'resp.ret_code is {resp["ret_code"]}')
        return []
    result: List[Dict[str, Any]] = resp['result']
    result.sort(key=lambda x: x['name'])
    return result
