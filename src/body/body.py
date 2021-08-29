from abc import abstractmethod
from typing import Optional

import pandas as pd

from src.food.utils import Features

nutrients_calory = {
    # kCal per g
    "protein": 4,
    "carb": 4,
    "fat": 9,
}


class Body:
    weight: int  # kg
    fat: float  # [0, 1]
    cal_neutral: int

    def __init__(
        self,
        weight: int,
        fat: float,
        # Daily intake
        cal_neutral: int,
    ) -> None:
        self.weight = weight
        self.fat = fat
        self.cal_neutral = cal_neutral

    @property
    def lean_body_mass(self) -> float:
        return self.weight * (1 - self.fat)


class BodyStrategy:
    body: Body
    features: Features
    calory_intake: int

    @property
    @abstractmethod
    def protein_intake(self) -> float:
        # gram of protein per weight
        pass

    @property
    @abstractmethod
    def fat_percentage(self) -> float:
        # percentage of calory intake
        pass

    @abstractmethod
    def get_default_calory_intake(self) -> int:
        # depends if you are cutting or bulking
        pass

    def __init__(
        self, body: Body, calory_intake: Optional[int], features: Optional[Features]
    ):
        self.body = body
        self.calory_intake = (
            calory_intake if calory_intake else self.get_default_calory_intake()
        )
        self.features = (
            features
            if features
            else {"protein": self.protein, "fat": self.fat, "carb": self.carb}
        )

    @property
    def protein(self) -> float:
        # in gram
        return self.body.weight * self.protein_intake

    @property
    def fat(self) -> float:
        # in gram
        return self.calory_intake * self.fat_percentage / nutrients_calory["fat"]

    @property
    def carb(self) -> float:
        # in gram
        return (
            self.calory_intake
            - self.protein * nutrients_calory["protein"]
            - self.fat * nutrients_calory["fat"]
        ) / nutrients_calory["carb"]

    def summary(self) -> pd.Series:
        return pd.Series(self.features)


class Bulking(BodyStrategy):
    protein_intake = 2  # gram of protein per weight
    fat_percentage = 0.2  # percentage of calory intake

    @abstractmethod
    def get_default_calory_intake(self) -> int:
        return self.body.cal_neutral + 250


class Cutting(BodyStrategy):
    protein_intake = 2.5  # gram of protein per weight
    fat_percentage = 0.2  # percentage of calory intake

    @abstractmethod
    def get_default_calory_intake(self) -> int:
        return self.body.cal_neutral - 500
