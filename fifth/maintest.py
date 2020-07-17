import fifth.Josphus as jo
import fifth.opentxt as file
import fifth.iostream as ios
import fifth.classJoseph as cjo


def test_success_func():

    test_list = [1, 2, 3]
    test_jo = jo.Josephus()
    test_jo.set_step(3)
    test_jo.set_start(1)
    test_jo.in_people(test_list)
    for i in test_jo:
        pass
    result = test_jo.get_success_person()
    assert result == 2


def test_out_list():
    out_list = []
    test_list = [1, 2, 3]
    test_jo = jo.Josephus()
    test_jo.set_step(3)
    test_jo.set_start(1)
    test_jo.in_people(test_list)
    for i in test_jo:
        if i:
            out_list.append(i)
    out_list.append(test_jo.get_success_person())
    assert out_list == [3, 1, 2]


#测试部分
test_success_func()
test_out_list()

test_num = 1
if test_num == 0:
    people_list = file.open_file_method('test.zip')
    for person in people_list:
        print(person)
    rule, start = ios.in_verification(0,len(people_list)+1,len(people_list))
    josephus = cjo.Josephus()
    jo_people = josephus.in_people(people_list)
    josephus.set_start(start)
    josephus.set_step(rule)
    ios.out_people(josephus)
    ios.out_success_person(josephus)

if test_num == 1:
    people_list = file.open_class_file_method('test.zip')
    for person in people_list:
        print(person)
    rule, start = ios.in_verification(0,len(people_list)+1,len(people_list))
    josephus = cjo.Josephus()
    jo_people = josephus.in_people(people_list)
    josephus.set_start(start)
    josephus.set_step(rule)
    ios.out_people(josephus)
    ios.out_success_person(josephus)