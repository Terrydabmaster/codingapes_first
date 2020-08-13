# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 09:26:23 2020

@author: USER
"""
from mcpi.minecraft import Minecraft

mc=Minecraft.create()

x,y,z = mc.player.getTilePos()



line1 = []
line2 = []
line3 = []
line4 = []
line5 = []
line6 = []
line7 = []
line8 = []
line9 = []



for i in range (1,10):
    line1.append(1*i)
    
for i in range(1,10):
    line2.append(2*i)
    
for i in range(1,10):
    line3.append(3*i)
    
for i in range (1,10):
    line4.append(4*i)
    
for i in range(1,10):
    line5.append(5*i)
    
for i in range(1,10):
    line6.append(6*i)
    
for i in range (1,10):
    line7.append(7*i)
    
for i in range(1,10):
    line8.append(8*i)
    
for i in range(1,10):
    line9.append(9*i)
    
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7)
print(line8)
print(line9)

mc.setSign(x,y,z,63,0,str(line1),str(line2),str(line3))
mc.setSign(x,y,z,63,0,str(line4),str(line5),str(line6))
mc.setSign(x,y,z,63,0,(line7),str(line8),str(line9))

















                