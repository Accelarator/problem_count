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
from codeforces_count import spide_for_codeforces
import threading
import multiprocessing

def proc(lock, user, L, func, oj):
    ac = func(user)
    lock.acquire()
    if ac == get_data_failed:
        L.append((-1, oj))
    else:
        if ac == match_user_failed:
            L.append((0, oj))
        else:
            L.append((ac, oj))
    lock.release()

def work_one(lock, user, L):
    proc(lock, user, L, spide_for_hdu, 'hdu')
    proc(lock, user, L, spide_for_zoj, 'zoj')
    proc(lock, user, L, spide_for_bzoj, 'bzoj')
    proc(lock, user, L, spide_for_acdream, 'acdream')
    proc(lock, user, L, spide_for_fzu, 'fzu')
    proc(lock, user, L, spide_for_sgu, 'sgu')
    proc(lock, user, L, spide_for_ural, 'ural')
    proc(lock, user, L, spide_for_poj, 'poj')
    L.append((find_from_db('count_noj', user), 'noj'))
    L.append((find_from_db('count_lightoj', user), 'lightoj'))

def work_two(lock, user, L):
    lock.acquire()
    L.append((spide_for_codeforces(user), 'codeforces'))
    lock.release()
    
def run(account):
    L = []
    lock = threading.Lock()
    codeforces_thread = threading.Thread(target=work_two, args=(lock, account,
                                                               L))
    codeforces_thread.start()
    work_one(lock, account, L)
    codeforces_thread.join()
    return account, L

def start(account_list):
    L = []
    Pools = multiprocessing.Pool(len(account_list)) 
    Pools.map_async(run, account_list,callback=lambda res:(L.append(res)))
    Pools.close()
    Pools.join()
    return L

if __name__ == '__main__':
    import sys
    import time
    if len(sys.argv) <= 1:
        print("Please input your account.")
    else:
        a = time.time()
        L = start(sys.argv[1:])
        print(L)
        b = time.time()
        print('cost time is {0}'.format(round(b - a, 1)))
