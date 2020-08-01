from rentomatic.user_case.txt_reader import TXTReader
from rentomatic.entities.person import Person


def test_txt_reader_len(file_path, result):
    reader = TXTReader(file_path)
    count = 0
    for person in reader:
        if person:
            count += 1
    assert count == len(result)


def test_txt_reader_num(file_path, result):
    reader = TXTReader(file_path)
    people = []
    count = same = 0
    for person in reader:
        if person:
            if person == result[count]:
                same += 1
            count += 1
    assert count == same


def test_txt_reader(file_path, result):
    reader = TXTReader(file_path)
    people = []
    for person in reader:
        if person:
            people.append(person)
    assert people==result


if __name__ == "__main__":
    file_path = "F:\\Python\\test\\test.txt"
    result = [
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

    test_txt_reader_len(file_path,result)
    test_txt_reader_num(file_path,result)
    test_txt_reader(file_path, result)