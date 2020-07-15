import forth.Person as person


def open_file():
    out_list = []
    with open("../test.txt", "r", encoding="utf-8") as out_file:
        for line in out_file:
            person_list = line.split()
            a_person = person.PersonInfo(person_list[0], person_list[1], person_list[2], person_list[3])
            out_list.append(a_person)
    return out_list