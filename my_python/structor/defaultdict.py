from collections import defaultdict

d = defaultdict(object)         # default dectionary를 생성
d = defaultdict(lambda: 0)      # default 값을 0으로 설정
print(d["first"])