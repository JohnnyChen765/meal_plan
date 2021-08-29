from abc import ABC, abstractmethod

import pandas as pd

from settings import chart
from src.utils import Features


class Food(ABC):
    g: int
    # raw features for 100g
    __features__: Features
    # features scaled on g
    features: Features

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    def kCal(self) -> int:
        return self.features["kCal"]

    @property
    def protein(self) -> int:
        return self.features["protein"]

    @property
    def fat(self) -> int:
        return self.features["fat"]

    @property
    def carb(self) -> int:
        return self.features["carb"]

    def __init__(self, g: int = 100) -> None:
        self.g = g
        self.__features__ = chart[self.name]
        self.features = (pd.Series(self.__features__) * g / 100).to_dict()

    def summary(self) -> Features:
        return pd.Series(self.features)
