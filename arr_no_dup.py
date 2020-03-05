#arr = [4,6,2,1,1,6,2,5,5,4,3]
#arr = [4,4,2,2,1,1,3,3,6]
#arr = [4,1,2,1,2]
#arr = [4,4,3]
arr = [17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]
n = len(arr)-1
i = n/2-2
j = n/2+2

while(1):
   n = len(arr)-1
   print(n)
   if len(arr) == 1:
       break
   else:
      

       nl = int(n/2)-1
       nr = int(n/2)+1
       nmid = int(n/2)
       i = nl-1
       j = nr+1

       arr_l = arr[nl]
       arr_r = arr[nr]
       arr_mid = arr[int(n/2)]
       if arr_l == arr_r:
         
          arr.pop(nr)
          arr.pop(nl)
          print(arr)      
   
       elif arr_l == arr_mid:
        
          arr.pop(nmid)
          arr.pop(nl)
          print(arr)
          
       elif arr_r == arr_mid:
          arr.pop(nr)
          arr.pop(nmid)
          
       elif arr[i] == arr_l:
          arr.pop(nl)
          arr.pop(i)
          print(arr)

       elif arr[j] == arr_l:
          arr.pop(j)
          arr.pop(nl)

       elif arr[i] == arr_mid:
          arr.pop(nmid)
          arr.pop(i)

       elif arr[j] == arr_mid:
          arr.pop(j)
          arr.pop(nmid)
       
       elif arr[i] == arr_r:
          arr.pop(nr)
          arr.pop(i)
   
       elif arr[j] == arr_r:
          arr.pop(j)
          arr.pop(nr)
 
       else:
          i = i - 1
          j = j + 1

print(arr)
