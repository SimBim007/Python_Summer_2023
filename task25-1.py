# Задача 25-1
# Простой вариант:
# Разработайте счетчик нажатий на кнопку, который меняет
# свою надпись на число нажатий на нее (1, 2, 3 и т.д.)


import sys
from PyQt6.QtCore import QSize,Qt
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QMainWindow,QLabel

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Задача 25-1")
        self.button=QPushButton("Нажми на кнопку")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.clickDD)

        self.setFixedSize(QSize(200,200))
        self.setCentralWidget(self.button)
        self.status=1
        self.count=0
    def clickDD(self):

        if self.status == 1:
            print(f"status-1")
            self.count+=1
            self.status = 2
            print(self.count)

        else:
            print(f"status-2")
            self.status = 1
            self.count+=1
            print(self.count)



app=QApplication([])
window=MainWindow()

window.show() # окно по умолчанию скрыто
app.exec()