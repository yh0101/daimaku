#!/usr/bin/python3 python
# -*- encoding: utf-8 -*-
'''
@File    :   ch1_5.py
@Time    :   2021/04/25 13:02:03
@Author  :   yh0101 
@Contact :   yh0101@outlook.com
@License :   (C)Copyright 2021-2025
@Desc    :   None
'''

# here put the import lib
from tkinter import *

root = Tk()
screenWidth = root.winfo_screenwidth()       # 屏幕宽度
screenHeight = root.winfo_screenwidth()      # 屏幕高度
w = 300          # 窗口宽
h = 160          # 窗口高
x = 400          # 窗口左上角x轴位置
y = 200          # 窗口左上角y轴位置
root.geometry("%dx%d+%d+%d" % (w,h,x,y))
root.mainloop()