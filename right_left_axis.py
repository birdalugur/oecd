import pandas as pd
from helper import crop_data
import plotly.graph_objects as go
from plotly.offline import plot

# path_all_items = "data/monthly_cpi_all_items.ods"
# path_goods = "data/monthly_cpi_goods.ods"
# path_services = "data/monthly_cpi_services.ods"

path_all_items = "data/quarterly_cpi_all_items.ods"
path_goods = "data/quarterly_cpi_goods.ods"
path_services = "data/quarterly_cpi_services.ods"

data_all_items = pd.read_excel(path_all_items, na_values="..", index_col='Time', parse_dates=['Time'])
data_goods = pd.read_excel(path_goods, na_values="..", index_col='Time', parse_dates=['Time'])
data_services = pd.read_excel(path_services, na_values="..", index_col='Time', parse_dates=['Time'])

# if timefreq is monthly
data_all_items.index = pd.to_datetime(data_all_items.index, format="%YM%m")
data_goods.index = pd.to_datetime(data_goods.index, format="%YM%m")
data_services.index = pd.to_datetime(data_services.index, format="%YM%m")

country_list = ["CRI", "CHL", "GBR", "USA", "MEX"]

data_goods = data_goods[country_list]
data_services = data_services[country_list]
data_all_items = data_all_items[country_list]

ratio_goods_all = data_goods / data_all_items
ratio_goods_all = ratio_goods_all.dropna(how='all', axis=1).dropna(how='all', axis=0)

ratio_services_all = data_services / data_all_items
ratio_services_all = ratio_services_all.dropna(how='all', axis=1).dropna(how='all', axis=0)

ratio_goods_all, ratio_services_all = crop_data([ratio_goods_all, ratio_services_all], 2000)

# ratio_goods_all.columns = "g_" + ratio_goods_all.columns
# ratio_services_all.columns = "s_" + ratio_services_all.columns


def goods_vs_services(first_df, second_df, countries):
    for country_name in countries:
        try:
            goods = first_df[country_name]
        except KeyError:
            continue

        services = second_df[country_name]

        df = pd.concat([goods, services], axis=1)
        df.columns = ["goods", "services"]

        fig = go.Figure()

        line_1 = go.Scatter(x=df.index, y=df["goods"], name='goods/general')
        line_2 = go.Scatter(x=df.index, y=df["services"], name='services/general')

        fig.add_traces([line_1, line_2])

        fig.update_layout(plot_bgcolor='white')
        fig.update_yaxes(linecolor='black', gridcolor="lightgray")
        fig.update_xaxes(linecolor='black', gridcolor="lightgray")

        fig.update_layout(title='{} - Index'.format(country_name),
                          xaxis_title='Quarterly',
                          yaxis_title='Ratio')

        plot(fig, filename="{}.html".format(country_name), auto_open=False)


goods_vs_services(ratio_goods_all, ratio_services_all, country_list)
