from config import ural_url
from config import match_user_failed
from config import ural_table_pattern
from config import get_data_failed
from config import ural_tr_pattern
from config import ural_ac_number_pattern
from config import ural_user_pattern
from common import match
from common import decompress
from common import spide
def spide_for_ural(username, url):
    data = decompress(spide(url+username))
    if data is None:
        return get_data_failed
    data = data.decode('utf-8')
    table_data = match(ural_table_pattern, data)
    if table_data is None:
        return match_user_failed
    table_data = table_data[0]
    tr_data = match(ural_tr_pattern, table_data)[1:]
    for item in tr_data:
        cur_username = match(ural_user_pattern, item)[0]
        if cur_username == username:
            ac_number = match(ural_ac_number_pattern, item)[2]
            return ac_number
    return match_user_failed


if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        print("Input your ural account please.")
    else:
        ac_number = spide_for_ural(sys.argv[1], ural_url)
        print(ac_number)

