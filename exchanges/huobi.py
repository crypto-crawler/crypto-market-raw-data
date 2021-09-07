import json
import logging
from typing import Any, Dict, List

from .utils import get_json


def fetch_markets(market_type: str) -> List[Dict[str, Any]]:
    '''Fetch all trading markets from a crypto exchage.'''
    if market_type == 'inverse_future':
        return _fetch_inverse_future_markets()
    elif market_type == 'inverse_swap':
        return _fetch_inverse_swap_markets()
    elif market_type == 'linear_swap':
        return _fetch_linear_swap_markets()
    elif market_type == 'spot':
        return _fetch_spot_markets()
    else:
        raise ValueError(f'Unknown market type: {market_type}')


def http_get(url: str) -> List[Dict[str, Any]]:
    resp = get_json(url)
    if resp['status'] != 'ok':
        logging.error(json.dumps(resp))
        return []
    return resp['data']


def _fetch_inverse_future_markets() -> List[Dict[str, Any]]:
    return http_get('https://api.hbdm.com/api/v1/contract_contract_info')


def _fetch_inverse_swap_markets() -> List[Dict[str, Any]]:
    return http_get('https://api.hbdm.com/swap-api/v1/swap_contract_info')


def _fetch_linear_swap_markets() -> List[Dict[str, Any]]:
    return http_get('https://api.hbdm.com/linear-swap-api/v1/swap_contract_info')


def _fetch_spot_markets() -> List[Dict[str, Any]]:
    symbols = http_get('https://api.huobi.pro/v1/common/symbols')
    symbols.sort(key=lambda x: x['symbol'])
    return symbols
