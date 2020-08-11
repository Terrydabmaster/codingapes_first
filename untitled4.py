# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 14:13:16 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
import random
mc=Minecraft.create()
 
time.sleep(1)


x,y,z = mc.player.getTilePos()
"""
while True:
    colour=random.randrange(0,16)
    mc.setBlocks(x+25,y-1,z+25,x-25,y-1,z-25,95,colour)                    
    time.sleep(0.5)
"""
"""
wallet_a = random.randrange(0,100)

wallet_b = random.randrange(0,100)

if wallet_a == 50 or wallet_b == 80:
    print ("50or80")
    
total = wallet_a + wallet_b


if total>130:
    print("yes")
    
print(wallet_a)
print(wallet_b)
 """ 
try:
    blockType = int(input("Block id:"))
    mc.setBlock(x,y,z, blockType)   
except:
    print("Invild")

 

            
    
           