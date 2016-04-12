from hdu_count import spide_for_hdu
from noj_count import spide_for_noj
from zoj_count import spide_for_zoj
from bzoj_count import spide_for_bzoj
from acdream_count import spide_for_acdream
from fzu_count import spide_for_fzu
from sgu_count import spide_for_sgu
from ural_count import spide_for_ural
from poj_count import spide_for_poj
from config import get_data_failed
from config import match_user_failed
from spide_to_db import find_from_db
def proc(user, L, func, oj):
    print('start fetch ', oj)
    ac = func(user)
    if ac == get_data_failed:
        L.append(("Fetch data error.", oj))
    else:
        if ac == match_user_failed:
            L.append((0, oj))
        else:
            L.append((ac, oj))
    print('end fetch ', oj)

def work_one(user, search_list):
    L = []
    proc(user, L, spide_for_hdu, 'hdu')
    proc(user, L, spide_for_zoj, 'zoj')
    proc(user, L, spide_for_bzoj, 'bzoj')
    proc(user, L, spide_for_acdream, 'acdream')
    proc(user, L, spide_for_fzu, 'fzu')
    proc(user, L, spide_for_sgu, 'sgu')
    proc(user, L, spide_for_ural, 'ural')
    proc(user, L, spide_for_poj, 'poj')
    L.append((find_from_db('count_noj', user), 'noj'))
    L.append((find_from_db('count_lightoj', user), 'lightoj'))
    search_list.append((user, L))

def run(search_list, account):
    work_one(account, search_list)

if __name__ == '__main__':
    import sys
    import time
    if len(sys.argv) <= 1:
        print("Please input your account.")
    else:
        a = time.time()
        L = []
        run(L, sys.argv[1])
        print(L)
        b = time.time()
        print('cost time is {0}'.format(round(b - a, 1)))
