class Josephus(object):

    def __init__(self):
        self.people = []
        self.out_people = []
        self.step = 0
        self.start = 1

    def add_joseph(self, person):
        self.people.append(person)

    def add_joseph(self, people_list):
        for x in people_list:
            self.people.append(x)

    def get_out_list(self):
        count = 0
        move = 0
        while len(self.people) > 0:
            count += 1
            if len(self.people) == move:
                move = 0
            if count == self.step:
                self.out_people.append(self.people.pop(move))
                count = 0
            else:
                move += 1

    def show_out_list(self):
        print("淘汰列表：")
        print("姓名\t性别\t年龄\t电话号码")
        for x in self.out_people:
            if self.out_people.index(x) == len(self.out_people) - 1:
                break
            print(x)

    def get_success_people(self):
        person = self.out_people[len(self.out_people) - 1]
        print("最后胜利的人是：%s" % person.get_name())
        print("具体信息为：")
        print(person)