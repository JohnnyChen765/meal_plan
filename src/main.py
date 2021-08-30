from src.analyzer.analyzer import Analyzer
from src.body.body import Body, Bulking
from src.food.food import (
    Apple,
    Banana,
    ChickenBreast,
    Courgette,
    Egg,
    Ham,
    OatFlakes,
    Pork,
    Whey,
    WhiteBread,
    WhiteRice,
    Yogurt,
)
from src.meal.meal import Meal, MealPlan

body = Body(weight=55, fat=0.25, cal_neutral=1500)
bulking = Bulking(body=body, calory_intake=2000, features=None)

bread_breakfast = Meal([WhiteBread(g=40), Egg(g=60), Ham(g=40)], name="bread_breakfast")
oat_breakfast = Meal([OatFlakes(g=40)], name="oat_breakfast")

chicken_meal = Meal(
    [
        ChickenBreast(g=200),
        Whey(g=25),
        WhiteRice(g=100),
        Courgette(g=50),
        Banana(g=100),
        Yogurt(g=100),
    ],
    name="chicken_meal",
)

porc_meal = Meal(
    [
        Pork(g=200),
        Whey(g=25),
        WhiteRice(g=100),
        Courgette(g=50),
        Apple(g=100),
        Yogurt(g=100),
    ],
    name="porc_meal",
)

meal_plan = MealPlan([bread_breakfast, chicken_meal, porc_meal])
analyzer = Analyzer(meal_plan, bulking)
print(analyzer.summary())
