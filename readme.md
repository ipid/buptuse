# BuptUse
The tool aims to help you reduce IPv4 data cost in BUPT.

Features
---

If you are a student in BUPT, you may understand that every byte of IPv4 data costs a lot. 

Therefore, I developed a tool that simply sign out BUPT gateway after your data usage reaches a number. That will prevent some malwares from using your IPv4 data without noticing you.

**The tool supports Python 3.5+.**

Setup
---

Currently the tool doesn't support `pip`. You may have to install the tool as following:

    sudo pip3 install --upgrade humanfriendly requests

And `cd` into current directory every time.

Usage
---

    usage: buptuse [usage-limit]
    A readable size is supported. Examples:
        buptuse 900K    use 900KiB of IPv4 data
        buptuse 100MB   use 100MiB of IPv4 data
        buptuse 1G      use 1GiB of IPv4 data