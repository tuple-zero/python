import forth.Person as person
import forth.Joseph as joseph
import forth.Fileopen as fp
import forth.InData as ind


def test_iter(people_list):
    test_joseph = joseph.Josephus()
    test_joseph.add_joseph(people_list)
    for x in test_joseph:
        print(x)

people_list = fp.open_file()
ind.show_list(people_list)
rule, start_num = ind.get_input()

while start_num > person.PersonInfo.count or start_num < 1:
    print("开始编号输入错误，请输入小于%d的开始下标,大于0的下标：" % person.PersonInfo.count)
    rule, start_num = ind.get_input()

joseph_test = joseph.Josephus()
joseph_test.add_joseph(people_list)
#测试迭代器
test_iter(people_list)

assert (len(joseph_test.people) == len(people_list))
joseph_test.step = rule
joseph_test.start = start_num
joseph_test.get_out_list()
assert (len(joseph_test.out_people) == len(people_list))
joseph_test.show_out_list()
joseph_test.get_success_people()