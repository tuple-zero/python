import fifth.People as po

class ReaderTxt(object):

    def __init__(self,file):
        self.file = file
        self.reader = []

    def append_reader(self):
        out_list = []
        with open(self.file, encoding='utf-8') as txt_file:
            for line in txt_file:
                line_list = line.split()
                sex = '无'
                if line_list[1] == '女':
                    sex = 0
                if line_list[1] == '男':
                    sex = 1
                self.reader.append(po.PersonInfo(line_list[0], sex, int(line_list[2]), int(line_list[3])))

    def __iter__(self):
        self._line = -1
        return self

    def __next__(self):
        self._line += 1
        if len(self.reader) > self._line:
            return self.reader[self._line]
        else:
            raise StopIteration


if __name__ == '__main__':
    reader_test = ReaderTxt('test.txt')
    reader_test.append_reader()
    people_list = [person for person in reader_test]
    for person in reader_test:
        print(person)
    print(people_list)