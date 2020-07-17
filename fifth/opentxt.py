import zipfile
import os
import csv
import fifth.People as po
import fifth.ReaderCsv as rcsv
import fifth.ReaderTxt as rtxt
import fifth.ReaderZip as rzip


def open_zip(filename):
    '''
    读取.zip压缩文件内容
    :param filename:文件名
    :return:文集的数组
    '''
    out_list = []
    zip_file = zipfile.ZipFile(filename)
    first_file_name = zip_file.namelist()[0]
    content = zip_file.read(first_file_name)
    txt_content = content.decode('utf-8')
    content_list = txt_content.split("\r\n")
    for line in content_list:
        line_list = line.split()
        sex = '无'
        if line_list[1] == '女':
            sex = 0
        if line_list[1] == '男':
            sex = 1
        out_list.append(po.PersonInfo(line_list[0],sex,int(line_list[2]),int(line_list[3])))
    zip_file.close()
    return out_list


def open_cvs(filename):
    out_list = []
    with open(filename,encoding='utf-8') as csv_file:
        csv_read = csv.reader(csv_file)
        line_num = 0
        for line in csv_read:
            if line_num != 0:
                if line[1] == '女':
                    sex = 0
                else:
                    sex = 1
                out_list.append(po.PersonInfo(line[0], sex, int(line[2]), int(line[3])))
            line_num += 1
    return out_list


def open_txt(filename):
    out_list = []
    with open(filename,encoding='utf-8') as txt_file:
        for line in txt_file:
            line_list = line.split()
            sex = '无'
            if line_list[1] == '女':
                sex = 0
            if line_list[1] == '男':
                sex = 1
            out_list.append(po.PersonInfo(line_list[0], sex, int(line_list[2]), int(line_list[3])))
    return out_list


def open_class_file_method(filename):
    out_list = []
    arr = os.path.splitext(filename)
    file_extend = arr[len(arr)-1]
    if file_extend == '.zip':
        read_zip = rzip.ReaderZip(filename)
        read_zip.append_reader()
        out_list = [person for person in read_zip]
    if file_extend == '.csv':
        read_csv = rcsv.ReaderCsv(filename)
        read_csv.append_reader()
        out_list = [person for person in read_csv]
    if file_extend == '.txt':
        read_txt = rtxt.ReaderTxt(filename)
        read_txt.append_reader()
        out_list = [person for person in read_txt]
    return out_list


def open_file_method(filename):
    out_list = []
    arr = os.path.splitext(filename)
    file_extend = arr[len(arr)-1]
    if file_extend == '.zip':
        out_list = open_zip(filename)
    if file_extend == '.csv':
        out_list = open_cvs(filename)
    if file_extend == '.txt':
        out_list = open_txt(filename)
    return out_list


if __name__ == "__main__":
    people_list = open_class_file_method('test.txt')
    for person in people_list:
        print(person)
    print('-'*60)
    people_list = open_class_file_method('test.zip')
    for person in people_list:
        print(person)
    print('-' * 60)
    people_list = open_class_file_method('test1.csv')
    for person in people_list:
        print(person)