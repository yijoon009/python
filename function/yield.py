import sys

def generator_list(value) :
    result = []
    for i in range(value):
        # yield i
        result.append(i)
    return result


result = generator_list(50)

print(sys.getsizeof(result))