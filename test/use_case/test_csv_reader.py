from rentomatic.user_case.csv_reader import CSVReader
from rentomatic.entities.person import Person


def test_csv_reader_len(file_path, result):
    reader = CSVReader(file_path)
    people = []
    for person in reader:
        if person:
            people.append(person)
    assert len(people)==len(result)


def test_csv_reader_num(file_path, result):
    reader = CSVReader(file_path)
    count = 0
    same = 0
    for person in reader:
        if person:
            if person == result[count]:
                same += 1
            count += 1
    assert same == len(result)


def test_csv_reader(file_path, result):
    reader = CSVReader(file_path)
    people = []
    for person in reader:
        if person:
            people.append(person)
    assert people == result


if __name__ == '__main__':

    file_path = "F:\\Python\\test\\test1.csv"
    result1 = [
        Person('小红','女',12,12345678912),
        Person('小黑','男',10,12345678912),
        Person('小李','男',19,12345678912),
        Person('小白','女',15,12345678912),
        Person('小明','男',17,12345678912),
        Person('小金','女',18,12345678912),
        Person('小智','女',18,12345678912),
        Person('小妮','女',10,12345678912),
        Person('张三','男',12,12345678912),
        Person('李四','男',10,12345678912),
        Person('王五','男',19,12345678912),
        Person('王麻子','男',10,12345678912)
    ]
    result2 = [
        Person('小红', '女', 12,12345678901),
        Person('小黑', '男', 10,12345678931),
        Person('小李', '男', 19,12345678201),
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
    test_csv_reader_len(file_path,result1)
    test_csv_reader_num(file_path, result2)
    test_csv_reader(file_path,result2)
