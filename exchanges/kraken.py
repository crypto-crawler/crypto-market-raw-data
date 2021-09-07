import logging
from typing import Any, Dict, List

from .utils import get_json


def fetch_markets(market_type: str) -> List[Dict[str, Any]]:
    '''Fetch all trading markets from a crypto exchage.'''
    if market_type == 'spot':
        return _fetch_spot_markets()
    else:
        raise ValueError(f'Unknown market type: {market_type}')


def _fetch_spot_markets() -> List[Dict[str, Any]]:
    url = 'https://api.kraken.com/0/public/AssetPairs'
    resp = get_json(url)
    if resp.get('error', None):
        logging.error(json.dumps(resp))
        return []
    symbols = list(resp['result'].values())
    symbols.sort(key=lambda x: x['altname'])
    return symbols
