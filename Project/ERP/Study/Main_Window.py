import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5 import uic

import Import_Excel

form_main_window_class = uic.loadUiType('Data/UI/main_windows.ui')[0]


class MyWindow(QMainWindow, form_main_window_class):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)

        #File menu action signals
        self.actionQuit.triggered.connect(self.close)

        #Material menu action signals
        self.actionImport_Excel_File.triggered.connect(self.testmenu)

    def testmenu(self):
        self.i_excel = Import_Excel.MyWidget()
        self.i_excel.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyWindow = MyWindow()

    MyWindow.show()

    sys.exit(app.exec_())


