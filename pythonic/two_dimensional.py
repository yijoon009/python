import pprint

# words = "The quick brown fox jumps over the lazy dog".split()
# pprint.pprint([[w.upper(), w.lower(), len(w)] for w in words]) 


case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]
result = [i+j for i in case_1 for j in case_2]
print(result)
result = [[i+j for i in case_1] for j in case_2]    # for j in case_2 먼저 실행
print(result)
