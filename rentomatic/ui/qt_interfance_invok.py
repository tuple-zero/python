import sys

from PyQt5.QtWidgets import QWidget,QApplication,QFileDialog,QMessageBox

from rentomatic.ui.qt_interface import Ui_QtWidgetsApplication2Class
from rentomatic.interface.interface import Interface


class QTWindow(QWidget,Ui_QtWidgetsApplication2Class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._interface = None

        self.open_file.clicked.connect(self.open_one_file)
        self.start_josephus.clicked.connect(self.start_josephus_circulation)

    def open_one_file(self):
        file_name,file_type = QFileDialog.getOpenFileName(self,'选择文件','F:\\Python\\test','*.txt *.csv *.zip')
        file_path = file_name.replace('/','\\\\')
        self.create_interface(file_path)
        people_info = self._interface.get_people_str()
        self.in_text.setText(people_info)

    def create_interface(self,file_path):
        self._interface = Interface()
        self._interface.create_reader(file_path)
        self._interface.get_josephus()

    def start_josephus_circulation(self):
        start = self.start.text()
        step = self.step.text()
        self._interface.set_start(int(start))
        try:
            self._interface.check_start()
        except ValueError:
            msg = QMessageBox(self,'提示',"请输入小于{len(self._interface.get_people())}的数。")
            msg.exec()
        self._interface.set_start(int(step))
        people_info = self._interface.get_out_str()
        self.out_text.setText(people_info)
        success_person = self._interface.get_people()
        self.success_text.setText(str(success_person))


def show_qt_window():
    app = QApplication(sys.argv)
    qt_window = QTWindow()
    qt_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    show_qt_window()