import os
import zipfile
import fifth.People as po


class ReaderZip(object):

    def __init__(self,file):
        self.file = file
        self.reader = []

    def append_reader(self):
        zip_file = zipfile.ZipFile(self.file)
        file_names = zip_file.namelist()
        for filename in file_names:
            arr = os.path.splitext(filename)
            file_extend = arr[len(arr) - 1]
            if file_extend == '.txt':
                content = zip_file.read(filename)
                txt_content = content.decode('utf-8')
                content_list = txt_content.split("\r\n")
                for line in content_list:
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
    reader_test = ReaderZip('test.zip')
    reader_test.append_reader()
    people_list = [person for person in reader_test]
    for person in reader_test:
        print(person)
    print(people_list)