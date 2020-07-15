def get_input():
    out_rule = int(input("请输入相应的规则："))
    out_start_num = int(input("请输入相应的开始位置："))
    return out_rule,out_start_num


def show_list(in_list):
    print("列表：")
    print("姓名\t性别\t年龄\t电话号码")
    for x in in_list:
        print(x)


def show_out_list(in_list):
    print("淘汰列表：")
    print("姓名\t性别\t年龄\t电话号码")
    for x in in_list:
        if in_list.index(x) == len(in_list)-1:
            break
        print(x)