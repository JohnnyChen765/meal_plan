from src.food.food import ChickenBreast, Courgette, Whey, WhiteRice
from src.meal.meal import Meal

meal1 = Meal(
    [
        ChickenBreast(g=200),
        WhiteRice(g=100),
        Courgette(g=50),
        Whey(g=25),
    ]
)
