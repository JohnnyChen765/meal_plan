from typing import List

import pandas as pd

from src.food.utils import Food


class Meal:
    items: List[Food]

    def __init__(self, items: List[Food]) -> None:
        self.items = items

    def summary(self) -> pd.Series:
        list_features = [x.features for x in self.items]
        df = pd.DataFrame(list_features)
        return df.sum()
