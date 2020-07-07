#!/usr/bin/env python
#coding:utf-8
import random
import math


print("Hello,World")
a = 19+2*4-8/2
print(a)

line = list(range(1,10))
line.insert(9,0)
print(line)
line.pop(0)
print(line)
#line.insert(9,1)
line.append(1)
print(line)


n=0
list1=[]
sum=0
while n<40:
    a=random.randint(0,100)
    list1.append(a)
    sum+=a
    n+=1
avg=sum/n
print(avg)
n=0
count=0
list2=[]
while n<40:
    if(list1[n]<avg):
        list2.append(list1[n])
        count += 1
        print(list1[n],end='\t')
    n += 1
list2.sort(reverse=True)
print()
print(list2)

#字符串的输出
st="How  are   you."
print(st)
list1=st.split()
word=" ".join(list1)
print(list1)
print(word)

st_lst=st.split(" ")
print(st_lst)
#words = [s.strip() for s in str_lst]
word= [s for s in st_lst if s!=""]
print(word)
word =" ".join(word)
print(word)

#方程的解
def getsolution(a,b,c):
    d=b*b-4*a*c
    if(d<0):
        print("方程 %dx*x+%dx+%d=0 无解"%(a,b,c))
    elif(d==0):
        x = -(b/(2*a))
        print("方程 %dx*x+%dx+%d=0 有一个解，为 %.2f"% (a,b,c,x))
        return x
    else:
        sqrt_d=math.sqrt(d)
        x1=(-b-sqrt_d)/(2*a)
        x2=(-b+sqrt_d)/(2*a)
        print("方程 %dx*x+%dx+%d=0 有两个解，第一个解为 %.2f，第二个解为 %。2f" % (a,b,c,x1,x2))
        return x1,x2

getsolution(1,2,1)


#学生成绩
studentscore = {"zhangsan":90, "lisi":78, "wangermazi":39,"wanghua":80,"xiaoming":60,
         "zhangsi":50, "liwu":20, "wangmazi":68,"lizi":78,"xiaohong":20}

def sumscore(studentscore):
    sums = 0
    count=0
    max=0
    min=100
    for value in studentscore.values():
        if(max<value):
            max=value
        if(min>value):
            min=value
        sums=sums+value
        count+=1
    avg = sums/count
    return sums,avg,max,min
print(studentscore.values())
total,avg,max,min=sumscore(studentscore)
print("总分： %.2f"% total)
print("平均分： %.2f"% avg)
print("最大值：%d"%max)
print("最小值：%d"%min)
print(list(sorted(studentscore.items(),key= lambda x:x[1],reverse=True)))

#寻找素数
list1=[]
n=0
def prime():
    n=0
    count=0
    for i in range(2,100):
        count = int(math.sqrt(i))
        for j in range(2,count+1):
            if( i%j == 0):
                break
        else:
            list1.append("%d" % i)
            n+=1
    return list1,n

list1,n = prime()
print(list1)
print(n)
