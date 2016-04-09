from common import decompress
from common import match
from common import spide
from config import sgu_url 
from config import get_data_failed
from config import match_user_failed

def spide_for_sgu(username, url):
    data = decompress(spide(url))
    if data is None:
        return get_data_failed
    data = data.decode('gb2312')
    print(data)

if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        print("Input your sgu account please")
    else:
        spide_for_sgu(sys.argv[1], sgu_url)
