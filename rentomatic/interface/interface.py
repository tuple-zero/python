import os

import zipfile

from rentomatic.entities.person import Person
from rentomatic.user_case.csv_reader import CSVReader
from rentomatic.user_case.txt_reader import TXTReader
from rentomatic.user_case.josephus import Josephus


class Interface(object):

    def __init__(self):
        self._start = 1
        self._step = 1
        self._reader = None
        self._josephus = None

    def create_reader(self, file_path: str, target_file: str = None):
        if not file_path:
            return
        arr = os.path.splitext(file_path)
        if '.txt' == arr[len(arr) - 1]:
            self._reader = TXTReader(file_path)
        if '.csv' == arr[len(arr) - 1]:
            self._reader = CSVReader(file_path)
        if '.zip' == arr[len(arr) - 1]:
            self.create_zip_reader(file_path,target_file)

    def create_zip_reader(self, file_path: str, target_file: str):
        arr = os.path.splitext(target_file)
        if arr[len(arr)-1] == ".txt":
            self._reader = TXTReader.from_zip(file_path, target_file)
        if '.csv' == arr[len(arr)-1]:
            self._reader = CSVReader.from_zip(file_path, target_file)
        else:
            raise FileNotFoundError

    def read_name_list(self, file_path: str) -> list:
        arr = os.path.splitext(file_path)
        if '.zip' == arr[len(arr) - 1]:
            with zipfile.ZipFile(file_path) as zip_file:
                if zip_file:
                    file_names = zip_file.namelist()
                    return file_names
        return []

    def set_start(self, start: int):
        self._start = start
        self._josephus.set_start(self._start)

    def set_step(self, step: int):
        self._step = step
        self._josephus.set_step(self._step)

    def get_josephus(self):
        self._josephus: Josephus = Josephus(self._reader)
        if len(self._josephus.get_people()) == 0:
            raise FileNotFoundError

    def get_people(self):
        return self._josephus.get_people()

    def out_people_list(self):
        people = []
        for person in self._josephus:
            people.append(person)
        return people

    def get_success_person_name(self) -> str:
        return self.get_people().get_name()

    def check_start(self,start):
        if len(self._josephus.get_people()) < start:
            raise ValueError

    def get_people_str(self) -> str:
        people = self.get_people()
        people_info = ''
        for person in people:
            if person:
                if person._gender == 0:
                    sex = '女'
                if person._gender == 1:
                    sex = '男'
                people_info = people_info + person._name +'  '+ sex +'  '+ str(person._age) + '  '+str(person._number)+'\n'
        return people_info

    def get_out_str(self) -> str:
        out_people = self.out_people_list()
        people_info = ''
        for person in out_people:
            if person:
                if person._gender == 0:
                    sex = '女'
                if person._gender == 1:
                    sex = '男'
                people_info = people_info + person._name +'  '+ sex +'  '+ str(person._age) + '  '+str(person._number)+'\n'
        return people_info
