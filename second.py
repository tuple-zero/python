#coding:utf-8
import random
import math

#数据位置转变
line_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(line_list)
line_list.remove(1)
print(line_list)
line_list.append(1)
print(line_list)


#成绩打印
def get_stu_scores(student_num=40, max_score=100):
    return [random.randint(0,100) for x in range(40)]


def get_under_avg(input_list):
    total_scores = sum(input_list)
    student_num = len(input_list)
    average_score = 1.0 * total_scores / student_num

    return [x for x in input_list if x < average_score], average_score


scores = get_stu_scores()
under_scores, average_score = get_under_avg(scores)
under_stu_num = len(under_scores)
ascending = False
scores.sort(reverse=ascending)
print("the average score if :%.1f" % average_score)
print("There are %d students less than average." % under_stu_num)
print(scores)


#去除空格
test_st = "   How     are      you?"
print(test_st)
split_list = test_st.split()
new_st = " ".join(split_list)
print(split_list)
print(new_st)

test_st = "   How     are      you?"
print(test_st)
split_list = test_st.split(" ")
new_list = [x for x in split_list if x != '']
new_st = " ".join(new_list)
print(new_list)
print(new_st)


#斐波那契数列
a, b = 0,1
for i in range(10):
    a, b = b, a+b
print(a)


#方程的解
def get_solution(a_int, b_int, c_int):
    delta = b_int * b_int - 4 * a_int * c_int
    if delta < 0:
        print("方程 %dx*x+%dx+%d=0 无解" % (a_int, b_int, c_int))
        return False
    elif delta == 0:
        x = -(b/(2*a))
        print("方程 %dx*x+%dx+%d=0 有一个解，为 %.2f" % (a_int,b_int,c_int,x))
        return x
    else:
        d_sqrt = math.sqrt(delta)
        x1 = (-b-d_sqrt)/(2*a_int)
        x2 = (-b+d_sqrt)/(2*a_int)
        print("方程 %dx*x+%dx+%d=0 有两个解，第一个解为 %.2f，第二个解为 %。2f" % (a_int,b_int,c_int,x1,x2))
        return x1,x2


get_solution(1, 2, 1)


#考试成绩
student_scores = {"zhangsan": 90, "lisi":78, "wangermazi":39,"wanghua":80,"xiaoming":60,
         "zhangsi":50, "liwu":20, "wangmazi":68,"lizi":78,"xiaohong":20}


def operate_score(student_scores):
    sum_scores = sum(student_scores.values())
    student_num = len(student_scores)
    maxx_score = max(student_scores.values())
    minx_score = min(student_scores.values())
    averagex_score = 1.0*sum_scores/student_num

    return sum_scores,maxx_score,minx_score,averagex_score


print(student_scores.values())
total_score, max_score,min_score, avg_score = operate_score(student_scores)
print("总分： %.2f" % total_score)
print("平均分： %.2f" % avg_score)
print("最大值：%d" % max_score)
print("最小值：%d" % min_score)
ascending = True
print(list(sorted(student_scores.items(), key=lambda x: x[1],reverse=ascending)))


Max_num = 100


#寻找素数
def find_prime(in_num):
    prime_l = []
    for i in range(2, in_num):
        count = int(math.sqrt(i))
        for j in range(2,count+1):
            if i % j == 0:
                break
        else:
            prime_l.append(i)
    return prime_l


prime_list = find_prime(Max_num)
print(prime_list)


def is_prime(in_num):  #素数
    """
    判断一个数是否为素数
    :param in_num:  输入参数
    :return: 布尔类型 是素数返回True 不是返回False
    """
    if in_num <= 1:
        return False
    for i in range(2, int(math.sqrt(in_num))+1):
        if in_num % i == 0:
            return False
    return True


prime_list = [x for x in range(2, Max_num) if is_prime(x)]
print(prime_list)


def get_list(in_num):
    """
    生成约瑟夫环
    :param in_num: 参与约瑟夫环的人数
    :return:返回一个约瑟夫环的列表
    """
    return [x for x in range(1,in_num)]


def out_circle(in_num,m):
    in_len = len(in_num)
    count = 0
    move = 0

    while in_len > 0:
        count += 1
        if move == in_len:
            move = 0
        if count == m:
            print(in_num.pop(move))
            count = 0
            move -= 1
            in_len -= 1
        move += 1


test_list = get_list(13)
out_circle(test_list, 4)