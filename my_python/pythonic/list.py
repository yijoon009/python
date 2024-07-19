# result = [i for i in range(10)]
# print(result)

# result = [i for i in range(10) if i % 2 == 0]
# print(result)

# word_1 = "Hello"
# word_2 = "World"

# result = [i+j for i in word_1 for j in word_2]
# print(result)

case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]
# result = [i+j for i in case_1 for j in case_2]
# result = [i+j for i in case_1 for j in case_2 if not (i==j)]
result = [i+j if not (i==j) else 'EEE' for i in case_1 for j in case_2]

print(result)