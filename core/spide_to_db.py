from MySQLdb import Connection
from noj_count import spide_for_noj
from config import database
from config import insert_data
from config import update_data
from config import find_data
from lightoj_count import spide_for_lightoj

def db_connect():
    while True:
        try:
            mysqldb = Connection(host=database['host'],
                                 user=database['user'],
                                 passwd=database['password'],
                                 db=database['db'],
                                 charset=database['charset']
                                )
        except Exception:
            print('error')
            continue
        else:
            return mysqldb

def store(oj, user_list):
    mysqldb = db_connect()
    cursor = mysqldb.cursor()
    for user, ac_number in user_list:
        print('start to write ', user, 'ac number:', ac_number)
        cursor.execute(find_data.format(oj, user))
        row = cursor.fetchone()
        print(row)
        if row is None:
            cursor.execute(insert_data.format(oj, user, int(ac_number)))
            print(insert_data.format(oj, user, int(ac_number)))
        else:
            user_id, ac_number = row
            cursor.execute(update_data.format(oj, user,
                                              int(ac_number), user_id))

    mysqldb.commit()
    mysqldb.close()

def fetch_noj():
    user_list = []
    print('spiding noj... wait.')
    spide_for_noj(user_list) 
    store('count_noj', user_list)

def fetch_lightoj():
    user_list = []
    print('spding lightoj... wait.')
    spide_for_lightoj(user_list)
    print(len(user_list))
    store('count_lightoj', user_list)

def find_from_db(oj, username):
    mysqldb = db_connect()
    cursor = mysqldb.cursor()
    cursor.execute(find_data.format(oj, username))
    row = cursor.fetchone()
    if row is None:
        return 0
    user, ac_number = row
    return ac_number
if __name__ == '__main__':
    fetch_lightoj()
    fetch_noj()
