# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 14:18:11 2021

@author: shrey
"""
from Sb_ch import *
import base64

fname=input("Enter the filename to be encoded : ")
with open(fname, "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
final_string=my_string.decode('utf-8')

msg=final_string
key=input("Input the key: ")
lkey=len(key)
j=0
for i in range(lkey,len(msg)):
    if j==len(key):
        j=0
    key=key+key[j]
    j=j+1

def encrypt(messagef,keyf,sB,ch):
    final=""
    for i in range(0, len(messagef)):
        x=messagef[i]
        y=keyf[i]
        x1=ch.index(x)
        y1=ch.index(y)
        final=final+sB[y1][x1]
    return final
    
encrypt1=encrypt(msg,key,sBox,chararray)
encrypt2=encrypt(encrypt1,key,sBox,chararray)
encrypt3=encrypt(encrypt2,key,sBox,chararray)
encrypt_final=encrypt(encrypt3,key,sBox,chararray)

name=input("Name of encrypted file : ")
file2 = open((name+".txt"),"w") 
file2.write(encrypt_final)  
file2.close()
