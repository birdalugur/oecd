import pandas as pd
from mychart import export_chart

data = pd.read_excel("data/CPI_TR_G&S.xlsx")

data = data.set_index(pd.to_datetime(data.Time)).drop("Time", axis=1)

cols = ["P_goods/P_General", "P_service/P_General"]

data = data[cols]

quarterly_data = data.resample('Q').mean()

export_chart(df=quarterly_data, xtitle="Time",ytitle="", file_name="tr_g&s", title="")

