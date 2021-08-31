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
    Oil,
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
        WhiteRice(g=110),
        Courgette(g=50),
        Banana(g=100),
        Yogurt(g=100),
        Oil(g=15),
    ],
    name="chicken_meal",
)

porc_meal = Meal(
    [
        Pork(g=200),
        Whey(g=25),
        WhiteRice(g=110),
        Courgette(g=50),
        Apple(g=100),
        Yogurt(g=100),
        Oil(g=15),
    ],
    name="porc_meal",
)


meal_plan = MealPlan([bread_breakfast, chicken_meal, porc_meal])
analyzer = Analyzer(meal_plan, bulking)
# print(analyzer.summary())
print(analyzer.details())

#                     kCal  protein        fat    carb  fibers
# bread_breakfast   257.00    19.80  10.280000   20.86    1.08
# chicken_meal      779.85    74.17  25.980000   58.35    3.10
# porc_meal         896.85    65.37  46.680000   49.35    2.90
# body_strategy    2000.00   110.00  44.444444  290.00     NaN
# analyzer          -66.30    49.34  38.495556 -161.44     NaN
