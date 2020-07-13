class Josephus(object):
    def __init__(self):
        self.people = []

    def add_joseph(self,person):
        self.people.append(person)

    def __str__(self):
        for x in self.people:
            print(x)