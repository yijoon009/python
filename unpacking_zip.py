ex = ([1,2],[3,4],[5,6],[5,6],[5,6])

# 위 ex는 튜플로 값이 1라 zip을 바로 해버리면 적용이 안된다.
for value in zip(ex):
    print(value)

for value in zip(*ex):
    print(value)

