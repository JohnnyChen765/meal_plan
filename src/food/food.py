from abc import ABC, abstractmethod

import pandas as pd

from src.settings import chart
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

    def summary(self) -> pd.Series:
        return pd.Series(self.features)


class WhiteRice(Food):
    name = "white_rice"


class WhiteBread(Food):
    name = "white_bread"


class OatFlakes(Food):
    name = "oat_flakes"


class Pasta(Food):
    name = "pasta"


class ChickenBreast(Food):
    name = "chicken_breast"


class BeefSteak(Food):
    name = "beef_steak"


class Salmon(Food):
    name = "salmon"


class Pork(Food):
    name = "pork"


class Ham(Food):
    name = "ham"


class Egg(Food):
    name = "egg"


class Whey(Food):
    name = "whey"


class Broccoli(Food):
    name = "broccoli"


class Courgette(Food):
    name = "courgette"


class Avocado(Food):
    name = "avocado"


class Almonds(Food):
    name = "almonds"


class Apple(Food):
    name = "apple"


class Banana(Food):
    name = "banana"


class Yogurt(Food):
    name = "yogurt"


class Oil(Food):
    name = "oil"
