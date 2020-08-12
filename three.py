# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:55:45 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
import random
mc=Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()
    if len(hits) >0:
        hit = hits[0]
        x,y,z = hit.pos.x, hit.pos.y,hit.pos.z
        mc.setBlock(x,y,z,46)
        block = mc.getBlock()
        mc.postToChat("恭喜你獵到了"+str(block))