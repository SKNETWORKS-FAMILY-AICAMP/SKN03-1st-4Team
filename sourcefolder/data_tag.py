import pandas as pd
import os

class data_tag:
    def __init__(self) -> None:
        self.data_refine()

    def data_refine(self) -> None:
        for j in range(2020,2025):
            for i in range(1,13):
                try:
                    df = pd.read_excel("./car_info/{year}/{year}_{month:02d}.xlsx".format(month = i, year = j), sheet_name="10.연료별_등록현황")
                except:
                    break
                test_df = df.iloc[[1,19,36,53,87],range(3,20)]
                test_df.columns = [i for i in range(17)]
                tran_df = test_df.T
                tran_df.columns = ["지역", "휘발유", "경유", "LPG", "전기"]
                try:
                    tran_df.to_csv("./csv_source/{year}/{year}_{month:02d}.csv".format(month=i,year=j), index=False)
                except:
                    path = "./csv_source/{year}".format(year = j)
                    os.mkdir(path)
                    tran_df.to_csv("./csv_source/{year}/{year}_{month:02d}.csv".format(month=i,year=j), index=False)


if __name__=="__main__":
    refine = data_tag()
    