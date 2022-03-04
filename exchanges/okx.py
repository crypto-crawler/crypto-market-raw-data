from typing import Any, Dict, List

from .utils import get_json


def _fetch_option_underlying() -> List[str]:
    obj = get_json('https://www.okx.com/api/v5/public/underlying?instType=OPTION')
    if obj['code'] != '0':
        return []
    else:
        return obj['data'][0]

def fetch_markets(inst_type: str) -> List[Dict[str, Any]]:
    '''Fetch a list of instruments from OKX.

    see https://www.okx.com/docs-v5/en/#rest-api-public-data-get-instruments
    '''
    if inst_type == 'OPTION':
        lst: List[Dict[str, Any]] = []
        underlyings = _fetch_option_underlying()
        for uly in underlyings:
            obj = get_json(f'https://www.okx.com/api/v5/public/instruments?instType=OPTION&uly={uly}')
            if obj['code'] == '0':
                lst.extend(obj['data'])
        return lst
    else:
        obj = get_json(f'https://www.okx.com/api/v5/public/instruments?instType={inst_type}')
        if obj['code'] != '0':
            return []
        else:
            return obj['data']
