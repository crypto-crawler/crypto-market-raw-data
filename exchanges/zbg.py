import logging
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
    url = 'https://www.zbg.com/exchange/api/v1/common/symbols'
    resp = get_json(url)
    if resp['resMsg']['code'] != "1":
        logging.error(json.dumps(resp))
        return []
    return resp['datas']


def _fetch_swap_markets() -> List[Dict[str, Any]]:
    url = 'https://www.zbg.com/exchange/api/v1/future/common/contracts'
    resp = get_json(url)
    if resp['resMsg']['code'] != "1":
        logging.error(json.dumps(resp))
        return []
    return resp['datas']
