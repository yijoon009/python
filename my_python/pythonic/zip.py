alist = ['a1', 'a2','a3']
blist = ['b1', 'b2','b3']
clist = ['c1', 'c2','c3']

# print([[a, b, c] for a, b, c in zip(alist, blist, clist)])
# print([c for c in zip(alist, blist, clist)])

math = (100,90,80)
kor = (90,90,70)
eng = (90,80,79)

print([sum(value) / 3 for value in zip(math, kor, eng)])