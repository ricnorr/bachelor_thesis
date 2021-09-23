import pandas as pd
import numpy as np
from datetime import date

def checkNoDuplicating(n_files : int, start_month : int, start_year : int, sum_previous : int) -> int:
    for i in range(n_files):
        month = (start_month + i) % 12 + 1
        month = str(month)
        if len(month) == 1:
            month = "0" + month
        else:
            pass
        year = start_year + ((start_month + i) // 12)

        df_temp = pd.read_csv(f"data/palms_report_data_{year}_{month}.csv", index_col=0, encoding="ISO-8859-1")
        sum_current = df_temp.sum()

        # If all of the column sums are the same, then sum of the boolean comparison on the left
        # will be equal to the number of columns seen on the right
        if (sum_previous == sum_current).sum() == sum_current.shape[0]:
            print("Duplicated readings")
            print(f"Current file: region-palms-report_{year}_{month}.csv")
            raise Exception("loop failed")
        else:
            sum_previous = sum_current
    return sum_previous     

def importAndConcatData(start_year : int, start_month : int, n_files : int) -> pd.DataFrame:
    df_palms = pd.DataFrame()
    for i in range(n_files):
        month = (start_month + i) % 12 + 1
        month = str(month)
        if len(month) == 1:
            month = "0" + month
        else:
            pass
        year = start_year + ((start_month + i) // 12)
        #     print(f"region-palms-report_{year}_{month}.csv")
        df_temp = pd.read_csv(f"data/palms_report_data_{year}_{month}.csv", index_col=0, encoding="ISO-8859-1")
        df_temp["palms_date"] = date(year, int(month), 1)
        df_palms = pd.concat([df_palms, df_temp])
    column_list = df_palms.columns.tolist()
    column_list = column_list[-3:-1] + column_list[:-3] + [column_list[-1]]
    df_palms = df_palms[column_list]
    df_palms.reset_index(inplace=True, drop=True)
    return df_palms
