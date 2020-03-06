stones = [8,1,1,1,1]

while(1): 
  
     if len(stones) == 1 or len(stones) == 0: 
        break
     else:
        max1 = max(stones)
        print(stones)
        stones.remove(max1)
        s_max = max(stones)
        stones.remove(s_max)
        if max1 > s_max:
           stones.append(max1-s_max)
        

print(stones)
