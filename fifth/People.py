class PersonInfo(object):
    count = 0

    def __init__(self, name, gender, age, number):
        self._name = name
        self._gender = gender
        self._age = age
        self._number = number

    def __str__(self):
        gender = '无'
        if self._gender == 0:
            gender = '女'
        if self._gender == 1:
            gender = '男'
        return "%s\t  %s\t  %d\t %d" % (self._name, gender,self._age,self._number)

    def get_name(self):
        return self._name