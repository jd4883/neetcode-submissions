a, b, c, d = False, False, True, True

p1 = a or b
p2 = b or c
p3 = c or d
p4 = (a or b or c) and d

print(p1)
print(p2)
print(p3)
print(p4)