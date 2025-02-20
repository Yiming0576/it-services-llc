from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
import os
import logging

logger = logging.getLogger(__name__)
logger.info("logger initialized.") 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")

        button = QPushButton("My simple app.")
        button.pressed.connect(self.close)

        self.setCentralWidget(button)
        self.show()


app = QApplication(sys.argv)
w = MainWindow()
app.exec()