def solution(my_string, overwrite_string, s):
    before_str = my_string[:s]
    after_str = my_string[s+len(overwrite_string):]
    return before_str+overwrite_string+after_str