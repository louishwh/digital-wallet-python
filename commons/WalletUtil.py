#
# -*- coding:utf-8 -*-
# author: louis
from bitcoin import *
import os

if __name__ == '__main__':
    private_key = sha256("123")
    public_key = privkey_to_pubkey(private_key)
    address = pubkey_to_address(public_key)

    print("{}\n{}\n{}".format(private_key, public_key, address))