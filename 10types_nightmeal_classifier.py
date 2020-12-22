from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import sys
import platform
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from night_meal.tentypes_nightmeal_classify import Ui_MainWindow

from matplotlib import rc

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.showStatusMsg("이미지를 선택해주세요.")
        self.model = load_model('./vgg_night_meal_model.h5')
        self.res = ""
        self.class_name = ['치킨', '닭발', '족발', '만두', '피자', '삼겹살', '돈까스', '라면',
                           '순대', '떡볶이']

        self.predict = None

        self.x = []
        self.y = []
        self.canvas = None

        self.selimgbutton.clicked.connect(self.openFileNameDiaglog)
        self.selmodelbutton.clicked.connect(self.choseModel)

    def showStatusMsg(self, msg):
        self.statusbar.showMessage(msg)

    def showResult(self):
        self.result.appendPlainText("이 음식은 '" + self.res + "' 로 예상됩니다.")

    def showResultProba(self):
        for i in np.argsort(self.predict)[0][::-1][:5]:
            self.top5.appendPlainText(self.class_name[i] + ":" + str(np.round(self.predict[0][i], 10)) + "%" + "\n")
            self.x.append(self.class_name[i])
            self.y.append(np.round(self.predict[0][i], 10))

    def showGraph(self):
        N = 5
        value = self.y
        ind = np.arange(N)
        width = 0.35

        fig = plt.Figure()
        ax = fig.add_subplot(111)
        ax.bar(ind, value, width)
        ax.set_xticks(ind + width / 20)
        ax.set_xticklabels(self.x)

        self.canvas = FigureCanvas(fig)
        self.canvas.draw()
        self.verticalLayout.addWidget(self.canvas)
        self.canvas.show()

    def openFileNameDiaglog(self):
        self.clearAll()
        fileName, _ = QFileDialog.getOpenFileName(self, '불러올 이미지를 선택하세요.', '',
                                                  'Image Files(*.jpg;*.png);;All File(*);; python File(*.py)')
        if fileName:
            self.label.setPixmap(QtGui.QPixmap(fileName).scaled(800, 500))

            img = image.load_img(fileName, target_size=(150, 150))
            X = image.img_to_array(img) / 255
            X = X.reshape(-1, 150, 150, 3)

            self.predict = self.model.predict(X)
            msg = self.class_name[np.argmax(self.predict)]

            self.res = msg
            self.showResult()
            self.showResultProba()
            self.showGraph()
            self.showStatusMsg("이미지 분류 완료")

    def clearAll(self):
        self.top5.clear()
        self.result.clear()
        self.x = []
        self.y = []
        for i in reversed(range(self.verticalLayout.count())):
            self.verticalLayout.itemAt(i).widget().setParent(None)

    def choseModel(self):
        fileName, _ = QFileDialog.getOpenFileName(self, '불러올 모를 선택하세요.', '','h5 Files(*.h5)')

        self.model = load_model(fileName)
        self.showStatusMsg("모델변경 완료")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    you_viewer_main = Main()
    you_viewer_main.show()
    app.exec_()
