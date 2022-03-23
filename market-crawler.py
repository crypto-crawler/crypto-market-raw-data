import json
import logging
import os
from datetime import datetime
from typing import Dict, List

from exchanges import fetch_markets

logging.basicConfig(level=logging.INFO)

EXCHANGE_MARKET_TYPES: Dict[str, List[str]] = {
    "binance": ["inverse", "linear", "option", "spot"],
    "bitfinex": ["spot", "swap"],
    "bitget": ["spot", "swap"],
    "bithumb": ["spot"],
    "bitmex": ["all"],
    "bitstamp": ["spot"],
    # "bitz": ["spot", "swap"],
    "bybit": ["all"],
    "coinbase_pro": ["spot"],
    "deribit": ["future", "option"],
    "dydx": ["all"],
    "ftx": ["all"],
    "gate": ["inverse_future", "inverse_swap", "linear_future", "linear_swap", "spot"],
    "huobi": ["inverse_future", "inverse_swap", "linear_swap", "spot"],
    "kraken": ["spot", "futures"],
    "kucoin": ["contract", "spot"],
    "mxc": ["spot", "swap"],
    "okx": ["SPOT", "MARGIN", "SWAP", "FUTURES", "OPTION"],
    "zbg": ["spot", "swap"],
}

if __name__ == "__main__":
    exchange_market_type_pair_map: Dict[str, Dict[str, Dict[str, float]]] = {}
    for exchange in EXCHANGE_MARKET_TYPES:
        for market_type in sorted(EXCHANGE_MARKET_TYPES[exchange]):
            logging.info(f"{exchange} {market_type}")
            try:
                json_obj = fetch_markets(exchange, market_type)
                json_text = json.dumps(json_obj, indent=4, sort_keys=True) + "\n"
                today = datetime.utcnow().isoformat()[:10]
                latest_file = f"./data/{exchange}.{market_type}.json"
                daily_file = f"./data/{exchange}.{market_type}.{today}.json"

                if os.path.exists(latest_file):
                    with open(latest_file, mode="rt") as f_in:
                        json_text_old = f_in.read()
                else:
                    json_text_old = ""
                if json_text != json_text_old:
                    with open(daily_file, mode="wt") as f_out:
                        f_out.write(json_text)
                    os.chdir("./data")
                    if json_text_old:
                        os.unlink(os.path.basename(latest_file))
                    os.symlink(
                        os.path.basename(daily_file), os.path.basename(latest_file)
                    )
                    os.chdir("..")
            except Exception as e:
                logging.exception(f"{exchange} {market_type} fetch_markets failed")
