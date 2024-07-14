from praktikum.burger import Burger, Bun
from data import Data
from unittest.mock import Mock


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        bun = Bun(Data.NAME, Data.PRICE)
        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient_mock = Mock()
        burger.add_ingredient(ingredient_mock)

        assert ingredient_mock in burger.ingredients

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.remove_ingredient(0)

        assert burger.ingredients[0] == ingredient_2

    def test_move_ingredient(self):
        burger = Burger()
        ingredient_1 = Mock()
        ingredient_2 = Mock()

        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0, 1)

        assert burger.ingredients == [ingredient_2, ingredient_1]

    def test_get_price(self):
        burger = Burger()
        bun = Mock()
        ingredient_1 = Mock()
        ingredient_2 = Mock()

        bun.get_price.return_value = 100
        ingredient_1.get_price.return_value = 200
        ingredient_2.get_price.return_value = 300
        burger.set_buns(bun)

        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        price = bun.get_price() * 2 + ingredient_1.get_price() + ingredient_2.get_price()

        assert burger.get_price() == price

    def test_get_receipt(self):
        burger = Burger()
        bun = Mock()
        ingredient = Mock()

        bun.get_name.return_value = Data.NAME
        bun.get_price.return_value = Data.PRICE
        ingredient.get_name.return_value = Data.INGREDIENT_NAME
        ingredient.get_type.return_value = Data.INGREDIENT_TYPE
        ingredient.get_price.return_value = Data.PRICE

        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        receipt = burger.get_receipt()

        assert '= sauce chili sauce =' and '(==== red bun ====)' and 'Price: 900' in receipt
