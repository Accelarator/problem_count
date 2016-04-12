from config import codeforces_url
from common import decompress
from common import match
from common import spide
from config import get_data_failed
from config import match_user_failed
import json

def spide_for_codeforces(username):
    url = codeforces_url.format(username)
    data = decompress(spide(url))
    if data is None:
        return get_data_failed
    json_data = json.loads(data.decode('utf-8'))
    ac_set = set()
    for key, value in json_data.items():
        if key != 'status':
            for submit in value:
                if submit['verdict'] == 'OK' and submit['problem']['name'] not in ac_set:
                    ac_set |= {submit['problem']['name']}
            break
    return len(ac_set)

if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        print('at least one account.')
    else:
        spide_for_codeforces(sys.argv[1])
