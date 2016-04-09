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

def spide_for_hdu(username, url):
    data = decompress(spide(url))
    if data is None:
        return get_data_failed
    data = data.decode('gb2312') 
    table_data = match(hdu_table_pattern, data)
    if table_data is None:
        return match_user_failed
    td_data = match(hdu_td_pattern, table_data)
    if username.lower() != td_data[2].lower():
        return match_user_failed 
    return td_data[5]

if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        print('Input your hdu account please.')
    else:
        spide_for_hdu(sys.argv[1], hdu_url+sys.argv[1])
