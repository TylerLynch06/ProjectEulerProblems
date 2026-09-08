import time

##Final key is p

file = open("Data//XOR.txt","r")
keys = file.readline()
keys = keys.split(",")
file.close()


exceptions = [40,41,33,45,39,63,59,58,32,44,46,34,96,37,38,47,43]

keycode = {}

def validKey(xor):
    return (xor>=48 and xor<=57) or (xor>=65 and xor<=90) or (xor>=97 and xor<=122) or xor in exceptions

print(validKey(62))

for key in keys:
    char = int(key)
    if char in keycode.keys():
        keycode[char]+=1
    else:
        keycode.update({char:1})

code = 97
while code<=122:
    valid=True
    for i in range(1,1455,3):
        xor = int(keys[i]) ^ code
        if not validKey(xor):
            valid=False
            break
    if valid ==True: print(code)
    code+=1

##greatestKey = [0,0]
##for key in keycode.keys():
##    if keycode[key]>greatestKey[1] and keycode[key]<107:
##        greatestKey[0],greatestKey[1]=key,keycode[key]
##
print(keys[64])
sum=0 
for i in range(0,1455,3):
    #print(chr(int(keys[i])^101),end="")
    #print(chr(int(keys[i+1])^120),end="")
    #print(chr(int(keys[i+2])^112),end="")
    sum+=(int(keys[i])^101)+(int(keys[i+1])^120)+(int(keys[i+2])^112)
print(f"\n{sum}")
##print(keycode)
