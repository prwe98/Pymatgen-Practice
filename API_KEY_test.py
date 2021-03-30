'''
-*- coding: utf-8 -*-
@Name        : API_KEY_test
@Time        : 2021/3/29 0029 17:49
@Author      : Xiaoyu Wu
@Institution : UESTC
'''

from pymatgen import MPRester

# api_key has written in pymatgen config file
with MPRester() as m:
    # structure id
    structure = m.get_structure_by_material_id('mp-1234')

    # DOS from material id
    dos = m.get_dos_by_material_id('mp-1234')

    # Band structure for material id
    band = m.get_bandstructure_by_material_id('mp-1234')

# 这种传输方式API的密钥是没有加密的，确定地址是https，密钥不会泄露。和的比特币交易所的API是类似, 但是比特币交易所所用的为加密API

