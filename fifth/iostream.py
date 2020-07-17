def in_info():
    out_rule = int(input("请输入游戏的相应规则："))
    out_start = int(input("请确认开始的编号："))
    return out_rule,out_start


def in_verification(in_rule,in_start,in_num):
    while in_num < in_start:
        in_rule,in_start = in_info()
    return in_rule,in_start


def out_people(joseph):
    print("淘汰顺序如下所示：")
    print("姓名\t性别\t年龄\t电话号码")
    for person in joseph:
        if person != None:
            print(person)


def out_success_person(joseph):
    person = joseph.get_success_person()
    print("最后胜利的人是： %s" % person.get_name())
    print("具体信息如下：")
    print(person)