from common import match
from common import decompress
from common import spide
from config import acdream_url
from config import acdream_ul_pattern
from config import acdream_ac_number_pattern

def spide_for_acdream(username, url):
    data = decompress(spide(url+username))
    if data is None:
        return get_data_failed
    data = data.decode('utf-8')
    ul_data = match(acdream_ul_pattern, data)
    if ul_data is None:
        return match_user_failed
    ul_data = ul_data[0]
    ac_number = match(acdream_ac_number_pattern, ul_data)
    return ac_number[0]
if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        print('Input your acdream account please.')
    else:
        ac_number = spide_for_acdream(sys.argv[1], acdream_url)
        print(ac_number)
