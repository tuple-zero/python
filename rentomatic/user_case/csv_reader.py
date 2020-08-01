import zipfile
import csv

from rentomatic.entities.reader import Reader
from rentomatic.entities.person import Person


class CSVReader(Reader):

    def __init__(self, path: str):
        self._file = None
        self._file = open(path,encoding='utf-8')
        if self._file:
            self._reader: csv.reader = csv.reader(self._file)

    def __del__(self):
        if self._file:
            self._file.close()

    def __iter__(self):
        self._line: int = -1
        return self

    def __next__(self) -> Person:
        self._line = self._line +1
        item = next(self._reader)
        if self._line > 0 and item:
            name = item[0]
            sex = item[1]
            try:
                age = int(item[2])
                if age < 0:
                    age = 0
            except ValueError:
                age = 0
            try:
                tel_num = int(item[3])
            except ValueError:
                tel_num = 0
            return Person(name,sex,age,tel_num)

    @classmethod
    def from_zip(cls, path: str, target_name: str):
        with zipfile.ZipFile(path, 'r') as zip_file:
            new_path = zip_file.extract(target_name, './data/')  # 返回解压的路径
        return cls(new_path)  # 等同于TXTReader(new_path)