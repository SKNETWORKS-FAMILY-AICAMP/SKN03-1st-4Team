import pandas as pd # 데이터 추출, 재가공, 정렬을 위한 모듈
def group_car_type():
    labeling_i = { # labeling 앞자리
        '0':'승용차', # 0 = 승용차
        '1':'승합차', # 1 = 승합차
        '2':'특수차', # 2 = 특수차
        '3':'화물차' # 3 = 화물차
    }

    labeling_j = { # labeling 뒷자리
        '0':'관용', # 0 = 관용
        '1':'개인', # 1 = 개인
        '2':'영업', # 2 = 영업
        '3':'합계' # 3 = 합계
    }
    # labeling
    # city = 시도별
    # year = 연도별

    for i in range(4): # 앞자리
        for j in range(4): #뒷자리
            df = pd.read_excel("./car_info/전국 자동차 등록 현황/{i}/{i}{j}.xlsx".format(i=i,j=j))         # 엑셀 파일 불러오기
            test_df = df.iloc[range(0,54),range(0,19)]                                     # 0~53행, 1~18열 추출
            test_df.rename(columns={'Unnamed: 0':'date'}, inplace=True)                    # 행 0의 column명 지정
            test_df.to_csv("./csv_source/total_review/{j} {i} 현황.csv".format(i = labeling_i[str(i)], j = labeling_j[str(j)]), index=False)    # 작업한 행렬 csv 파일로 추출


if __name__ == "__main__":
    group_car_type()