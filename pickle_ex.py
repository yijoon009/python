import pickle

# f = open('list.pickle', 'wb')  # pickle은 파이썬에 특화된 바이너리 파일
# test = [1,2,3,4,5]
# pickle.dump(test, f)
# f.close


# del test

# print(test)


f = open('list.pickle', 'rb')
test_pickle = pickle.load(f)
print(test_pickle)
f.close