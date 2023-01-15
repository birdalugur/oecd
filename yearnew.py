import plotly.graph_objects as go
import pandas as pd
from plotly.offline import plot

path = "data/annual_cpi_goods.ods"
path2 = "data/annual_cpi_services.ods"

data_goods = pd.read_excel(path, na_values="..", index_col='Time', parse_dates=['Time'])
data_services = pd.read_excel(path2, na_values="..", index_col='Time', parse_dates=['Time'])

countries = data_services.columns.tolist()


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

        line_1 = go.Scatter(x=df.index, y=df["goods"], name='goods')
        line_2 = go.Scatter(x=df.index, y=df["services"], name='services')

        fig.add_traces([line_1, line_2])

        fig.update_layout(plot_bgcolor='white')
        fig.update_yaxes(linecolor='black', gridcolor="lightgray")
        fig.update_xaxes(linecolor='black', gridcolor="lightgray")

        fig.update_layout(title='{} - Index'.format(country_name),
                          xaxis_title='Quarterly',
                          yaxis_title='CPI')

        plot(fig, filename="{}.html".format(country_name), auto_open=False)
