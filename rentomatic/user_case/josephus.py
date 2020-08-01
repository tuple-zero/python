from rentomatic.entities.person import Person


class Josephus:

    def __init__(self, reader):
        self._start = 1
        self._step = 1
        self._move = self._start - 1
        self._people = []
        self.append(reader)

    def append(self,reader):
        if reader:
            for person in reader:
                if person:
                    self._people.append(person)

    def set_step(self,step: int):
        self._step = step

    def set_start(self,start: int):
        self._start = start

    def pop_index(self) -> int:
        self._move = (self._move + self._step - 1) % len(self._people)
        return self._move

    def pop(self, index: int):
        self._people.pop(index)

    def __iter__(self):
        return self

    def __next__(self) -> Person:
        if len(self._people) > 1:
            return self._people.pop(self.pop_index())
        else:
            self._iter = 0
            raise StopIteration

    def get_people(self) -> Person:
        if len(self._people) == 1:
            return self._people[0]
        return self._people