import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QtWidgetsApplication2Class(object):

    def setupUi(self, QtWidgetsApplication2Class):
        QtWidgetsApplication2Class.setObjectName("QtWidgetsApplication2Class")
        QtWidgetsApplication2Class.resize(820, 501)
        self.label = QtWidgets.QLabel(QtWidgetsApplication2Class)
        self.label.setGeometry(QtCore.QRect(410, 30, 68, 15))
        self.label.setObjectName("label")
        self.start = QtWidgets.QLineEdit(QtWidgetsApplication2Class)
        self.start.setGeometry(QtCore.QRect(500, 30, 161, 21))
        self.start.setObjectName("start")
        self.in_text = QtWidgets.QTextEdit(QtWidgetsApplication2Class)
        self.in_text.setGeometry(QtCore.QRect(20, 80, 311, 351))
        self.in_text.setObjectName("in_text")
        self.open_file = QtWidgets.QPushButton(QtWidgetsApplication2Class)
        self.open_file.setGeometry(QtCore.QRect(90, 40, 93, 28))
        self.open_file.setObjectName("open_file")
        self.step = QtWidgets.QLineEdit(QtWidgetsApplication2Class)
        self.step.setGeometry(QtCore.QRect(500, 70, 161, 21))
        self.step.setObjectName("step")
        self.label_2 = QtWidgets.QLabel(QtWidgetsApplication2Class)
        self.label_2.setGeometry(QtCore.QRect(410, 70, 68, 15))
        self.label_2.setObjectName("label_2")
        self.start_josephus = QtWidgets.QPushButton(QtWidgetsApplication2Class)
        self.start_josephus.setGeometry(QtCore.QRect(680, 40, 101, 41))
        self.start_josephus.setObjectName("start_josephus")
        self.label_3 = QtWidgets.QLabel(QtWidgetsApplication2Class)
        self.label_3.setGeometry(QtCore.QRect(410, 110, 68, 15))
        self.label_3.setObjectName("label_3")
        self.out_text = QtWidgets.QTextEdit(QtWidgetsApplication2Class)
        self.out_text.setGeometry(QtCore.QRect(500, 120, 301, 271))
        self.out_text.setObjectName("out_text")
        self.label_4 = QtWidgets.QLabel(QtWidgetsApplication2Class)
        self.label_4.setGeometry(QtCore.QRect(420, 410, 68, 15))
        self.label_4.setObjectName("label_4")
        self.success_text = QtWidgets.QTextEdit(QtWidgetsApplication2Class)
        self.success_text.setGeometry(QtCore.QRect(500, 400, 301, 31))
        self.success_text.setObjectName("success_text")

        self.retranslateUi(QtWidgetsApplication2Class)
        QtCore.QMetaObject.connectSlotsByName(QtWidgetsApplication2Class)

    def retranslateUi(self, QtWidgetsApplication2Class):
        _translate = QtCore.QCoreApplication.translate
        QtWidgetsApplication2Class.setWindowTitle(_translate("QtWidgetsApplication2Class", "约瑟夫环"))
        self.label.setText(_translate("QtWidgetsApplication2Class", "开始下标："))
        self.open_file.setText(_translate("QtWidgetsApplication2Class", "打开文件"))
        self.label_2.setText(_translate("QtWidgetsApplication2Class", "相关规则："))
        self.start_josephus.setText(_translate("QtWidgetsApplication2Class", "开始约瑟夫"))
        self.label_3.setText(_translate("QtWidgetsApplication2Class", "淘汰顺序："))
        self.label_4.setText(_translate("QtWidgetsApplication2Class", "游戏获胜："))