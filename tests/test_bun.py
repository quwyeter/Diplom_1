from praktikum.bun import Bun
from data import Data
class TestBun:
    def test_get_name_bun(self):
        bun = Bun(Data.NAME, Data.PRICE)

        assert bun.get_name() == bun.name

    def test_get_price_bun(self):
        bun = Bun(Data.NAME, Data.PRICE)

        assert bun.get_price() == bun.price
