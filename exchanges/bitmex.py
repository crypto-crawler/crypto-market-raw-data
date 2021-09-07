from typing import Any, Dict, List

from .utils import get_json


def fetch_markets(market_type: str) -> List[Dict[str, Any]]:
    '''Fetch all trading markets from a crypto exchage.'''
    if market_type == 'all':
        return _fetch_all_markets()
    else:
        raise ValueError(f'Unknown market type: {market_type}')


def _fetch_all_markets() -> List[Dict[str, Any]]:
    url = 'https://www.bitmex.com/api/v1/instrument/active'
    symbols = get_json(url)
    for symbol in symbols:
        del symbol['closingTimestamp']
        del symbol['fairBasis']
        del symbol['fairBasisRate']
        del symbol['foreignNotional24h']
        del symbol['homeNotional24h']
        del symbol['indicativeFundingRate']
        del symbol['lastChangePcnt']
        del symbol['lastTickDirection']
        del symbol['openInterest']
        del symbol['openingTimestamp']
        del symbol['openValue']
        del symbol['prevTotalTurnover']
        del symbol['prevTotalVolume']
        del symbol['quoteToSettleMultiplier']
        del symbol['timestamp']
        del symbol['totalTurnover']
        del symbol['totalVolume']
        del symbol['turnover']
        del symbol['turnover24h']
        del symbol['volume']
        del symbol['volume24h']
        del symbol['vwap']
        for key in list(symbol.keys()):
            if symbol[key] == None:
                del symbol[key]
            elif 'Price' in key or 'price' in key:
                del symbol[key]
    return symbols
