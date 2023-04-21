import math
import requests
import json
from datetime import datetime
import time


def get_date(wallet, t, proxy, headers):
    time.sleep(t)
    url_link_day = f"https://api.debank.com/user?id={wallet}"
    url_link_balance = f"https://api.debank.com/user/total_balance?addr={wallet}"
    res_day_wallet = requests.get(url_link_day, headers=headers, proxies=proxy)                                        
    res_balance_wallet = requests.get(url_link_balance, headers=headers, proxies=proxy)                                
    dictionary_day_wallet = json.loads(res_day_wallet.text)
    dictionary_balance_wallet = json.loads(res_balance_wallet.text)
    balance = dictionary_balance_wallet['data']['total_usd_value']                                                     
    date_create_wallet = math.floor((time.time() - dictionary_day_wallet['data']['user']['desc']['born_at']) / 86400)  
    return [datetime.now().strftime('%Y-%m-%d %H:%M:%S'), wallet, balance, date_create_wallet]
