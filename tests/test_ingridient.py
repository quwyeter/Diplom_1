from praktikum.ingredient import Ingredient
from data import Data
import pytest


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type, name, price', Data.INGREDIENTS)
    def test_get_type_ingredient(self, ingredient_type, name, price):
        ing = Ingredient(ingredient_type, name, price)

        assert ing.get_type() == ing.type

    @pytest.mark.parametrize('ingredient_type, name, price', Data.INGREDIENTS)
    def test_get_name_ingredient(self, ingredient_type, name, price):
        ing = Ingredient(ingredient_type, name, price)

        assert ing.get_name() == ing.name

    @pytest.mark.parametrize('ingredient_type, name, price', Data.INGREDIENTS)
    def test_get_price_ingredient(self, ingredient_type, name, price):
        ing = Ingredient(ingredient_type, name, price)

        assert ing.get_price() == ing.price
