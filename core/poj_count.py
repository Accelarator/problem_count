from config import poj_url
from config import match_user_failed
from config import poj_td_pattern
from config import get_data_failed
from config import poj_username_pattern
from config import poj_table_pattern
from common import match
from common import decompress
from common import spide

def spide_for_poj(username, url):
    if len(username) <= 1:
        return match_user_failed
    data = decompress(spide(url.format(username)))
    if data is None:
        return get_data_failed
    data = data.decode('utf-8')
    table_data = match(poj_table_pattern, data)
    if table_data is None:
        return match_user_failed
    td_data = match(poj_td_pattern, table_data[0]) 
    for i in range(0, len(td_data), 6):
        cur_username = match(poj_username_pattern, td_data[i])[0]
        if cur_username.lower() != username.lower():
            continue
        return td_data[i+4]
    return match_user_failed
if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        print("Input your poj account please.")
    else:
        ac_number = spide_for_poj(sys.argv[1], poj_url)
        print(ac_number)
