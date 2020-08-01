from rentomatic.entities.person import Person


def test_person_name(name, sex, age, num, result):
    person = Person(name,sex,age,num)
    person_name = person.get_name()
    assert person_name == result


def test_person(name, sex, age, num, result):
    person = Person(name,sex,age,num)
    assert person == result

if __name__ == '__main__':

    #test_person_name("hello",'男',12,123456963258,'world')
    test_person_name("hello", '男', 12, 123456963258, 'hello')
    #test_person_name("小loli", '男', 12, 123456963258, '小lola')
    test_person_name("小loli", '男', 12, 123456963258, '小loli')
    test_person_name("小六", '男', 12, 123456963258, '小六')

    result = Person("hello",'女',14,123456689)
    test_person("hello",'女',14,123456689,result)