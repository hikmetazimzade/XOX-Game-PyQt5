from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from Game import XOXWindow
from ChooseBackground import Backrgound_Window

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Menu')
        self.setWindowIcon(QIcon('images\main_menu_image.png'))
        self.setStyleSheet('background:rgb(176, 139, 255)')

        start_game = QPushButton(self)
        start_game.setGeometry(600, 150, 800, 250)
        start_game.setStyleSheet("QPushButton{\n"
                                  "  background:rgb(47, 148, 255);\n"
                                  "  border:rgb(47, 148, 255);\n"
                                  "  border-radius:20px;\n"
                                  "  color : white;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "  background:rgb(97, 181, 255);\n"
                                  "  border:2px solid rgb(97, 181, 255);\n"
                                  "}")
        start_game.setText('Start Game')
        start_game.setFont(QFont('Times', 80))
        start_game.clicked.connect(self.Start_Game)


        background_button = QPushButton(self)
        background_button.setGeometry(600, 500, 800, 250)
        background_button.setStyleSheet("QPushButton{\n"
                                  "  background:rgb(47, 148, 255);\n"
                                  "  border:rgb(47, 148, 255);\n"
                                  "  border-radius:20px;\n"
                                  "  color : white;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "  background:rgb(97, 181, 255);\n"
                                  "  border:2px solid rgb(97, 181, 255);\n"
                                  "}")
        background_button.setText('Choose Background')
        background_button.setFont(QFont('Times', 53))
        background_button.clicked.connect(self.Set_Background)


    def Start_Game(self):
        self.close()
        self.game_window = XOXWindow()
        self.game_window.showMaximized()


    def Set_Background(self):
        self.close()
        self.background = Backrgound_Window()
        self.background.showMaximized()