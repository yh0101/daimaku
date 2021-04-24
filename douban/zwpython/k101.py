#!/usr/bin/python3 python
# -*- encoding: utf-8 -*-
'''
@File    :   k101.py
@Time    :   2021/04/24 16:54:49
@Author  :   yh0101 
@Contact :   yh0101@outlook.com
@License :   (C)Copyright 2021-2025
@Desc    :   None
'''

# here put the import lib
import numpy as np

def sta001(k,nyear,xd):
    d2=np.fv(k,nyear,-xd,-xd);
    d2=round(d2)
    return d2

d40=1.4*40
print("d40,40 x 1.4=",d40)
d=sta001(0.05,40-1,1.4);
print("01保守投资模式, ",d,round(d/d40))

d2=sta001(0.20,40-1,1.4);
print("02激进投资模式, ",d2,round(d2/d40))

dk=round(d2/d)
print("dk,两者差别(xx倍): ",dk)