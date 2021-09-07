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
    url = 'https://apiv2.bitz.com/V2/Market/symbolList'
    resp = get_json(url)
    if resp['status'] != 200:
        logging.error(f'resp.status is {resp["status"]}')
        return []
    else:
        return list(resp['data'].values())


def _fetch_swap_markets() -> List[Dict[str, Any]]:
    url = 'https://apiv2.bitz.com/V2/Market/getContractCoin'
    resp = get_json(url)
    if resp['status'] != 200:
        logging.error(f'resp.status is {resp["status"]}')
        return []
    else:
        return resp['data']
