import os
headers = {
    'User-Agent': '''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87
    Safari/537.36''',
    'Connection': 'close',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}
# Error Code
get_data_failed = -1
match_user_failed = -2

# Maximum Process Number
# depend on the number of core
MPN = os.cpu_count()

# Spide Time Limits
TIME = 10
# Each OJ's URL
hdu_url = 'http://acm.hdu.edu.cn/search.php?field=author&key='
poj_url = 'http://poj.org/searchuser?key={0}&B1=Search'
noj_url = 'https://ac.2333.moe/User/user_list.xhtml?page='
codeforces_url = 'http://codeforces.com/problemset/standings/page/'
spoj_url = 'http://www.spoj.com/ranks/users/start='
bzoj_url = 'http://www.lydsy.com/JudgeOnline/ranklist.php?start='
zoj_url = 'http://acm.zju.edu.cn/onlinejudge/showRankList.do?contestId=1&from='
sgu_url = 'http://acm.sgu.ru/standing.php?onpage=50&page='
ural_url = 'http://acm.timus.ru/ranklist.aspx?from='
fzu_url = 'http://acm.fzu.edu.cn/ranklist.php?page='
acdream_url = 'http://acdream.info/ranklist?page='

# Corresponding regular expression pattern.
# hdu 
hdu_table_pattern = '<table width="80%" border="0" align="center" cellspacing="2" class=\'TABLE_TEXT\'>([\s\S]*?)</table>'
hdu_td_pattern = '<td>([\s\S]*?)</td>'
hdu_username_pattern = '<A href="[\s\S]*?">([\s\S]*?)</A>'
hdu_ac_number_pattern = '<A href="[\s\S]*?">([\s\S]*?)</A>'
hdu_submit_number_pattern = '<A href="[\s\S]*?">([\s\S]*?)</A>'

# noj
noj_page_count_pattern = '<a title="尾页" href="([\s\S]*?)" class="page_a">'
noj_td_pattern = '<td style="text-align: center;">([\s\S]*?)</td>'
noj_username_pattern = '<a target="_blank" href="[\s\S]*?">([\s\S]*?)</a>'

# poj
poj_table_pattern = '<table border=1 width=80%>([\s\S]*?)</table>'
poj_td_pattern = '<td>([\s\S]*?)</td>'
poj_username_pattern = '<a href=[\s\S]*?>([\s\S]*?)</a>'

# sgu

# database configuration
database = {
    'host': '',
    'db': '',
    'user': '',
    'password': '',
    'charset': '',
}

# sql
find_data = 'select id from {0} where username=\"{1}\" and ac_number={2} and submit_number={3}'
insert_data = 'insert into {0} (username, ac_number, submit_number) values (\"{1}\", {2}, {3})'
update_data = 'update {0} set username=\"{1}\",ac_number={2} ,submit_number={3} where id={4}'
