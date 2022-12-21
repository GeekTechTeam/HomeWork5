from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def application():
    app  = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("GeekTech")
    window.setGeometry(500, 500, 500, 500)

    main_text = QtWidgets.QLabel(window)
    main_text.setText("GeekTech 150KGS")

    window.show()
    sys.exit(app.exec_())



application()