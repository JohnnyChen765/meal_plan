import pandas as pd

from src.body.body import BodyStrategy
from src.meal.meal import MealPlan


class Analyzer:
    meal_plan: MealPlan
    body_strategy: BodyStrategy

    def __init__(self, meal_plan: MealPlan, body_strategy: BodyStrategy) -> None:
        self.meal_plan = meal_plan
        self.body_strategy = body_strategy

    def summary(self) -> pd.Series:
        print(self.meal_plan.summary())
        print(self.body_strategy.summary())
        return self.meal_plan.summary() - self.body_strategy.summary()
