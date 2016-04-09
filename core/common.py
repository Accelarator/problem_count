from urllib import request
from config import TIME 
from config import headers
import gzip
import config
import re

def spide(url):
    try:
        Req = request.Request(url=url, headers=headers)
        Res = request.urlopen(url, timeout=TIME)
        data = Res.read()
    except Exception:
        return None
    else:
        return data

def decompress(data):
    if data is None:
        return None
    try:
        data = gzip.decompress(data)
    finally:
        return data
        
def match(pattern, data):
    reg_exp = re.compile(pattern)
    return reg_exp.findall(data)
