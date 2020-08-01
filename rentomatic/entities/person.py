class Person(object):
    count = 0

    def __init__(self, name: str, gender: int, age: int, number: int):
        self._name = name
        if gender == '女':
            self._gender = 0
        if gender == '男':
            self._gender = 1
        if int(age) < 0:
            self._age = 0
        else:
            self._age = int(age)
        self._number = int(number)

    def __str__(self):
        gender = '无'
        if self._gender == 0:
            gender: str = '女'
        if self._gender == 1:
            gender = '男'
        return "%s\t  %s\t  %d\t %d" % (self._name, gender,self._age,self._number)

    def get_name(self):
        return self._name

    def __eq__(self, other):
        return self._name == other._name and self._gender == other._gender and self._age == other._age and self._number == other._number