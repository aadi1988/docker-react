arr = [0,2,1,0]
m = 0
for i,elem in enumerate(arr):
    if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
           m = i 


print(m)      
