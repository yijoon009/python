# a = {1,2,3,4,5}
# print(type(a))

# s = {2,3}
# print(s)

# s.add(1)
# print(s)

# s.add(1)
# print(s)

# s.remove(1)
# print(s)

# s.update({1,4,5,6,10})
# print(s)

# s.discard(6)
# print(s)

# s.clear()

s1 = set([1,2,3,4,5])
s2 = set([3,4,5,6,7])

print(s1.union(s2))     # s1과 s2의 합집합
print(s1 | s2)     # s1과 s2의 합집합

print(s1.intersection(s2))      # s1과 s2의 교집합
print(s1 & s2)     # s1과 s2의 교집합

print(s1.difference(s2))      # s1과 s2의 차집합
print(s1 - s2)     # s1과 s2의 차집합