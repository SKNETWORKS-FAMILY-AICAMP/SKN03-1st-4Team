import pandas as pd

# column - 지역, 연료종류, 합계
# 분포는 -> 일단 https://sgis.kostat.go.kr/view/urban/main


# 지역 D:3 -> T:3, 
# 연료 종류(labeling) : 휘발류:0, 경유:1, LPG:2, 전기:3
# 휘발유 합계: D:21 -> T:21 , 경유 합계: D:38 -> T:38, LPG 합계: D:55 -> T:55, 전기 합계 : D:89 -> T:89 (202001 ~ 202406 범례 가능함을 확인)

data_row1 = pd.read_excel("./car_info/2020/2020_01.xlsx", sheet_name="10.연료별_등록현황", usecols = 'D:T', skiprows=range(1), nrows=1)
data_row1.columns = [i for i in range(17)]
data_row1 # 지역명 column

data_row2 = pd.read_excel("./car_info/2020/2020_01.xlsx", sheet_name="10.연료별_등록현황", usecols = 'D:T', skiprows=range(19), nrows=1)
data_row2.columns = [i for i in range(17)]
data_row2 # 휘발유 column

data_row3 = pd.read_excel("./car_info/2020/2020_01.xlsx", sheet_name="10.연료별_등록현황", usecols = 'D:T', skiprows=range(36), nrows=1)
data_row3.columns = [i for i in range(17)]
data_row3 # 경유 column

data_row4 = pd.read_excel("./car_info/2020/2020_01.xlsx", sheet_name="10.연료별_등록현황", usecols = 'D:T', skiprows=range(53), nrows=1)
data_row4.columns = [i for i in range(17)]
data_row4 # LPG column

data_row5 = pd.read_excel("./car_info/2020/2020_01.xlsx", sheet_name="10.연료별_등록현황", usecols = 'D:T', skiprows=range(87), nrows=1)
data_row5.columns = [i for i in range(17)]
data_row5 # 전기column

data_con = pd.concat([data_row1, data_row2, data_row3, data_row4, data_row5], axis=0)
data_refine = data_con.T
data_refine.columns=['지역', '휘발유','경유','LPG',"전기"]
data_refine