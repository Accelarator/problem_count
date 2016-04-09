from common import match
from common import decompress
from common import spide
from config import noj_url
from config import noj_page_count_pattern
from config import get_data_failed
from config import match_user_failed
from config import noj_td_pattern
from config import noj_username_pattern

def get_page_count(url):
    data = decompress(spide(url+'1'))
    if data is None:
        return get_data_failed
    data = data.decode('utf-8')
    page_info = match(noj_page_count_pattern, data)[0]
    char_pos = page_info.index('=')
    return int(page_info[char_pos+1:])

def spide_for_noj(username, url):
    page_count = get_page_count(url+'1')
    if page_count == get_data_failed:
        return get_data_failed
    for page in range(1, page_count+1):
        page_url = url + str(page)
        info = find_user(username, page_url)
        if info == get_data_failed:
            return get_data_failed
        if info != match_user_failed:
            return info
    return match_user_failed

def find_user(username, page_url):
    data = decompress(spide(page_url)).decode('utf-8') 
    if data is None:
        return get_data_failed
    td_data = match(noj_td_pattern, data)
    for i in range(2, len(td_data), 6):
        cur_username = match(noj_username_pattern, td_data[i])[0]
        if username.lower() == cur_username.lower():
            return td_data[i+3]
    return match_user_failed
if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        print('Input your noj account please.')
    else:
        ac_number = spide_for_noj(sys.argv[1], noj_url)
        print(ac_number)
