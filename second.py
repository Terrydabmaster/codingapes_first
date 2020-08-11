# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 14:08:38 2020

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

from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()


time.sleep(5)
x,y,z = mc.player.getTilePos()

mc.setBlock(x,y,z,20)
x,y,z = mc.player.getTilePos()

mc.setBlock(x,y-1,z,20)
mc.setBlock(x+1,y-1,z,20)
mc.setBlock(x+2,y-1,z,20)
mc.setBlock(x,y-1,z-1,20)
mc.setBlock(x+2,y-1,z-1,20)
mc.setBlock(x,y-1,z-2,20)
mc.setBlock(x+1,y-1,z-2,20)
mc.setBlock(x+2,y-1,z-2,20)
