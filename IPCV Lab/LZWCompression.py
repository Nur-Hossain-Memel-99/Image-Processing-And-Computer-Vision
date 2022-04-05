# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:29:57 2020

@author: Arifur Rahaman
"""
string = "BABAABAAA"
print(string)
#string = "ABB"
#string = input("enter a string = ")
#string = "ABCAA"
dictionary = {chr(i):i for i in range(0,256)}
#dictionary ={'A':65,'B':66,'BA':256}
#string = "ababbabcababba"
#dictionary = {'a':1,'b':2, 'c':3}
last = 256
p = ""
result = []
 
for c in string:
	pc = p+c
	if pc in dictionary:
		p = pc
	else:
		result.append(dictionary[p])
		#print(dictionary[p])
		dictionary[pc] = last
		last = last + 1
		p = c
 
if p != '':
	result.append(dictionary[p])
    
print(result)
#for i in range(len(result)):
#  print(chr(result[i]),"=",(result[i]))