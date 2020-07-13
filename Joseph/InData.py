import Joseph.Person as p


def get_input():
    out_rule = int(input("请输入相应的规则："))
    out_start_num = int(input("请输入相应的开始位置："))
    return out_rule,out_start_num


def show_list(jo):
    print("淘汰列表：")
    print("姓名\t性别\t年龄\t电话号码")
    print(jo)


def get_success_person(jo):
    person = jo.people[p.PersonInfo.count-1]
    print("最后胜利的人是：%s" % person.get_name())
    print("具体信息为：")
    print(person)