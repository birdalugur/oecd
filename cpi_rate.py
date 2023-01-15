import pandas as pd
from mychart import export_chart
from helper import crop_data

# path_all_items = "data/annual_cpi_all_items.ods"
# path_goods = "data/annual_cpi_goods.ods"
# path_services = "data/annual_cpi_services.ods"

path_all_items = "data/quarterly_cpi_all_items.ods"
path_goods = "data/quarterly_cpi_goods.ods"
path_services = "data/quarterly_cpi_services.ods"

data_all_items = pd.read_excel(path_all_items, na_values="..", index_col='Time', parse_dates=['Time'])
data_goods = pd.read_excel(path_goods, na_values="..", index_col='Time', parse_dates=['Time'])
data_services = pd.read_excel(path_services, na_values="..", index_col='Time', parse_dates=['Time'])

ratio_goods_all = data_goods / data_all_items
ratio_goods_all = ratio_goods_all.dropna(how='all', axis=1).dropna(how='all', axis=0)

ratio_services_all = data_services / data_all_items
ratio_services_all = ratio_services_all.dropna(how='all', axis=1).dropna(how='all', axis=0)

ratio_goods_all, ratio_services_all = crop_data([ratio_goods_all, ratio_services_all], 2020)

export_chart(ratio_goods_all, xtitle='Year', ytitle='Ratio',
             title="Ratio of CPI:All Items to CPI:Goods (Measure: Index, Frequency: Quarterly)",
             file_name="goods_div_all_items")

export_chart(ratio_services_all, xtitle='Year', ytitle='Ratio',
             title="Ratio of CPI:All Items to CPI:Services (Measure: Index, Frequency: Quarterly)",
             file_name="services_div_all_items")





