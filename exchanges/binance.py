from typing import Any, Dict, List

from .utils import get_json

SPOT_URL = 'https://api.binance.com/api/v3/exchangeInfo'
INVERSE_URL = 'https://dapi.binance.com/dapi/v1/exchangeInfo'
LINEAR_URL = 'https://fapi.binance.com/fapi/v1/exchangeInfo'
OPTION_URL = 'https://voptions.binance.com/options-api/v1/public/exchange/symbols'


def fetch_markets(market_type: str) -> List[Dict[str, Any]]:
    '''Fetch all trading markets from a crypto exchage.'''
    if market_type == 'spot':
        return _fetch_raw_markets(url=SPOT_URL)
    elif market_type == 'inverse':
        return _fetch_raw_markets(url=INVERSE_URL)
    elif market_type == 'linear':
        return _fetch_raw_markets(url=LINEAR_URL)
    elif market_type == 'option':
        return _fetch_raw_markets(url=OPTION_URL)
    else:
        raise ValueError(f'Unknown market type: {market_type}')


def _fetch_raw_markets(url: str) -> List[Dict[str, Any]]:
    json_obj = get_json(url)
    symbols = json_obj['symbols'] if 'symbols' in json_obj else json_obj['data']['optionSymbols']
    for symbol in symbols:
        for filter in symbol['filters']:
            if filter['filterType'] == 'PRICE_FILTER':
                del filter['minPrice']
                del filter['maxPrice']
    return symbols
