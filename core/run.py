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

def proc(user, L, func, oj):
    ac = func(user)
    if ac == get_data_failed:
        L.append(("Fetch data error.", oj))
    else:
        if ac == match_user_failed:
            L.append((0, oj))
        else:
            L.append((ac, oj))

def work_one(user, search_list):
    L = []
    proc(user, L, spide_for_hdu, 'hdu')
#    proc(user, L, spide_for_noj, 'noj')
    proc(user, L, spide_for_zoj, 'zoj')
    proc(user, L, spide_for_bzoj, 'bzoj')
    proc(user, L, spide_for_acdream, 'acdream')
    proc(user, L, spide_for_fzu, 'fzu')
    proc(user, L, spide_for_sgu, 'sgu')
    proc(user, L, spide_for_ural, 'ural')
    proc(user, L, spide_for_poj, 'poj')
    search_list.append((user, L))

def run(search_list, account):
    work_one(account, search_list)

if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        print("input your account.")
    else:
        L = []
        run(L, sys.argv[1])
        print(L)