import logging
from typing import Any, Dict, List, Union

import requests

logging.basicConfig(level=logging.INFO)


def get_json(url: str) -> Union[Dict[str, Any], List[Any]]:
    resp = requests.get(
        url=url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        },
    )
    if resp.status_code != 200:
        logging.error(f"resp.status_code is {resp.status_code}")
        return []
    else:
        # print(resp.text)
        return resp.json()
