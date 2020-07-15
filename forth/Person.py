class PersonInfo(object):
    count = 0

    def __init__(self, name, gender, age, number):
        self._name = name
        self._gender = gender
        self._age = age
        self._number = number
        PersonInfo.count += 1

    def __str__(self):
        sex = '男'
        if self._gender == 0:
            sex = '女'
        return "%s\t  %s\t  %d\t %s" % (self._name, sex, self._age, self._number)

    def get_name(self):
        return self._name