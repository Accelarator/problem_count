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

def spide_for_noj(user_list):
    url = noj_url
    page_count = get_page_count(url+'1')
    if page_count == get_data_failed:
        return 
    for page in range(1, page_count+1):
        page_url = url + str(page)
        res = find_user(user_list, page_url)
        if res == False:
            break

def find_user(user_list, page_url):
    data = decompress(spide(page_url))
    if data is None:
        return get_data_failed
    data = data.decode('utf-8')
    td_data = match(noj_td_pattern, data)
    for i in range(2, len(td_data), 6):
        cur_username = match(noj_username_pattern, td_data[i])[0]
        print('get ', cur_username)
        if int(td_data[i+3]) == 0:
            return False
        user_list.append((cur_username, td_data[i+3]))
    return True
if __name__ == '__main__':
    user_list = []
    spide_for_noj(user_list)
