S = "loveleetcode" 
C = 'e'
dict1 = {}
arr1 = []
list1 = list(S)

for i in range(0,len(S)):
    if S[i] == 'e':
       arr1.append(i)


print(arr1)
arr3 = []
arr4 = []
for i in range(0,len(S)):
    arr4 = []
    for elem in arr1:
        arr4.append(abs(elem-i))

    arr3.append(arr4)
arr5 = []
for lst in arr3:
    arr5.append(min(lst))

print(arr5)
