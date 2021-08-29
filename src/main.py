from src.body.body import Body, Bulking
from src.food.food import ChickenBreast, Courgette, Whey, WhiteRice
from src.meal.meal import Meal

body = Body(weight=55, fat=0.25, cal_neutral=1500)

chicken_meal = Meal(
    [
        ChickenBreast(g=200),
        Whey(g=25),
        WhiteRice(g=100),
        Courgette(g=50),
    ]
)

bulking1 = Bulking(body=body, calory_intake=2000, features=None)
print(bulking1.summary())
