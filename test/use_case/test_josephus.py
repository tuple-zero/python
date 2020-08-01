from rentomatic.user_case.josephus import Josephus


def test_josephus(in_list,result):
    josephus = Josephus(in_list)
    out_list = []
    for x in josephus:
        out_list.append(x)
    out_list.append(josephus.get_people())
    assert out_list == result


def test_josephus_sucess(in_list,in_start,in_step,result):
    josephus = Josephus(in_list)
    josephus.set_start(in_start)
    josephus.set_step(in_step)
    for x in josephus:
        x
    sucess = josephus.get_people()
    print(sucess)
    assert sucess == result


def test_josephus_all(in_list,in_start,in_step,result):
    josephus = Josephus(in_list)
    josephus.set_start(in_start)
    josephus.set_step(in_step)
    out_list = []
    for x in josephus:
        out_list.append(x)
    out_list.append(josephus.get_people())
    assert out_list == result


def test_josephus_append(in_list,result):
    josephus = Josephus(in_list)
    out_list = josephus.get_people()
    assert out_list==result


if __name__ == "__main__":
    in_list = [1,2,3,4,5]
    result = [1,2,3,4,5]
    test_josephus(in_list,result)
    start = 2
    step = 2
    result =[2,4,1,5,3]
    test_josephus_all(in_list,start,step,result)
    result = 5
    test_josephus_sucess(in_list,start,step,result)
    result = 3
    test_josephus_sucess(in_list, start, step, result)
    result = [1,2,3,4,5]
    test_josephus_append(in_list,result)