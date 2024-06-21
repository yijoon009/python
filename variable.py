# def kwards_test_1(**kwards):
# 	print(kwards)
# 	print(type(kwards))

# kwards_test_1(first=3, second=5, third=2)


def kwards_test_3(one, two=3, *args, **kwrds):
	print(one+two+sum(args))
	print(args)
	print(kwrds)
	
#5,6,7,8,9가 *args에 들어가고 나머지 first, second, third가 kwrds에 들어간다
print(kwards_test_3(3,4,5,6,7,8,9,first=3, second=4, third=6))  

print(kwards_test_3(10,30,3,5,6,first=3, second=5, third=10))