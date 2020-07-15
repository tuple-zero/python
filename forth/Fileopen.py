import forth.Person as person


def open_file(file_path):
    out_list = []
    with open(file_path, "r", encoding="utf-8") as out_file:
        for line in out_file:
            person_list = line.split()
            sex = 0
            if person_list[1] == '男':
                sex = 1
            a_person = person.PersonInfo(person_list[0], sex, int(person_list[2]), person_list[3])
            out_list.append(a_person)
    return out_list