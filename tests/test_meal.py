from src.food.food import ChickenBreast, WhiteRice
from src.meal.meal import Meal
from tests.utils import assert_series_are_equal

chicken = ChickenBreast(g=200)
rice = WhiteRice(g=200)

meal = Meal([chicken, rice])


def test_meal_summary_should_give_correct_features() -> None:
    summary = meal.summary()
    expected_summary = chicken.summary() + rice.summary()

    assert_series_are_equal(expected_summary, summary)
