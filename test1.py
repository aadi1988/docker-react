#arr1 = [40,11,26,27,-20]
arr1 = [4,2,1,3]
#arr1 = [1,3,6,10,15]
#arr1 = [3,8,-10,23,19,-4,-14,27]
#arr1 = [2,3]
#arr1 = [-169,-133,178,-50,-4,138,136,-140,137,69,8,-80,3,183,-57,164,192,191]
#arr1 = [-17,46,63,81,-101,-91,121,-2,112,-15,-65,-96,6,-139]
arr1 = sorted(arr1)

print(arr1)

min = 2147483647
dict1 = {}
arr2 = []
arr3 = [0] * (len(arr1)-1)
for i in range(0,len(arr1)-1):
    var = arr1[i+1] - arr1[i]
    if var == min:
       arr2.append([arr1[i],arr1[i+1]])
    elif var < min:
       arr3[0] = [arr1[i],arr1[i+1]]
       min = var
       arr2 = []
    else:
       continue

print(arr2)
print(arr3)

#if len(arr2) > 0:
if len(arr2) > 0:
   if (arr3[0][1] - arr3[0][0] < arr2[0][1] - arr2[0][0]):
       print(arr3[0])
   else:
       print([arr3[0]] + arr2)
else:
   print(arr3[0])
