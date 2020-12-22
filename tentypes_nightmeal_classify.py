# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tentypes_nightmeal_classify.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1042, 1005)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 4, 1000, 600))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(70, 30, 800, 500))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../192.168.0.54/우리끼리/오늘실습 자료/web2.png"))
        self.label.setObjectName("label")
        self.selimgbutton = QtWidgets.QPushButton(self.groupBox)
        self.selimgbutton.setGeometry(QtCore.QRect(800, 550, 191, 41))
        self.selimgbutton.setObjectName("selimgbutton")
        self.selmodelbutton = QtWidgets.QPushButton(self.groupBox)
        self.selmodelbutton.setGeometry(QtCore.QRect(610, 550, 191, 41))
        self.selmodelbutton.setObjectName("selmodelbutton")
        self.result = QtWidgets.QPlainTextEdit(self.groupBox)
        self.result.setGeometry(QtCore.QRect(11, 560, 581, 21))
        self.result.setObjectName("result")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 614, 1011, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 634, 511, 311))
        self.groupBox_3.setObjectName("groupBox_3")
        self.top5 = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.top5.setGeometry(QtCore.QRect(10, 30, 491, 271))
        self.top5.setObjectName("top5")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 1010, 1011, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 950, 1011, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(540, 650, 481, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "10가지 야식분류기"))
        self.groupBox.setTitle(_translate("MainWindow", "모델 이미지"))
        self.selimgbutton.setText(_translate("MainWindow", "야식 이미지 선택"))
        self.selmodelbutton.setText(_translate("MainWindow", "야식분류 모델 선택"))
        self.groupBox_3.setTitle(_translate("MainWindow", "모델 분류 결과"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

