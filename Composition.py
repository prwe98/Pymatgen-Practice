'''
-*- coding: utf-8 -*-
@Name        : Composition
@Time        : 2021/3/22 0022 11:14
@Author      : Xiaoyu Wu
@Institution : UESTC
'''

import pymatgen.core as mg
import requests
import pandas as pd
import numpy as np
import random
from pymatgen import MPRester, Element, Composition
import itertools  # itertools可以提供几种无限迭代器count(), cycle(), repeat(, times), takewhile()....
import time
# API_KEY = {"API_KEY": 'mXC0lwK6QBDIqZVc'}
# response = requests.get("https://www.materialsproject.org/rest/v2/materials/Fe2O3/vasp", API_KEY)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

start_time = time.time()

API_KEY = 'mXC0lwK6QBDIqZVc'

element = ["H", "Li", "Be", "C", "N", "O", "Na",
            "Mg", "Al", "Si", "P", "S", "K", "Ca", "Sc", "Ti",
            "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As",
            "Se", "Br", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru",
            "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "Cs",
            "Ba", "La", "Ta", "W", "Re", "Os"]

complx = list(itertools.combinations(element, 2))
complx_pikced = random.sample(complx, 300)

system = list(map(lambda x: complx_pikced[x][0] + '-' + complx_pikced[x][1], np.arange(len(complx_pikced))))

def que(x):
    a = MPRester(API_KEY)
    data = a.query(criteria=x, properties=["unit_cell_formula", "pretty_formula", "spacegroup"])
    return data

data=[]
valid_num=[]
for i in system:
    res=que(i)
    if res !=[]:
        data.extend(res)
        valid_num.append(system.index(i))
        print(len(res),"bloody hell!",system.index(i))

data = pd.DataFrame(data=data)

print(data)

data.to_csv('data.csv')

print(f'finish time :{(time.time() - start_time):0.2f}')
# df = pd.DataFrame(response)
# df.to_csv("response.csv", index=False, encoding="gb18030")
# mpr = MPRester("mXC0lwK6QBDIqZVc")
# print(mpr.supported_properties)

