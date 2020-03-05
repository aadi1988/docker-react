#arr = [1,0,0,0]
arr = [1,0,0,0,1,0,0]
n = 2
cnt_ins = 0
i=0
while i < len(arr):
      if arr[i] == 0:
         if i+1 < len(arr):
            if arr[i-1] == 0 and arr[i+1] == 0:
                  arr[i] = 1
                  cnt_ins += 1

      i+=1
print(arr)
print(cnt_ins)
