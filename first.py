# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 13:36:14 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()


time.sleep(5)
x,y,z = mc.player.getTilePos()

a=0

while a<10:
    mc.setBlock(x,y,z,1)
    y=y+1
    a=a+1
