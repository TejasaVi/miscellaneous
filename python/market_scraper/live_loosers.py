import requests
import pandas as pd
import json
import pprint 
expiry_date = '10-Feb-2022'
symbol = 'NIFTY'
url = 'https://www.nseindia.com/api/liveanalysis/loosers/allSec' 
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
           'accept-language': 'en-US,en;q=0.9',
           'accept-encoding': 'gzip, deflate, br',
           'referer':'https://www.nseindia.com/'}

def _do_request():
    session = requests.Session()
    request = session.get(url,headers=headers)
    cookies = dict(request.cookies)
    response = session.get(url, headers=headers, cookies=cookies).json()	
    rdata = json.dumps(response)
    json_data = json.loads(rdata)
    return json_data

data = _do_request()
pprint.pprint(data)
