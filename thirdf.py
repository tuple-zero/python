class PersonInfo(object):
    count = 0

    def __init__(self, name, gender, age, number):
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__number = number
        self.count += 1

    def __str__(self):
        return "%s\t  %s\t  %s\t %s" % (self.__name, self.__gender,self.__age,self.__number)

    def get_name(self):
        return self.__name


def open_file():
    out_list = []
    out_file = open("test.txt", "r",encoding='utf-8')
    for line in out_file:
        person_list = line.split()
        person = PersonInfo(person_list[0],person_list[1],person_list[2],person_list[3])
        out_list.append(person)
    return out_list


def out_circle(in_list, in_num, start_index=1):
    """
    :param in_list:人物信息输入
    :param in_num:游戏规则
    :param start_index:开始位置
    :return: 返回淘汰的顺序
    """
    out_list = []
    in_len = len(in_list)
    count = 0
    move = start_index - 1
    index = 0

    while in_len > 0:
        count += 1
        if move == in_len:
            move = 0
        if count == in_num:
            index += 1
            out_list.append(in_list.pop(move))
            count = 0
            move -= 1
            in_len -= 1
        move += 1
    return out_list


def show_list(in_list):
    print("淘汰列表：")
    print("姓名\t性别\t年龄\t电话号码")
    for x in in_list:
        if in_list.index(x) == len(in_list)-1:
            break
        print(x)


def get_success_person(in_list):
    person = in_list[len(in_list)-1]
    print("最后胜利的人是：%s" % person.get_name())
    print("具体信息为：")
    print(person)


people_list = open_file()
show_list(people_list)
out_people = out_circle(people_list, 4, 1)
show_list(out_people)
get_success_person(out_people)