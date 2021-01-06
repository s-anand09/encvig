# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 02:57:22 2021

@author: shrey
"""
from Sb_ch import *
encrypt=input("Input the encrypted text: ")
key=input("Input the key: ")
lkey=len(key)
j=0
for i in range(lkey,len(encrypt)):
    if j==len(key):
        j=0
    key=key+key[j]
    j=j+1

def decrypt(enc,keyf,sB,ch):
    msg=""
    for i in range(0, len(enc)):
        x=enc[i]
        y=keyf[i] 
        y1=ch.index(y)
        x1=sB[y1].index(x)
        msg=msg+ch[x1]        
    return msg

decrypt1=decrypt(encrypt,key,sBox,chararray)
decrypt2=decrypt(decrypt1,key,sBox,chararray)
decrypt3=decrypt(decrypt2,key,sBox,chararray)
msg_final=decrypt(decrypt3,key,sBox,chararray)
    
print(msg_final)