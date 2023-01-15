import pandas as pd
import plotly.express as px
from plotly.offline import plot

path = "oecd/annualy/cpi_goods_annual.ods"

# data = pd.read_excel(path, na_values="..", skiprows=1, index_col='Time')
data = pd.read_excel(path, na_values="..", index_col='Time', parse_dates=True)

fig = px.line(data)

fig.update_layout(title='Percentage change on the same period of the previous year',
                  xaxis_title='year',
                  yaxis_title='CPI')

plot(fig)
