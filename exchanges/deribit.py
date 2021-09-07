import logging
from typing import Any, Dict, List

from .utils import get_json


def fetch_markets(market_type: str) -> List[Dict[str, Any]]:
    '''Fetch all trading markets from a crypto exchage.'''
    if market_type == 'future':
        return _fetch_raw_markets('BTC', market_type) + _fetch_raw_markets('ETH', market_type)
    elif market_type == 'option':
        return _fetch_raw_markets('BTC', market_type) + _fetch_raw_markets('ETH', market_type)
    else:
        raise ValueError(f'Unknown market type: {market_type}')


def _fetch_raw_markets(currency: str, kind: str) -> List[Dict[str, Any]]:
    url = f'https://www.deribit.com/api/v2/public/get_instruments?currency={currency}&kind={kind}'
    resp = get_json(url)
    if 'error' in resp:
        logging.error(f'resp.error is {resp["error"]}')
        return []
    return resp['result']
