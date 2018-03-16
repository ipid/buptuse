# -*- coding: utf-8 -*-
import sys
from gate_api import gate_api
import parse_input
import time
import humanfriendly
from pathlib import Path
from gate_api.errors import GatewayNotLoginError

LIMIT_DEFAULT = '50M'
CONFIG_ADDR = Path.home() / '.buptuse' / 'config.json'
SLEEP_DURATION = 3

r"""
    Config file format:
    {
        "user": "[username]",
        "pwd": "[password]"
    }
    
    It should be under ~/.buptuse/config.json (Linux)
    or [SystemDisk]:\Users\[UserName]\.buptuse\config.json (Windows).
"""

def wait_until_usage(usage):
    while True:
        if gate_api.data_usage() >= usage:
            break
        time.sleep(SLEEP_DURATION)

def main():
    # Print usage
    if '-h' in sys.argv or '--help' in sys.argv:
        return parse_input.show_usage()

    # Parse user-input data usage limit
    try:
        input_limit, usage_limit = parse_input.parse_input_limit(LIMIT_DEFAULT)
    except ValueError as err:
        print(err)
        return

    # Retrieve username and password from config.json
    try:
        uname, pwd = parse_input.get_stored_account(CONFIG_ADDR)
    except FileNotFoundError:
        print("Config file not found.\n"
            "Double-check document to fix the problem.")
        return
    except ValueError:
        print("There is error in config file.\n"
              "Double-check document to fix the problem.")
        return

    print("Signin until {} of data used.\n".format(input_limit))
    print("Attempt to sign in...")
    gate_api.sign_in(uname, pwd)
    print("Sign-in succeed.")

    init_usage = gate_api.data_usage()

    limit_exceed = False
    try:
        wait_until_usage(init_usage + usage_limit)
        limit_exceed = True
    except KeyboardInterrupt:
        print("Ctrl+C detected.")
    except GatewayNotLoginError:
        print("Signed out by user or other applications.")

    total_usage = gate_api.sign_out() - init_usage
    if total_usage > usage_limit:
        print("{} limit exceeded.".format(input_limit))
    
    print("\nTotal usage: %s." \
            % humanfriendly.format_size(total_usage * 1024, binary=True))


if __name__ == '__main__':
    main()
