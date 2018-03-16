# -*- coding: utf-8 -*-
import requests
from gate_api.errors import *

login_url = 'http://10.3.8.211'
logout_url = 'http://10.3.8.211/F.htm'


def login_data(user, pwd):
    return {
        'DDDDD': user,
        'upass': pwd,
        '0MKKey': ''
    }


def sign_in(user, pwd):
    r = requests.post(login_url, data=login_data(user, pwd)).text
    if r.find("<title>登录成功窗</title>") < 0:
        raise GatewayApiError("Failed to sign in.")


def sign_out():
    r = requests.get(logout_url).text
    flow_loc = r.find("flow='")
    return int(r[flow_loc + 6: flow_loc + 16])


def is_login():
    r = requests.get(login_url).text
    return r.find("<title>上网注销窗</title>") >= 0


def data_usage():
    r = requests.get(login_url).text
    if r.find("<title>上网注销窗</title>") < 0:
        raise GatewayNotLoginError()

    flow_loc = r.find("flow='")
    return int(r[flow_loc + 6: flow_loc + 16])

def main():
    pass


if __name__ == '__main__':
    main()
