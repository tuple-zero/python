from rentomatic.entities.person import Person
from rentomatic.interface.interface import Interface


def test_get_reader(file_path,target_name,result):
    test_interface = Interface()
    test_interface.create_reader(file_path,target_name)
    test_interface.get_josephus()
    people_list = test_interface.get_people()
    assert people_list == result


def test_out_len_josephus(file_path,target_name,result, start=1,step=1):
    test_interface = Interface()
    test_interface.create_reader(file_path,target_name)
    test_interface.get_josephus()
    test_interface.set_step(step)
    test_interface.set_start(start)
    out_list = test_interface.out_people_list()
    assert len(out_list) == result


def test_out_josephus(file_path,target_name,result,start=1,step=1):
    test_interface = Interface()
    test_interface.create_reader(file_path, target_name)
    test_interface.get_josephus()
    test_interface.set_step(step)
    test_interface.set_start(start)
    out_list = test_interface.out_people_list()
    assert out_list == result


def test_success_name_josephus(file_path,target_name,result,start=1,step=1):
    test_interface = Interface()
    test_interface.create_reader(file_path, target_name)
    test_interface.get_josephus()
    test_interface.set_step(step)
    test_interface.set_start(start)
    test_interface.out_people_list()
    person_name = test_interface.get_success_person_name()
    assert person_name == result


def test_success_josephus(file_path,target_name,result,start=1,step=1):
    test_interface = Interface()
    test_interface.create_reader(file_path, target_name)
    test_interface.get_josephus()
    test_interface.set_step(step)
    test_interface.set_start(start)
    test_interface.out_people_list()
    person = test_interface.get_people()
    assert person == result


if __name__ == '__main__':
    result_csv = [
        Person('小红', '女', 12, 12345678901),
        Person('小黑', '男', 10, 12345678931),
        Person('小李', '男', 19, 12345678201),
        Person('小白', '女', 15, 12345678901),
        Person('小明', '男', 17, 12345678901),
        Person('小金', '女', 18, 12345678901),
        Person('小智', '女', 18, 12345678901),
        Person('小妮', '女', 10, 12345678901),
        Person('张三', '男', 12, 12345678901),
        Person('李四', '男', 10, 12345678901),
        Person('王五', '男', 19, 12345678901),
        Person('王麻子', '男', 16, 12345678901)
    ]
    result_txt = [
        Person('小红', '女', 12, 12345678912),
        Person('小黑', '男', 10, 12345678912),
        Person('小李', '男', 19, 12345678912),
        Person('小白', '女', 15, 12345678912),
        Person('小明', '男', 17, 12345678912),
        Person('小金', '女', 18, 12345678912),
        Person('小智', '女', 18, 12345678912),
        Person('小妮', '女', 10, 12345678912),
        Person('张三', '男', 12, 12345678912),
        Person('李四', '男', 10, 12345678912),
        Person('王五', '男', 19, 12345678912),
        Person('王麻子', '男', 10, 12345678912)
    ]
    test_get_reader('F:\\Python\\test\\test1.csv','', result_csv)
    test_get_reader('F:\\Python\\test\\test.txt', '', result_txt)
    test_out_len_josephus('F:\\Python\\test\\test1.csv','',11)
    result_csv = [
        Person('小红', '女', 12, 12345678901),
        Person('小黑', '男', 10, 12345678931),
        Person('小李', '男', 19, 12345678201),
        Person('小白', '女', 15, 12345678901),
        Person('小明', '男', 17, 12345678901),
        Person('小金', '女', 18, 12345678901),
        Person('小智', '女', 18, 12345678901),
        Person('小妮', '女', 10, 12345678901),
        Person('张三', '男', 12, 12345678901),
        Person('李四', '男', 10, 12345678901),
        Person('王五', '男', 19, 12345678901)
    ]
    test_out_josephus('F:\\Python\\test\\test1.csv','',result_csv)

    result_name = '王麻子'
    test_success_name_josephus('F:\\Python\\test\\test1.csv','',result_name)
    result_success = Person('王麻子', '男', 16, 12345678901)
    test_success_josephus('F:\\Python\\test\\test1.csv', '', result_success)
