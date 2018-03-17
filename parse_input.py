# -*- coding: utf-8 -*-
import humanfriendly
import sys
import re
import json
from json.decoder import JSONDecodeError


def show_usage():
    print("""A simple python script helps you use less IPv4 data.
    When given limit is reached, sign out and exit.

    usage: buptuse [usage-limit]
    A readable size is supported. Examples:
        buptuse 900K    use 900KiB of IPv4 data
        buptuse 100MB   use 100MiB of IPv4 data
        buptuse 1G      use 1GiB of IPv4 data

    If not given, default limit is 50M.
    """)


def parse_input_limit(default):
    """
    Parse data usage limit provided in sys.argv.
    If not given, the default value is LIMIT_DEFAULT(50M).

    :return: User-input, and usage limit(KB).
    :rtype: (str, int)
    """

    # NOTE: sys.argv[0] is .py filename.
    if len(sys.argv) >= 3:
        user_input = sys.argv[1] + sys.argv[2]
    elif len(sys.argv) == 2:
        user_input = sys.argv[1]
    else:
        user_input = default

    # Strip all whitespaces
    user_input = re.sub(r'\s+', "", user_input)

    # If user input does not look like "xx KB/G/mb"
    if not re.fullmatch(r'\d+[tmgk](b|ib)?', user_input, re.IGNORECASE):
        raise ValueError("Invalid input: {}".format(user_input))

    # Represented in KB.
    usage_limit = \
        int(humanfriendly.parse_size(user_input, binary=True) / 1024)

    return user_input, usage_limit

def get_stored_account(addr):
    data = json.load(open(addr))
    return data['user'], data['pwd']