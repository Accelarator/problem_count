from common import match
from common import decompress
from common import spide
from config import zoj_url
from config import match_user_failed
from config import zoj_user_pattern
from config import zoj_ac_pattern
from config import zoj_div_pattern
from config import get_data_failed

def get_user_url(username):
    url = zoj_url
    data = decompress(spide(url.format(username)))
    if data is None:
        return get_data_failed
    data = data.decode('utf-8')
    user_url = match(zoj_user_pattern, data)
    if user_url is None or len(user_url) == 0:
        return match_user_failed
    return 'http://www.icpc.moe' + user_url[0]

def spide_for_zoj(username):
    url = zoj_url
    url = get_user_url(username) 
    if url == get_data_failed:
        return get_data_failed
    if url == match_user_failed:
        return match_user_failed
    data = decompress(spide(url.format(username)))
    if data is None: 
        return get_data_failed
    data = data.decode('utf-8')
    div_data = match(zoj_div_pattern, data)[0]
    ac_number = match(zoj_ac_pattern, div_data)[0]
    char_pos = ac_number.index('/')
    return ac_number[:char_pos]
if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        print('Input your zoj account please.')
    else:
        ac_number = spide_for_zoj(sys.argv[1], zoj_url)
        print(ac_number)
