from common import decompress
from common import match
from common import spide
from config import hdu_url
from config import hdu_table_pattern
from config import hdu_td_pattern
from config import hdu_ac_number_pattern
from config import hdu_username_pattern
from config import get_data_failed
from config import match_user_failed

def spide_for_hdu(username):
    url = hdu_url + username
    data = decompress(spide(url))
    if data is None:
        return get_data_failed
    data = data.decode('gb2312') 
    table_data = match(hdu_table_pattern, data)
    if table_data is None:
        return match_user_failed
    table_data = table_data[0]
    td_data = match(hdu_td_pattern, table_data)
    for i in range(2, len(td_data), 6):
        if td_data[i] == username:
            return td_data[i+3]
    return match_user_failed

if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        print('Input your hdu account please.')
    else:
        ac_number = spide_for_hdu(sys.argv[1], hdu_url+sys.argv[1])
        print(ac_number)
