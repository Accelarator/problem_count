from common import decompress
from common import match
from common import spide
from config import get_data_failed
from config import match_user_failed
from config import lightoj_login_url
from config import lightoj_userlist_url
from urllib import request
from urllib import parse
from config import headers
from http import cookiejar
from config import lightoj_tr_data_one_pattern
from config import lightoj_tr_data_two_pattern
from config import lightoj_page_count_pattern
from config import lightoj_td_data_one_pattern
from config import lightoj_td_data_two_pattern
from config import lightoj_user_data_one_pattern
from config import lightoj_user_data_two_pattern

post_data = {
    'myuserid': '15728042044@163.com',
    'mypassword': 'use_for_spide',
    'Submit': 'Login',
}

def spide_for_lightoj(user_list):
    data = parse.urlencode(post_data).encode('utf-8')
    cookie = cookiejar.CookieJar()
    opener = request.build_opener(request.HTTPCookieProcessor(cookie))
    request.install_opener(opener)
    try:
        Req = request.Request(url=lightoj_login_url, data=data, headers=headers)
        Res = request.urlopen(Req)
    except Exception:
        return user_list
    else:
        page_tot = page_count()
        if page_tot == get_data_failed:
            return
        for page in range(page_tot):
            url = lightoj_userlist_url + str(page*50+1) 
            data = decompress(spide(url))
            if data is None:
                continue
            data = data.decode('utf-8')
            user_one = match(lightoj_tr_data_one_pattern, data)
            user_two = match(lightoj_tr_data_two_pattern, data)
            get(user_list, user_one, lightoj_user_data_one_pattern,
                lightoj_td_data_one_pattern)
            get(user_list, user_two, lightoj_user_data_two_pattern,
                lightoj_td_data_two_pattern)

def page_count():
    data = decompress(spide(lightoj_userlist_url))
    if data is None:
        return get_data_failed
    data = data.decode('utf-8')
    page = match(lightoj_page_count_pattern, data)[-1:][0]
    return int(page.lstrip().rstrip())

def get(user_list, user, user_name_pattern, ac_number_pattern): 
    for item in user:
        username = match(user_name_pattern, item)[0].lstrip().rstrip()
        ac_number = match(ac_number_pattern, item)
        for i in range(2, len(ac_number), 4):
            print('get', username, 'AC:', ac_number[i].lstrip().rstrip())
            user_list.append((username, ac_number[i].lstrip().rstrip()))

if __name__ == '__main__':
    print('db ok')
    user_list = []
    spide_for_lightoj(user_list)
