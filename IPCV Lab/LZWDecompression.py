dictionary = {i:chr(i) for i in range(0,256)}
last = 256
#ababbabcababba
arr = [97, 98, 256, 257, 98, 99, 256, 258, 97]
#BABAABAAA
result = []
p = arr.pop(0)
result.append(dictionary[p])
for c in arr:
    if c in dictionary:
        entry = dictionary[c]
        #print(entry)
        result.append(entry)
        print(entry,":",entry[0])
        dictionary[last] = dictionary[p] + entry[0]
        last += 1
        p = c
print(''.join(result))