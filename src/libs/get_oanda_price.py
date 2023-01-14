import json
import os
from pathlib import Path
from typing import Dict

import requests
from attrdict import AttrDict
from dotenv import load_dotenv

dotenv_path = Path('D:\Code\PycharmProjects\optix\.env')
load_dotenv(dotenv_path=dotenv_path)

API_KEY: str = os.getenv('OANDA_API_KEY')


def get_oanda_price(instrument: str) -> float:
    """
    Get current price from Oanda API
    instrument: currency pair, eg. 'EUR_USD'
    """
    url: str = f'https://api-fxpractice.oanda.com/v3/instruments/{instrument}/candles'
    headers: Dict[str, str] = {"Authorization": f"Bearer {API_KEY}"}
    r: requests.Response = requests.get(url, headers=headers)

    data: AttrDict = AttrDict(json.loads(r.text))

    return float(data.candles[0].mid.c)
