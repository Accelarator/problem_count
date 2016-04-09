from common import decompress
from common import match
from common import spide
from config import bzoj_url
from config import get_data_failed
from config import match_user_failed
from config import bzoj_ac_pattern

def spide_for_bzoj(username, url):
    data = decompress(spide(url+username))
    if data is None:
        return get_data_failed
    data = data.decode('utf-8')
    if data[-13:-1] == 'No such User!':
        return match_user_failed
    ac_number = match(bzoj_ac_pattern, data)[0]
    return ac_number
if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        print('Input your bzoj account please')
    else:
        ac_number = spide_for_bzoj(sys.argv[1], bzoj_url)
        print(ac_number)
