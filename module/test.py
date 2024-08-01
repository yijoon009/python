
# module1.py 안에 있는 Module1 Class를 가져온다.
from module1 import Module1
from module2 import Module2

test = Module1('yijun')
test2 = Module2(3, 5,45,6,7,1)
test.print_name()
print(test2.sum_numbers()) # 8이 출력됨.