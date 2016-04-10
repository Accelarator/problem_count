from common import decompress
from common import match
from common import spide
from config import sgu_url 
from config import get_data_failed
from config import match_user_failed
from config import sgu_ac_number_pattern
from config import sgu_table_pattern
from config import sgu_tr_pattern

def spide_for_sgu(username):
    url = sgu_url
    data = decompress(spide(url+username))
    if data is None:
        return get_data_failed
    data = data.decode('utf-8')
    table_data = match(sgu_table_pattern, data)
    if table_data is None or len(table_data) < 1:
        return match_user_failed
    tr_data = match(sgu_tr_pattern, table_data[0])[17]
    return match(sgu_ac_number_pattern, tr_data)[0]

if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        print("Input your sgu account please")
    else:
        ac_number = spide_for_sgu(sys.argv[1], sgu_url)
        print(ac_number)
