import sys

from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog

from PyQt5 import uic

import DBtool

form_widget_class = uic.loadUiType('Data/UI/import_excel_to_sql.ui')[0]

class MyWidget(QWidget, form_widget_class):

    #클래스 변수 선언
    #입력받은 엑셀파일의 경로
    filepath = ''

    #엑셀파일로부터 추출한 pandas db
    df = ''

    def __init__(self):
        super(QWidget, self).__init__()
        self.setupUi(self)

        #생성자에서 버튼 객체를 불러온다
        self.pushButton.clicked.connect(self.btn_clicked)
        self.pushButton_2.clicked.connect(self.btn_clicked_2)
        self.pushButton_3.clicked.connect(self.btn_clicked_3)

    def btn_clicked(self):
        fname = QFileDialog.getOpenFileName(self, directory='//192.168.0.2/소재발주/통합소재 재고관리 ver2.xlsx', filter='*.xlsx')

        if fname[0] == '':
            #QFileDialog에서 Cancel을 누를 시, fname[0]에 ''가 반환되는 것을 착안하여, 취소 시에는 함수가 실행되지 않도록 함.
            #self.lineEdit.setText('취소됨')
            pass
        else:
            MyWidget.filepath = fname[0]
            self.lineEdit.setText(MyWidget.filepath)
            #여기에 Pandas readexcel 구현해야함
            temp_db = DBtool.DBtools()
            MyWidget.df = temp_db.Excel_Reader(MyWidget.filepath)
            #print(MyWidget.filepath)
            #print(MyWidget.df)
            self.plainTextEdit.setPlainText('''File Path:  %s\nFile Load Complete'''%MyWidget.filepath)

        #self.plaintextedit.setText('파일정보')

    def btn_clicked_2(self):
        #여기에 Pandas DF to sql 구현해야함.
        if type(MyWidget.df) is str:
            self.plainTextEdit.setPlainText('''!!파일이 로드되지 않았습니다!!''')
        else:
            temp_db = DBtool.DBtools()
            temp_db.Data_Uploader(MyWidget.df)
            self.plainTextEdit.setPlainText('''업로드 완료''')

    def btn_clicked_3(self):
        self.close()
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyWidget = MyWidget()

    MyWidget.show()
    print(type(MyWidget.df))
    sys.exit(app.exec_())
