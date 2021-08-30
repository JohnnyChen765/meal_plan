from typing import List

import pandas as pd

from src.food.utils import Food


class Meal:
    items: List[Food]

    def __init__(self, items: List[Food]) -> None:
        self.items = items

    def details(self) -> pd.DataFrame:
        list_features = [{"name": x.name, **x.features} for x in self.items]
        return pd.DataFrame(list_features)

    def summary(self) -> pd.Series:
        list_features = [x.features for x in self.items]
        df = pd.DataFrame(list_features)
        return df.sum()


class MealPlan:
    def __init__(self, meals: List[Meal]) -> None:
        self.meals = meals

    def summary(self) -> pd.Series:
        df = pd.concat([meal.summary() for meal in self.meals])
        return df.sum()
