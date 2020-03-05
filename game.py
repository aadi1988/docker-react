#widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
#S = "abcdefghijklmnopqrstuvwxyz"

widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "bbbcccdddaaaa"

dict1 = {}
x = 97
for elem in widths:
    dict1[str(chr(x))] = elem
    x = x+1

print(dict1)
cnt = 0
line = 1
for i in S:
    if cnt + dict1[i] <= 100:
       cnt += dict1[i]
    else:
       cnt = dict1[i]
       line += 1

print(cnt)
print(line)
