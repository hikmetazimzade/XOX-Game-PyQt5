from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon
import MainMenu

class Backrgound_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 600, 600)
        self.setWindowIcon(QIcon(r'images\background_image.jpg'))
        self.setStyleSheet('background:rgb(228, 255, 213)')
        self.setWindowTitle('Choose Background Color')
        self.dic = {}


        label = QLabel(self)
        label.setText('Click The Background You Want To Choose')
        label.setGeometry(500, 100, 1000, 150)
        label.setFont(QFont('Times', 30))

        background_1 = QPushButton(self)
        background_1.setGeometry(200, 300, 450, 170)
        background_1.setStyleSheet('background : rgb(135, 167, 120);'
                                   'border-radius:20px;')
        self.dic[background_1] = 'rgb(135, 167, 120)'

        background_2 = QPushButton(self)
        background_2.setGeometry(750, 300, 450, 170)
        background_2.setStyleSheet('background : white;'
                      'border-radius:20px;')
        self.dic[background_2] = 'white'

        background_3 = QPushButton(self)
        background_3.setGeometry(1300, 300, 450, 170)
        background_3.setStyleSheet('background : rgb(135, 167, 255);'
                      'border-radius:20px;')
        self.dic[background_3] = 'rgb(135, 167, 255)'

        background_4 = QPushButton(self)
        background_4.setGeometry(200, 600, 450, 170)
        background_4.setStyleSheet('background : rgb(141, 170, 163);'
                                   'border-radius:20px;')
        self.dic[background_4] = 'rgb(141, 170, 163)'

        background_5 = QPushButton(self)
        background_5.setGeometry(750, 600, 450, 170)
        background_5.setStyleSheet('background : rgb(220, 240, 255);'
                                   'border-radius:20px;')
        self.dic[background_5] = 'rgb(220, 240, 255)'

        background_6 = QPushButton(self)
        background_6.setGeometry(1300, 600, 450, 170)
        background_6.setStyleSheet('background : rgb(255, 197, 126);'
                                   'border-radius:20px;')
        self.dic[background_6] = 'rgb(255, 197, 126)'

        background_1.clicked.connect(self.Chosen_Button)
        background_2.clicked.connect(self.Chosen_Button)
        background_3.clicked.connect(self.Chosen_Button)
        background_4.clicked.connect(self.Chosen_Button)
        background_5.clicked.connect(self.Chosen_Button)
        background_6.clicked.connect(self.Chosen_Button)


    def Chosen_Button(self):
        button = self.sender()
        with open(r'background.txt', mode = 'w') as background:
            background.write(self.dic[button])

        self.close()
        self.main_menu = MainMenu.MainWindow()
        self.main_menu.showMaximized()