class PersonInfo(object):
    count = 0

    def __init__(self, name, gender, age, number):
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__number = number

    def __str__(self):
        return "%s\t  %s\t  %d\t" % (self.__name, self.__gender,self.__age,self.__number)

    def get_name(self):
        return self.__name


def get_input():
    the_num = 0
    out_num = 0
    out_start_num = 0
    while the_num <= 0 or out_num <= 0 or the_num < out_start_num or out_start_num <= 0 or out_start_num > the_num:
        the_num = int(input("请确认玩游戏的总人数："))
        out_num = int(input("请输入游戏的相应规则："))
        out_start_num = int(input("请确认开始的编号："))
    return the_num, out_num, out_start_num


def verify_information(in_name,in_gender,in_age,in_number):
    if len(in_name) > 0 and 6 > len(in_gender) > 0 and 100 > in_age > 12 and len(in_number) == 11:
        return True
    return False


def show_error_information(in_name,in_gender,in_age,in_number):
    result = ""
    if len(in_name) == 0:
        result += "名字不能为空！\n"
    if len(in_gender) <= 0 or len(in_gender) > 5:
        result += "性别输入错误！\n"
    if in_age < 12 or in_age >= 100:
        result += "年龄输入错误！"
    if len(in_number) != 11:
        result += "电话号码格式错误！"
    return result


def get_information():
    """
    判断一个人的个人信息
    :return: 一个人的个人信息
    """
    name = input("请输入姓名：")
    gender = input("请输入性别：")
    age = int(input("请输入年龄："))
    number = input("请输入电话号码：")
    if verify_information(name,gender,age,number):
        person = PersonInfo(name,gender,age,number)
        return person
    else:
        show_error_information(name, gender, age, number)
        return False


def get_people_info(in_num):
    out_list = []
    while in_num > 0:
        people = get_information()
        if people:
            out_list.append(people)
            in_num -= 1
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


def get_success_person(in_list):
    person = in_list[:-1]
    print("最后胜利的人是：%s" % person.get_name())
    print("具体信息为：")
    print(in_list[len(in_list)-1])


def show_people_info(in_list):
    print("姓名\t性别\t年龄\t电话号码")
    for x in in_list:
        print(x)


people_num, rule, start_num = get_input()
assert (get_input() == 3)
people_list = get_people_info(people_num)
out_people = out_circle(people_list, rule, start_num)
assert (out_people == [1])
show_people_info(out_people)
get_success_person(out_people)