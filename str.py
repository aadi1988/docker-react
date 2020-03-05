s = 'abcd'
t = 'abcde'

final_s = 0
final_t = 0

for i in s:
    final_s += ord(i)

for i in t:
    final_t += ord(i)

print(chr(final_t-final_s))
