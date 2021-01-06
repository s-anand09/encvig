import random
chararray = []
sBox = []
for i in range(0, 26):
    chararray.append(chr(ord('a')+i))

for i in range(0, 26):
    chararray.append(chr(ord('A')+i))

for i in range(0, 10):
    chararray.append(str(i))

chararray=chararray+['#','!','_','-','@','%',' ','.',',',':',';','(',')','{','}','[',']','+']

for i in range(0, len(chararray)):
    temp = []
    for j in range(0, len(chararray)):
        temp.append(chararray[j])
    temp2=[]
    while len(temp)>0:
        x=random.randrange(0,len(temp))
        temp2.append(temp[x])
        temp.pop(x)
    sBox.append(temp2)
    
file2 = open("Sbox.txt","w") 
file2.write(str(sBox))  
file2.close()
    
file3 = open("chararray.txt","w") 
file3.write(str(chararray))  
file3.close()

# msg=input("Input the message: ")
# key=input("Input the key: ")
# lkey=len(key)
# j=0
# for i in range(lkey,len(msg)):
#     if j==len(key):
#         j=0
#     key=key+key[j]
#     j=j+1
    
# final=""
# for i in range(0, len(msg)):
#     x=msg[i]
#     y=key[i]
#     j=0
#     for each in chararray:
#         if each==x:
#             x1=j
#         j=j+1
#     j=0
#     for each in chararray:
#         if each==y:
#             y1=j
#         j=j+1
#     final=final+sBox[x1][y1]

# print(final)
    
    