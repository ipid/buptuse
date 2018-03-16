# BuptUse
The tool aims to help you reduce IPv4 data cost in BUPT.

Features
---

If you are a student in BUPT, you may understand that every bit of IPv4 data costs a lot. 

Therefore, I developed a tool that simply sign out BUPT gateway after your data usage reaches a specified number. That prevents some malwares from costing too much IPv4 data.

Compability
---

**The tool supports Python 3.5+ and probably every platforms.**

Setup
---

Currently the tool doesn't support `pip`. You may have to install the tool as following:

    sudo pip3 install --upgrade humanfriendly requests tqdm

Then write your BUPT gateway username and password into config file. It's path is as follows:

> **Linux**: ~/.buptuse/config.json

> **Windows**: %HomeDrive%%HomePath%\\.buptuse\\config.json
> (Get exact path with command `echo %HomeDrive%%HomePath%\.buptuse\config.json` in `cmd`)

A template for configuation file:

    {
        "user": "2016123456",
        "pwd": "[password]"
    }

Usage
---
`cd` into the directory that contains `buptuse.py`. Then run following commands:

    usage: python3 buptuse.py [usage-limit]
    A readable size is supported. Examples:
        python3 buptuse.py 900Kb    use 900KiB of IPv4 data
        python3 buptuse.py 100MiB   use 100MiB of IPv4 data
        python3 buptuse.py 1g       use 1GiB of IPv4 data