import pandas as pd

from src.body.body import BodyStrategy
from src.meal.meal import MealPlan


class Analyzer:
    meal_plan: MealPlan
    body_strategy: BodyStrategy

    def __init__(self, meal_plan: MealPlan, body_strategy: BodyStrategy) -> None:
        self.meal_plan = meal_plan
        self.body_strategy = body_strategy

    # def details(self) -> None:
    #     for meal in self.meal_plan.meals:
    #         print(f"Summary of {meal.name}")
    #         print(meal.summary())
    #         print("\n")

    #     print("Summary of body strategy")
    #     print(self.body_strategy.summary())
    #     print("\n")

    #     print("Analyzer Summmary")
    #     print(self.summary())

    def details(self) -> None:
        df = pd.DataFrame(
            [meal.summary() for meal in self.meal_plan.meals]
            + [self.body_strategy.summary(), self.summary()],
            index=[meal.name for meal in self.meal_plan.meals]
            + ["body_strategy", "analyzer"],
        )

        return df

    def summary(self) -> pd.Series:
        return self.meal_plan.summary() - self.body_strategy.summary()
