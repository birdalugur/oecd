import pandas as pd
import plotly.express as px
from plotly.offline import plot

path = "data/annual_cpi_goods.ods"
path2 = "data/annual_cpi_services.ods"

# data = pd.read_excel(path, na_values="..", skiprows=1, index_col='Time')
good = pd.read_excel(path, na_values="..", index_col='Time', parse_dates=True)
service = pd.read_excel(path2, na_values="..", index_col='Time', parse_dates=True)

service.columns = service.columns.str.strip()
good.columns = good.columns.str.strip()

good = good.unstack()
service = service.unstack()

good = good.reset_index()
service = service.reset_index()
good = good.assign(type="good")
service = service.assign(type="services")

df = pd.concat([good, service])

df.columns = ["Country", "Time", "Value", "Type"]

fig = px.line(df, x="Time", y="Value", color="Country", facet_col="Type")

fig.update_layout(title='Percentage change on the same period of the previous year')

fig.update_layout(plot_bgcolor='white')
fig.update_yaxes(linecolor='black', gridcolor="lightgray")
fig.update_xaxes(linecolor='black', gridcolor="lightgray")

plot(fig)
