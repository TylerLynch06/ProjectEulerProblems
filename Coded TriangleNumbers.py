import os
import sys

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def decodeAlpha(char):
    return alphabet.index(char.lower())+1

def isTriangleNum(num):
    n = ((2*num)+(0.25))**0.5-(0.5)
    print(n)
    return str(n).split(".")[-1] == "0"
        
    
    

print(isTriangleNum(3))

file = open("Data\\0042_words.txt","r")
words = file.read()
words = words.split(",")
words = [word.split('"')[1] for word in words]
print(words)
triangleWords = 0
for word in words:
    wordSum = 0
    for char in word:
        wordSum+=decodeAlpha(char)
    if isTriangleNum(wordSum): triangleWords+=1
print(triangleWords)
