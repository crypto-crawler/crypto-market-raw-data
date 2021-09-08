import logging
from typing import Any, Dict, List

from .utils import get_json


def _clean_fields(symbols: List[Dict[str, Any]]) -> None:
    for symbol in symbols:
        symbol.pop('fundingFeeRate', None)
        symbol.pop('highPrice', None)
        symbol.pop('indexPrice', None)
        symbol.pop('lastTradePrice', None)
        symbol.pop('lowPrice', None)
        symbol.pop('markPrice', None)
        symbol.pop('nextFundingRateTime', None)
        symbol.pop('openInterest', None)
        symbol.pop('predictedFundingFeeRate', None)
        symbol.pop('priceChg', None)
        symbol.pop('priceChgPct', None)
        symbol.pop('turnoverOf24h', None)
        symbol.pop('volumeOf24h', None)


def fetch_markets(market_type: str) -> List[Dict[str, Any]]:
    '''Fetch all trading markets from a crypto exchage.'''
    if market_type == 'spot':
        return _fetch_spot_markets()
    elif market_type == 'contract':
        return _fetch_contract_markets()
    else:
        raise ValueError(f'Unknown market type: {market_type}')


def _fetch_spot_markets() -> List[Dict[str, Any]]:
    url = 'https://api.kucoin.com/api/v1/symbols'
    resp = get_json(url)
    if resp['code'] != "200000":
        logging.error(json.dumps(resp))
        return []
    return resp['data']


def _fetch_contract_markets() -> List[Dict[str, Any]]:
    url = 'https://api-futures.kucoin.com/api/v1/contracts/active'
    resp = get_json(url)
    if resp['code'] != "200000":
        logging.error(json.dumps(resp))
        return []
    symbols = resp['data']
    _clean_fields(symbols)
    return symbols
