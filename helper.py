import pandas as pd


def crop_data(data: pd.DataFrame | list[pd.DataFrame], start_year: int) -> pd.DataFrame | list[pd.DataFrame]:
    if type(data) != list:
        return data[data.index >= str(start_year)]
    else:
        list_of_data = []
        for df in data:
            list_of_data.append(df[df.index >= str(start_year)])
        return list_of_data
