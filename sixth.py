# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 14:31:55 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()


time.sleep(1)
x,y,z = mc.player.getTilePos()

while True:
    mc.executeCommand("weather clear")
    time.sleep(5)
    mc.executeCommand("weather rain")
    time.sleep(5)