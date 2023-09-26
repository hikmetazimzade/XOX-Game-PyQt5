from PyQt5.QtWidgets import QApplication
import sys
import MainMenu

app = QApplication(sys.argv)
main_window = MainMenu.MainWindow()
main_window.showMaximized()
sys.exit(app.exec())