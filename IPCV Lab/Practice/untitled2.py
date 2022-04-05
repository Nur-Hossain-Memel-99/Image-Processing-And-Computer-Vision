string = "BABAABAAA"
#string = "ABCAA"
dictionary = {chr(i):i for i in range(0,256)}
#{'A':65,'B':66}
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
		print(p,"=",dictionary[p])
		dictionary[pc] = last
		last = last + 1
		p = c
 
if p != '':
	result.append(dictionary[p])
 
#print(result)