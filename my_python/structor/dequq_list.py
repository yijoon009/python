from collections import deque
import time

# deque
# 높은 해상도의 타이머 사용
start_time = time.perf_counter()
deque_list = deque()

# Stack
for i in range(10000):
    for j in range(10000):
        deque_list.append(i)
        deque_list.pop()

# 경과 시간 계산 및 출력
end_time = time.perf_counter()
print(end_time - start_time, "seconds")

start_time = time.perf_counter()

just_list = []
for i in range(10000):
    for j in range(10000):
        just_list.append(i)
        just_list.pop()

end_time = time.perf_counter()
print(end_time - start_time, "seconds")
