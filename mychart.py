import plotly.graph_objects as go
from plotly.offline import plot
import pandas as pd


def export_chart(df: pd.DataFrame, xtitle: str, ytitle: str, title: str, file_name: str) -> None:
    traces = [go.Scatter(x=df.index, y=df[c], name=c) for c in df.columns]

    fig = go.Figure(data=traces)

    # fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(plot_bgcolor='white')
    fig.update_yaxes(linecolor='black', gridcolor="lightgray")
    fig.update_xaxes(linecolor='black', gridcolor="lightgray")
    fig.update_yaxes(autorange=True, fixedrange=False)
    fig.update_layout(title=title,
                      xaxis_title=xtitle,
                      yaxis_title=ytitle)

    tickvals = df.index.to_list()
    ticktext = [d.strftime('%Y-%B') for d in df.index]
    fig.update_xaxes(tickvals=tickvals, ticktext=ticktext)

    plot(fig, filename=r"{}.html".format(file_name), auto_open=False)
