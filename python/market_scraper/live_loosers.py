"""Python script to get live loosers on NSE."""
import json
import pprint
import requests

URL = 'https://www.nseindia.com/api/liveanalysis/loosers/allSec'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
           'accept-language': 'en-US,en;q=0.9',
           'accept-encoding': 'gzip, deflate, br',
           'referer': 'https://www.nseindia.com/'}


def _do_request():
    session = requests.Session()
    request = session.get(URL, headers=HEADERS)
    cookies = dict(request.cookies)
    response = session.get(URL, headers=HEADERS, cookies=cookies).json()
    rdata = json.dumps(response)
    json_data = json.loads(rdata)
    return json_data


data = _do_request()
pprint.pprint(data)
