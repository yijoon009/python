class SoccerPlayer(object):
    # 속성 정보
    def __init__(self, name: str, position: str, back_number: int):
        self.name = name
        self.position = position
        self.back_number = back_number

    def __str__(self):
        return "hello, my name is %s. my back number is %d." % (self.name, self.back_number)

    def __add__(self, other):
        return self.name + other.name

    def change_back_number(self, new_number):
        print('선수의 등번호를 변경합니다. from %d to %d' % (self.back_number, new_number))
        self.back_number = new_number

park = SoccerPlayer('park', 'wf', 13)
son = SoccerPlayer('son', 'fw', 7)
print(park)
print(park+son)

son.change_back_number(100)
print(son)

