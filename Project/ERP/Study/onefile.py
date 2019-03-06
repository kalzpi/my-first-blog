import sys
import pymysql
import pandas as pd
from sqlalchemy import create_engine
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog
from PyQt5 import uic

form_main_window_class = uic.loadUiType('main_windows.ui')[0]
form_widget_class = uic.loadUiType('import_excel_to_sql.ui')[0]

class MyWindow(QMainWindow, form_main_window_class):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)

        #File menu action signals
        self.actionQuit.triggered.connect(self.close)

        #Material menu action signals
        self.actionImport_Excel_File.triggered.connect(self.testmenu)

    def testmenu(self):
        self.i_excel = MyWidget()
        self.i_excel.show()

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
            temp_db = DBtools()
            MyWidget.df = temp_db.Excel_Reader(MyWidget.filepath)
            self.plainTextEdit.setPlainText('''File Path:  %s\nFile Load Complete'''%MyWidget.filepath)

        #self.plaintextedit.setText('파일정보')

    def btn_clicked_2(self):
        #여기에 Pandas DF to sql 구현해야함.
        if type(MyWidget.df) is str:
            self.plainTextEdit.setPlainText('''!!파일이 로드되지 않았습니다!!''')
        else:
            temp_db = DBtools()
            temp_db.Data_Uploader(MyWidget.df)
            self.plainTextEdit.setPlainText('''업로드 완료''')

    def btn_clicked_3(self):
        self.close()
        pass

class DBtools:
    def __init__(self):
        pass

    def Excel_Reader(self, filepath):
        #filepath를 읽어들여 해당 내용을 Pandas Dataframe 형태로 df객체에 저장하는 문구, 다만 sheet명은 현재 재고현황 으로 고정 해 두었다.
        self.df = pd.read_excel(filepath, skiprows=2, sheet_name = '재고현황')

        #여기에 읽은 Excel이 목표로 하는 datafile이 맞는지 확인하는 메소드 추가되어야 함(Excel_Judge)

        #함수 결과값으로 반환한다.
        return self.df

    def Excel_Judge(self, df):
        pass

    def Data_Uploader(self, df):
        #차후 이 부분은 접속창에서 주소와 id를 입력받는 것으로 수정할 필요가 있다. 현재는 내 db명, id, 암호, 서버주소를 그대로 사용한다.
        engine = create_engine("mysql+pymysql://yhhuh:"+"srcroll0"+"@192.168.0.240:3306/yhhuh?charset=utf8", encoding = 'utf-8')

        #접속실행
        conn = engine.connect()

        #입력받은 df dataframe을 db에 업로드
        df.to_sql(name = 'pandas_df', con = engine, if_exists='replace', index='false')

        #접속종료
        conn.close()


    def module_test(self):
        print('Module is loaded!')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyWindow = MyWindow()

    MyWindow.show()

    sys.exit(app.exec_())
