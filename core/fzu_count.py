from common import decompress
from common import match
from common import spide
from config import fzu_url
from config import fzu_ac_number_pattern
from config import get_data_failed
from config import match_user_failed

def spide_for_fzu(username):
    url = fzu_url + username
    data = decompress(spide(url))
    if data is None:
        return get_data_failed
    data = data.decode('utf-8')
    ac_number = match(fzu_ac_number_pattern, data)
    if ac_number is None or len(ac_number) < 1:
        return match_user_failed
    return ac_number[1]

if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        print('Input your fzu account please.')
    else:
        ac_number = spide_for_fzu(sys.argv[1], fzu_url+sys.argv[1])
        print(ac_number)
