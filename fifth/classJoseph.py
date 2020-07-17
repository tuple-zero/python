class Josephus(object):

    def __init__(self):
        self._people = []
        self._start = 1
        self._move = self._start - 1

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._people) > 1:
            return self._people.pop(self.pop_index())
        else:
            self._iter = 0
            raise StopIteration

    def pop_index(self):
        self._move = (self._move + self._step - 1) % len(self._people)
        return self._move

    def in_people(self,people_list):
        for person in people_list:
            self._people.append(person)
        return self._people

    def set_step(self,step):
        self._step = step

    def set_start(self,start):
        self._start = start

    def get_success_person(self):
        return self._people[0]