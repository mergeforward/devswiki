
class Calculator:
    def add(self, x, y):
        return x+y


def test_calc_add_should_equal_to_x_plus_y(x, y):
    calc = Calculator()
    answer = calc.add(x, y)
    assert answer == x + y


if __name__ == "__main__":
    test_calc_add_should_equal_to_x_plus_y(10, 20)