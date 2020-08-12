# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:55:45 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
import random
"""
while True:
    hits = mc.events.pollBlockHits()
    if len(hits) >0:
        hit = hits[0]
        x,y,z = hit.pos.x, hit.pos.y,hit.pos.z
        mc.setBlock(x,y,z,46)
        block = mc.getBlock(x,y,z)
        mc.postToChat("恭喜你獵到了"+str(block))

x,y,z = mc.player.getPos()
while True:
    x = x + random.uniform(-20,20)
    z = z + random.uniform(-20,20)
    y = y + 5
   
    mc.spawnEntity(x,y,z,20)
    mc.spawnEntity(x,y,z,20)
    mc.spawnEntity(x,y,z,20)
    mc.spawnEntity(x,y,z,20)
    mc.spawnEntity(x,y,z,20)
    mc.spawnEntity(x,y,z,20)
    mc.spawnEntity(x,y,z,20)
    mc.spawnEntity(x,y,z,20)
    mc.spawnEntity(x,y,z,20)
    mc.spawnEntity(x,y,z,20)
    mc.spawnEntity(x,y,z,20)
    mc.spawnEntity(x,y,z,20)
    time.sleep(0.1)

x,y,z = mc.player.getPos()

for i in range(20):
    mc.setBlock(x+i,y-1,z+i,41)

def plantTree(x,y,z):
    print(x)
    print(y)
    print(z)
    
plantTree("save the earth", "I am y", 0)

mc=Minecraft.create()
"""

def plantTree (x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,18)
    mc.setBlocks(x,y,z,x,y+4,z,17)
    
for i in range(10):
    plantTree (x + i,y,z)
                 

    
    
    
    
    
    
        
    
    


























                   