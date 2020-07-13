import forth.Person as person
import forth.Joseph as joseph
import forth.Fileopen as fp
import forth.InData as ind


people_list = fp.open_file()
ind.show_list(people_list)
rule, start_num = ind.get_input()
while start_num > person.PersonInfo.count:
    print("开始编号输入错误，请输入小于%d的开始下标：" % person.PersonInfo.count)
    rule, start_num = ind.get_input()
out_people = joseph.out_circle(people_list, rule, start_num)
ind.show_list(out_people)
ind.get_success_person(out_people)