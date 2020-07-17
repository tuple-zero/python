import fifth.People as po
import csv


class ReaderCsv(object):

    def __init__(self,file):
        self.file = file
        self.reader = []

    def append_reader(self):
        out_list = []
        with open(self.file, encoding='utf-8') as csv_file:
            csv_read = csv.reader(csv_file)
            line_num = 0
            for line in csv_read:
                if line_num != 0:
                    if line[1] == '女':
                        sex = 0
                    else:
                        sex = 1
                    self.reader.append(po.PersonInfo(line[0], sex, int(line[2]), int(line[3])))
                line_num += 1

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
    reader_test = ReaderCsv('test1.csv')
    reader_test.append_reader()
    people_list = [person for person in reader_test]
    for person in reader_test:
        print(person)
    print("-"*50)
    print(people_list)