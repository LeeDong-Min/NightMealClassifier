import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QLabel, QStatusBar
from PyQt5.QtGui import *

import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

model = load_model('./model/vgg_night_meal_model.h5')


# filename='C:/Users/tjoeun/정리/datas/night_meal/validation/jokbal/jokbal_img121.jpg'


class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.sid = QImage('1.jpg').scaled(200, 150)
        btn = QPushButton('image change', self)
        btn.resize(btn.sizeHint())
        btn.move(300, 200)
        btn.clicked.connect(self.openFileNameDiaglog)

        food = '야식은?'
        self.lbl = QLabel(food, self)

        self.lbl.move(200, 220)

        self.setGeometry(800, 300, 500, 400)
        self.setWindowTitle('6번째 창입니다.')
        self.show()

    def openFileNameDiaglog(self):
        fileName, _ = QFileDialog.getOpenFileName(self, '불러올 이미지를 선택하세요.', '',
                                                  'Image Files(*.jpg;*.png);;All File(*);; python File(*.py)')
        if fileName:
            img = ''
            X = ''
            print(fileName)

            img = image.load_img(fileName, target_size=(150, 150))
            X = image.img_to_array(img)
            X = X.reshape(-1, 150, 150, 3)
            class_names = ['chiken', 'dakbal', 'jokbal', 'mandoo', 'pizza', 'pork_belly', 'pork_cutlet', 'ramyun',
                           'sundae', 'tteokbokki']

            A = model.predict(X)
            msg = class_names[np.argmax(A)]

            self.lbl.setText(msg)

            # self.lbl2 = QLabel(msg, self)
            # self.lbl2.move(200, 260)

            self.sid = QImage(fileName).scaled(200, 150)

    def change_label_value(self, msg):
        self.lbl2

    def grayScale(self, image):
        for i in range(self.sid.width()):
            for j in range(self.sid.height()):
                c = image.pixel(i, j)
                gray = qGray(c)
                alpha = qAlpha(c)
                image.setPixel(i, j, qRgba(gray, gray, gray, alpha))
        return image

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawImages(painter)
        painter.end()

    def drawImages(self, painter):
        painter.drawImage(5, 15, self.sid)
        painter.drawImage(self.sid.width() + 30, 15, self.grayScale(self.sid.copy()))


def main():
    app = QApplication(sys.argv)
    w = Exam()
    sys.exit(app.exec_())
    # print('메인안에서 실행되는 프린트 문입니다.')


if __name__ == '__main__':
    print('메인입니다.')
    main()
