class PersonInfo:
    """
    个人信息类
    """
    def __init__(self, name, gender, age):
        """
        构造函数
        :param name: 姓名
        :param gender: 性别
        :param age: 年龄
        """
        self.__name = name
        self.__gender = gender
        self.__age = age

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender

    def set_age(self, age):
        self.__age = age

    def __str__(self):
        return "%s\t  %s\t  %d" % (self.__name, self.__gender,self.__age)


def show_person(in_list):
    print("姓名\t性别\t年龄")
    for i in in_list:
        print(i)


def show_out(in_list):
    in_len = len(in_list)
    print("淘汰的顺序是：")
    print("姓名", "\t", "性别", "\t", "年龄")
    for i in range(0,in_len):
        if i == (in_len-1):
            print("最后留下来的人是: %s" % in_list[i].get_name())
            print("具体信息显示:", end=" ")
            print(in_list[i])
            break
        print(in_list[i])

def out_circle(in_list, in_num, start_index=1):
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


def get_people():
    person_one = PersonInfo("小红", "女", 12)
    person_two = PersonInfo("小黑", "男", 10)
    person_three = PersonInfo("小李", "男", 19)
    person_four = PersonInfo("小白", "女", 15)
    person_five = PersonInfo("小明", "男", 17)
    person_six = PersonInfo("小金", "女", 18)
    person_seven = PersonInfo("小智", "女", 18)
    person_eight = PersonInfo("小妮", "女", 10)
    person_nine = PersonInfo("张三", "男", 12)
    person_ten = PersonInfo("李四", "男", 10)
    person_eleven = PersonInfo("王五", "男", 19)
    person_twelve = PersonInfo("王麻子", "男", 10)
    out_list = [person_one, person_two, person_three, person_four, person_five, person_six, person_seven, person_eight,
                person_nine, person_ten, person_eleven, person_twelve]

    return out_list

test_list = get_people()
show_person(test_list)
test_out = out_circle(test_list, 4, 1)
show_out(test_out)