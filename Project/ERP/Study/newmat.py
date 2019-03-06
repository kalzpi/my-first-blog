import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox
from PyQt5 import uic

form_new_mat_class = uic.loadUiType('Data/UI/newmat.ui')[0]
f = open("Data/Test/test_data.txt", 'r')
data = f.readlines()
print(data)
f.close()


class new_mat(QWidget, form_new_mat_class):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setupUi(self)
        self.comboBox_comp.addItem('MWU')
        self.comboBox_mod.addItem('SFM')


if __name__ == '__main__':
    pass
#    app = QApplication(sys.argv)
#    MyWidget = new_mat()
#
#    MyWidget.show()
#
#    sys.exit(app.exec_())
