from typing import List, Optional

import pandas as pd

from src.food.food import Food


class Meal:
    items: List[Food]
    name: Optional[str]

    def __init__(self, items: List[Food], name: Optional[str]) -> None:
        self.items = items
        self.name = name

    def details(self) -> pd.DataFrame:
        list_features = [{"name": x.name, "g": x.g, **x.features} for x in self.items]
        return pd.DataFrame(list_features)

    def summary(self) -> pd.Series:
        list_features = [x.features for x in self.items]
        df = pd.DataFrame(list_features)
        return df.sum()


class MealPlan:
    def __init__(self, meals: List[Meal]) -> None:
        self.meals = meals

    def summary(self) -> pd.Series:
        df = pd.concat([meal.summary() for meal in self.meals], axis=1)
        return df.sum(axis=1)
