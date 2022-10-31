# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainwindow import Ui_Morse_GUI


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Morse_GUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())