'''
 * @author  anlzou
 * @date  2020/6/27 11:04
 * @version xx
 * @description xx
'''

import pandas as pd
import os

data = pd.read_csv('北海.csv', encoding='gbk')
with open('北海.txt', 'a+', encoding='utf-8') as f:
    for line in data.values:
        f.write((str(line[0]) + '\t' + str(line[11]) + '\n'))