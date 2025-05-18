luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
# Đánh Dấu Bản Quyền
ndp_tool = trang + "" + do + "[" + trang + "=.=" + do + "] " + trang + "=> "
ndp = trang + "" + do + "[" + trang + "=.=" + do + "] " + trang + "=> "
# Config
__ZALO__ = '0777374145'
__ADMIN__ = 'An Orin'
__FACEBOOK__ = 'anorintool'
__VERSION__ = '1.0'
dem = 0
# import lib
import requests, os, sys
from time import sleep
from datetime import datetime
try:
    import requests
except:
    print(luc+"Bạn Chưa Tải Thư Viện \n Bắt Đầu Tải... ")
    os.system("pip install requests")
# ====================== [ FUNCTION ] ====================== 
def echo(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()
def banner():
    banner = f"""

  \033[1;35m  █████╗  ███╗   ██╗     ██████╗ ██████╗ ██╗███╗   ██╗     
    \033[1;37m██╔══██╗████╗  ██║    ██╔═══██╗██╔══██╗██║████╗  ██║     
    \033[1;35m███████║██╔██╗ ██║    ██║   ██║██████╔╝██║██╔██╗ ██║    
    \033[1;37m██╔══██║██║╚██╗██║    ██║   ██║██╔══██╗██║██║╚██╗██║     
    \033[1;35m██║  ██║██║ ╚████║    ╚██████╔╝██║  ██║██║██║ ╚████║
    \033[1;37m╚═╝  ╚═╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝


\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;31mCopyright By: \033[1;35m{__ADMIN__}
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mZalo: \033[1;34m{__ZALO__}
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;36mFacebook: \033[1;37mFb.com/{__FACEBOOK__}
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[0;93mTool Auto Reg Page Pro5 {__VERSION__}
\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"""
    echo(banner)
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def thanh():
    print('\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
def ndp_delay(o):
    while(o>1):
        o=o-1
        print(f'{trang}[\033[1;31mA\033[1;33mN \033[1;36mO\033[1;35mR\033[1;34mI\033[1;32mN\033[1;37m[\033[1;36m|\033[1;37m]\033[1;37m[.....]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;35mA\033[1;32mN \033[1;34mO\033[1;35mR\033[1;36mI\033[1;33mN\033[1;37m[\033[1;31m/\033[1;37m]\033[1;37m[\033[1;32m>\033[1;37m....]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;31mA\033[1;33mN \033[1;36mO\033[1;35mR\033[1;34mI\033[1;32mN\033[1;37m[\033[1;32m-\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;37m...]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;35mA\033[1;32mN \033[1;34mO\033[1;35mR\033[1;36mI\033[1;33mN\033[1;37m[\033[1;33m+\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;37m..]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;31mA\033[1;33mN \033[1;36mO\033[1;35mR\033[1;34mI\033[1;32mN\033[1;37m[\033[1;34m\{trang}]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;33m>\033[1;37m.]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;35mA\033[1;32mN \033[1;34mO\033[1;35mR\033[1;36mI\033[1;33mN\033[1;37m[\033[1;35m|\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;33m>\033[1;35m>\033[1;37m]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
# =================[ START TOOL ]===========================
clear()
banner()
cookie = input(ndp_tool+luc+'Vui Lòng Nhập Cookie Facebook'+trang+': '+vang)
headers = {
        'authority': 'mbasic.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'origin': 'https://mbasic.facebook.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://mbasic.facebook.com/',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': cookie
}
    
try:
    print(ndp_tool+trang+"Đang Check Live Cookie...", end="\r")
    find_data = requests.get("https://mbasic.facebook.com/", headers=headers).text
    fb_dtsg = find_data.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoest = find_data.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
    uid = cookie.split('c_user=')[1].split(';')[0]
except:
    print(ndp+do+"Cookie Die Vui Lòng Kiểm Tra Lại!!!")
# =================[ NHẬP DELAY ]===========================
clear()
banner()
delay = int(input(ndp_tool+luc+'Vui Lòng Nhập Delay Reg Page'+trang+': '+vang))
# GET INFO
json_name = requests.get('https://keysiuvip.com/ndp_api/getthongtin.php?cookie='+cookie).json()
if json_name['status'] == 'success':
    id = json_name['id']
    name_fb = json_name['name']
    thanh()
    print(luc+'NAME FB: '+vang+str(name_fb)+do+' | '+luc+'UID FB: '+vang+str(id)+'')
    thanh()
else:
    exit(ndp_tool+do+'Get Thông Tin Thất Bại!!')

while True: 
    name = requests.get('https://story-shack-cdn-v2.glitch.me/generators/vietnamese-name-generator/male?count=2').json()['data'][0]['name']
    headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com/pages/creation/?ref_type=launch_point',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'viewport-width': '1221',
        'x-fb-friendly-name': 'AdditionalProfilePlusCreationMutation',
        'x-fb-lsd': 'wPd4PRo0e2MNyiZJhrq96a',
        'cookie': cookie,
    }

    data = {
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'lsd': 'wPd4PRo0e2MNyiZJhrq96a',
        '__spin_r': '1006614608',
        '__spin_b': 'trunk',
        '__spin_t': '1668582022',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation',
        'variables': '{"input":{"bio":"test tool auto reg page pro5 by NguyenDucPhat","categories":["660696964377118"],"creation_source":"comet","name":"'+name+'","page_referrer":"launch_point","actor_id":"'+uid+'","client_mutation_id":"1"}}',
        'server_timestamps': 'true',
        'doc_id': '5903223909690825',
    }

    response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
    if 'id' in response.text:
        dem=dem+1
        id = response.json()['data']['additional_profile_plus_create']['additional_profile']['id']
        print(f''+do+'['+trang+'AN ORIN'+do+'] | '+do+'['+vang+str(dem)+do+'] | '+do+'['+trang+name+do+'] | '+do+'['+trang+id+do+']')
        ndp_delay(delay)
    else:
        exit(ndp_tool+do+'Clone Đã Bị Block Reg Page!!!')