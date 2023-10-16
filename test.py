import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply(self):
        assert self.calc.multiply(self,2, 6)==12

    def test_adding_success(self):
        assert self.calc.adding(self, 4, 2)==6

    def test_subtraction(self):
            self.calc.subtraction(self, 3, 1)==2

    def test_division(self):
            self.calc.division(self, 8, 4)==2

    def teardown(self):
        print(' Выполнение метода Teardown')