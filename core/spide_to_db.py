from MySQLdb import Connection
from noj_count import spide_for_noj
from config import database
from config import insert_data
from config import update_data
from config import find_data

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
            continue
        else:
            return mysqldb

def fetch_noj():
    user_list = []
    print('spiding... wait.')
    spide_for_noj(user_list) 
    mysqldb = db_connect()
    cursor = mysqldb.cursor()
    for user, ac_number in user_list:
        print('start to write ', user, 'ac number:', ac_number)
        cursor.execute(find_data.format('count_noj', user))
        row = cursor.fetchone()
        if row is None:
            cursor.execute(insert_data.format('count_noj', user, int(ac_number)))
        else:
            user_id, ac_number = row
            cursor.execute(update_data.format('count_noj', user,
                                              int(ac_number), user_id))

    mysqldb.commit()
    mysqldb.close()

def find_from_noj_db(username):
    mysqldb = db_connect()
    cursor = mysqldb.cursor()
    cursor.execute(find_data.format('count_noj', username))
    row = cursor.fetchone()
    if row is None:
        return 0
    user, ac_number = row
    return ac_number
if __name__ == '__main__':
    fetch_noj()

