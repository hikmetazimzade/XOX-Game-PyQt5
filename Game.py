from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon
import sys

import MainMenu

player_order = 0
table = [[''] * 3 for i in range(3)]
round_number = 0
set_letter = 'O'

class XOXWindow(QWidget):
    def __init__(self):
        global table
        global round_number
        global set_letter
        global player_order

        table = [[''] * 3 for _ in range(3)]
        round_number = 0
        player_order = 0
        set_letter = 'O'

        super().__init__()
        self.setWindowTitle('XOX')
        self.setWindowIcon(QIcon('images\XOXGame.png'))
        with open('background.txt', mode = 'r') as background:
            self.setStyleSheet(f'background:{background.read()}')
        self.xy_dic = {}


        button_1 = QPushButton(self)
        button_1.setGeometry(500, 100, 250, 250)
        button_1.clicked.connect(self.Set_X_Y)

        button_2 = QPushButton(self)
        button_2.setGeometry(750, 100, 250, 250)
        button_2.clicked.connect(self.Set_X_Y)

        button_3 = QPushButton(self)
        button_3.setGeometry(1000, 100, 250, 250)
        button_3.clicked.connect(self.Set_X_Y)

        button_4 = QPushButton(self)
        button_4.setGeometry(500, 350, 250, 250)
        button_4.clicked.connect(self.Set_X_Y)

        button_5 = QPushButton(self)
        button_5.setGeometry(750, 350, 250, 250)
        button_5.clicked.connect(self.Set_X_Y)

        button_6 = QPushButton(self)
        button_6.setGeometry(1000, 350, 250, 250)
        button_6.clicked.connect(self.Set_X_Y)

        button_7 = QPushButton(self)
        button_7.setGeometry(500, 600, 250, 250)
        button_7.clicked.connect(self.Set_X_Y)

        button_8 = QPushButton(self)
        button_8.setGeometry(750, 600, 250, 250)
        button_8.clicked.connect(self.Set_X_Y)

        button_9 = QPushButton(self)
        button_9.setGeometry(1000, 600, 250, 250)
        button_9.clicked.connect(self.Set_X_Y)

        number = 0
        for i in (button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9):
            self.xy_dic[i] = number
            number += 1

    def Set_X_Y(self):
        global player_order
        global table
        global set_letter
        button = self.sender()
        if button.text() == '':
            set_letter = 'O'
            if player_order % 2 == 0:
                set_letter = 'X'
            button.setText(set_letter)
            button.setFont(QFont('Times', 60))
            player_order += 1
            button_dic = self.xy_dic[button]
            table[button_dic // 3][button_dic % 3] = set_letter
            self.CheckWinner()

    def CheckWinner(self):
        global table
        global round_number

        for i in range(3):
            columns = set()
            for k in range(3):
                columns.add(table[k][i])

            if (len(columns) == 1 and '' not in columns) or (table[i][0 : 3].count('X') == 3 or table[i][0 : 3].count('O') == 3):
                self.close()
                self.game_info = GameInfo()
                self.game_info.showMaximized()
                return

        left_side, right_side = set(), set()
        a = 2
        for h in range(3):
            left_side.add(table[h][h])
            right_side.add(table[h][a])
            a -= 1


        if (len(left_side) == 1 and '' not in left_side) or (len(right_side) == 1 and '' not in right_side):
            self.close()
            self.game_info = GameInfo()
            self.game_info.showMaximized()
            return

        round_number += 1
        if round_number == 9:
            self.close()
            self.game_info = GameInfo()
            self.game_info.showMaximized()


class GameInfo(QWidget):
    def __init__(self):
        global set_letter
        super().__init__()
        self.setStyleSheet('background:rgb(172, 216, 255)')
        self.setGeometry(600, 200, 600, 600)
        self.setWindowTitle('Game Info')
        self.setWindowIcon(QIcon('images\game_info.jpg'))

        info = QLabel(self)
        info.setGeometry(630, 0, 850, 250)

        if round_number == 9:
            info.setText('The Game Is A Draw')
            info.setFont(QFont('Times', 50))

        else:
            info.setText(set_letter + ' Player Won')
            info.setFont(QFont('Times', 70))

        play_again = QPushButton(self)
        play_again.setGeometry(650, 270, 700, 180)
        play_again.setText('Play Again')
        play_again.setStyleSheet("QPushButton{\n"
                                  "  background:rgb(47, 148, 255);\n"
                                  "  border:rgb(47, 148, 255);\n"
                                  "  border-radius:20px;\n"
                                  "  color : white;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "  background:rgb(161, 230, 255);\n"
                                  "  border:2px solid rgb(161, 230, 255);\n"
                                  "}")
        play_again.setFont(QFont('Times', 45))
        play_again.clicked.connect(self.Play_Again)

        back_button = QPushButton(self)
        back_button.setGeometry(650, 520, 700, 180)
        back_button.setText('Back To Main Menu')
        back_button.setStyleSheet("QPushButton{\n"
                                  "  background:rgb(47, 148, 255);\n"
                                  "  border:rgb(47, 148, 255);\n"
                                  "  border-radius:20px;\n"
                                  "  color : white;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "  background:rgb(161, 230, 255);\n"
                                  "  border:2px solid rgb(161, 230, 255);\n"
                                  "}")
        back_button.setFont(QFont('Times', 45))
        back_button.clicked.connect(self.Back_To_Menu)


        exit_button = QPushButton(self)
        exit_button.setGeometry(650, 770, 700, 180)
        exit_button.setText('Exit Game')
        exit_button.setStyleSheet("QPushButton{\n"
                                  "  background:rgb(47, 148, 255);\n"
                                  "  border:rgb(47, 148, 255);\n"
                                  "  border-radius:20px;\n"
                                  "  color : white;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "  background:rgb(161, 230, 255);\n"
                                  "  border:2px solid rgb(161, 230, 255);\n"
                                  "}")
        exit_button.setFont(QFont('Times', 60))
        exit_button.clicked.connect(self.Exit_Game)


    def Back_To_Menu(self):
        self.close()
        self.main_menu = MainMenu.MainWindow()
        self.main_menu.showMaximized()


    def Exit_Game(self):
        sys.exit()


    def Play_Again(self):
        self.close()
        self.game = XOXWindow()
        self.game.showMaximized()