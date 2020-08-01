import zipfile

from rentomatic.entities.reader import Reader
from rentomatic.entities.person import Person


class TXTReader(Reader):

    def __init__(self, path: str):
        self._file = None
        self._file = open(path, encoding='utf-8')

    def __del__(self):
        if self._file:
            self._file.close()

    def __iter__(self):
        return self

    def __next__(self) -> Person:
        line = next(self._file)
        if not line:
            raise StopIteration
        line_list = line.split()
        name = line_list[0]
        sex = line_list[1]
        try:
            age = int(line_list[2])
            if age < 0:
                age = 0
        except ValueError:
            age = 0
        try:
            tel_num = int(line_list[3])
        except ValueError:
            tel_num = 0
        return Person(name,sex,age,tel_num)

    @classmethod
    def from_zip(cls, path: str, target_name: str):
        with zipfile.ZipFile(path, 'r') as zip_file:
            new_path = zip_file.extract(target_name, './data/')#返回解压的路径
        return cls(new_path)#等同于TXTReader(new_path)
