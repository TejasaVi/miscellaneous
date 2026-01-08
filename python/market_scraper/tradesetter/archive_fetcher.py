import urllib.parse
import json
import wget

original_url = "https://www.nseindia.com/api/reports?archives=%5B%7B%22name%22%3A%22F%26O%20-%20FII%20Derivatives%20Statistics%22%2C%22type%22%3A%22archives%22%2C%22category%22%3A%22derivatives%22%2C%22section%22%3A%22equity%22%7D%5D&date=19-Apr-2024&type=equity&mode=single"
json_obj = [{"name":"F&O - FII Derivatives Statistics","type":"archives","category":"derivatives","section":"equity"}]

def santize_json(json_obj):
    json_str = json.dumps(json_obj)
    json_str = json_str.replace(" ", "%20")
    utf8_bytes = json.dumps(json_obj).encode('utf-8')
    utf8_bytes = utf8_bytes.replace(b': ', b':')  # Remove spaces after :
    utf8_bytes = utf8_bytes.replace(b', ', b',')  # Remove spaces after ,
    url_encoded_bytes = urllib.parse.quote(utf8_bytes)
    return url_encoded_bytes


bas_url = "https://www.nseindia.com/api/reports?archives="
tail_url = "&date={}&type=equity&mode=single".format("21-Jun-2024")
url = bas_url + santize_json(json_obj) +tail_url

if  original_url == url:
    print("Matched")
import pdb;pdb.set_trace()
