import pymysql
import pandas as pd
from sqlalchemy import create_engine

class DBtools:
    def __init__(self):
        pass

    def Excel_Reader(self, filepath):
        # filepath 를 읽어들여 해당 내용을 Pandas Dataframe 형태로 df객체에 저장하는 문구, 다만 sheet명은 현재 재고현황 으로 고정 해 두었다.
        self.df = pd.read_excel(filepath, skiprows=2, sheet_name = '재고현황')

        # 여기에 읽은 Excel 이 목표로 하는 datafile 이 맞는지 확인하는 메소드 추가되어야 함(Excel_Judge)

        # 함수 결과값으로 반환한다.
        return self.df

    def Excel_Judge(self, df):
        pass

    def Data_Uploader(self, df):
        # 차후 이 부분은 접속창에서 주소와 id를 입력받는 것으로 수정할 필요가 있다. 현재는 내 db명, id, 암호, 서버주소를 그대로 사용한다.
        engine = create_engine("mysql+pymysql://yhhuh:"+"srcroll0"+"@192.168.0.240:3306/yhhuh?charset=utf8", encoding = 'utf-8')

        # 접속실행
        conn = engine.connect()

        # 입력받은 df dataframe 을 db에 업로드
        df.to_sql(name = 'pandas_df', con = engine, if_exists='replace', index='false')

        # 접속종료
        conn.close()


    def module_test(self):
        print('Module is loaded!')


if __name__ == '__main__':
    test = DBtools()
    df = test.Excel_Reader('//192.168.0.2/소재발주/통합소재 재고관리 ver2.xlsx')
    test.Data_Uploader(df)
