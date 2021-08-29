from typing import Dict, TypedDict

import pandas as pd


class Features(TypedDict):
    kCal: int
    protein: int
    fat: int
    carb: int


Chart = Dict[str, Features]


def load_chart_pd() -> pd.DataFrame:
    df = pd.read_csv("data/food_chart.csv")
    return df


def load_chart() -> Chart:
    dico = {}
    df = load_chart_pd()

    for index, row in df.iterrows():
        features = row.to_dict()
        del features["name"]
        dico[row["name"]] = features

    return dico
