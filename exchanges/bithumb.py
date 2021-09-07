import logging
from typing import Any, Dict, List

from .utils import get_json

logging.basicConfig(level=logging.INFO)


def fetch_markets(market_type: str) -> List[Dict[str, Any]]:
    '''Fetch all trading markets from a crypto exchage.'''
    if market_type == 'spot':
        return _fetch_spot_markets()
    else:
        raise ValueError(f'Unknown market type: {market_type}')


def _fetch_spot_markets() -> Dict[str, Any]:
    url = 'https://global-openapi.bithumb.pro/openapi/v1/spot/config'
    resp: Dict[str, Any] = get_json(url)
    if resp['code'] != "0":
        logging.error(f"code : {resp['code']}, msg: {resp['msg']}")
        return {}
    return resp['data']
