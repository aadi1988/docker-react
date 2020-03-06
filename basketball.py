B = ["5","-2","4","C","C","D","+","+"]
#B = ["5","2","C","D","+"]
sum = 0

round_points = []

for i,elem in enumerate(B):
    if elem != 'C' and elem != 'D' and elem != '+':
            round_points.append(int(elem))
    elif elem == 'C':
            round_points.pop(-1)
    elif elem == 'D':
         print(round_points)
         print(i)
         round_points.append(round_points[-1] * 2)
    elif elem == '+':
         round_points.append(round_points[-2] + round_points[-1])
    else:
         continue

print(round_points)

for elem in round_points:
    sum += elem

print(sum)
