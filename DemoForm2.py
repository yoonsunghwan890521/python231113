# DemoForm2.py
# DemoForm2.ui(화면단) + DemoForm.py(로직단)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#디자인파일 로딩
form_class = uic.loadUiType("DemoForm3.ui")[0]

#폼클래스 정의(QDialog)
class DemoForm(QMainWindow, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def firstClick(self):
        self.label.setText("첫번째 버튼")
    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭~")

#직접 모듈을 실행한 경우면 실행
if __name__=="__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()