word = input('enter your word: ')
word_list = list(word)
# print(word_list)

for i in range(len(word_list)):
    print(word_list.pop())
    print(word_list)
