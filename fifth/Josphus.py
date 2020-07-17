class Josephus(object):

    def __init__(self):
        self._people = []
        self._step = 1
        self._start = 1

    def __iter__(self):
        self._iter = 0
        self._move = self._start - 1
        return self

    def __next__(self):
        self._iter += 1
        if len(self._people) > 1:
            if self._move == len(self._people):
                self._move = 0
            if self._iter == self._step:
                self._iter = 0
                return self._people.pop(self._move)
            else:
                self._move += 1
        else:
            self._iter = 0
            raise StopIteration

    def in_people(self,people_list):
        for person in people_list:
            self._people.append(person)
        return self._people

    def set_step(self,step):
        self._step = step

    def set_start(self,start):
        if start < 1:
            return
        self._start = start

    def get_success_person(self):
        return self._people[0]