#
# -*- coding:utf-8 -*-
# author: louis

class WalletCore(object):

    def __init__(self):
        self.public_key = ""
        self.private_key = ""
        self.net_params = ""
        self.password = ""


class Wallet(object):

    def __init__(self):
        self.address = ""
        self.mnemonic_list = []
        self.wallet_core = WalletCore()



class WalletManager(object):

    @classmethod
    def generate_mnemonic(cls):
        return ""

    @classmethod
    def is_validate_mnemonic(cls, mnemonic_list):
        return ""

    @classmethod
    def generate_wallet(cls):
        """
        生成钱包
        :return: 钱包详情
        """
        return ""

    @classmethod
    def generate_wallet_from_mnemonic(cls, mnemonic_list, net, password):
        if not cls.is_validate_mnemonic(mnemonic_list):
            return Wallet()








