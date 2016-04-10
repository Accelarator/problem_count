from common import match
from common import decompress
from common import spide
from config import acdream_url
from config import acdream_ul_pattern
from config import acdream_ac_number_pattern
from config import get_data_failed
from config import match_user_failed

def spide_for_acdream(username):
    url = acdream_url
    data = decompress(spide(url+username))
    if data is None:
        return get_data_failed
    data = data.decode('utf-8')
    ul_data = match(acdream_ul_pattern, data)
    if ul_data is None or len(ul_data) < 1:
        return match_user_failed
    ul_data = ul_data[0]
    ac_number = match(acdream_ac_number_pattern, ul_data)
    return ac_number[0]
