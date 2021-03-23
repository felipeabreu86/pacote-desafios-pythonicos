from functools import partial
import unittest


def multiple_of(base, num):
    return num % base == 0


multiple_of_5 = partial(multiple_of, 5)
multiple_of_3 = partial(multiple_of, 3)


def robot(pos):
    say = str(pos)
    if multiple_of_5(pos) and multiple_of_3(pos):
        say = 'FizzBuzz'
    elif multiple_of_5(pos):
        say = 'Buzz'
    elif multiple_of_3(pos):
        say = 'Fizz'
    return say


class FizzBuzzTest(unittest.TestCase):
    def test_say_1_when_1(self):
        self.assertEqual(robot(1), '1')

    def test_say_2_when_2(self):
        self.assertEqual(robot(2), '2')

    def test_say_4_when_4(self):
        self.assertEqual(robot(4), '4')

    def test_say_fizz_when_3(self):
        self.assertEqual(robot(3), 'Fizz')

    def test_say_fizz_when_6(self):
        self.assertEqual(robot(6), 'Fizz')

    def test_say_fizz_when_9(self):
        self.assertEqual(robot(9), 'Fizz')

    def test_say_buzz_when_5(self):
        self.assertEqual(robot(5), 'Buzz')

    def test_say_buzz_when_10(self):
        self.assertEqual(robot(10), 'Buzz')

    def test_say_buzz_when_20(self):
        self.assertEqual(robot(20), 'Buzz')

    def test_say_fizzbuzz_when_15(self):
        self.assertEqual(robot(15), 'FizzBuzz')

    def test_say_fizzbuzz_when_30(self):
        self.assertEqual(robot(30), 'FizzBuzz')

    def test_say_fizzbuzz_when_45(self):
        self.assertEqual(robot(45), 'FizzBuzz')


if __name__ == '__main__':
    unittest.main()

# Implementação anterior, sem utilizar o modulo unittest

'''
def assert_equal(result, expected):
    from sys import _getframe
    msg = 'Fail: Line {} got {} expected {}'

    if not result == expected:
        current = _getframe()
        caller = current.f_back
        line_no = caller.f_lineno
        print(msg.format(line_no, result, expected))


if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'
    # or
    assert_equal(robot(1), '1')
    assert_equal(robot(2), '2')
    assert_equal(robot(4), '4')

    assert robot(3) == 'Fizz'
    assert robot(6) == 'Fizz'
    assert robot(9) == 'Fizz'

    assert robot(5) == 'Buzz'
    assert robot(10) == 'Buzz'
    assert robot(20) == 'Buzz'

    assert robot(15) == 'FizzBuzz'
    assert robot(30) == 'FizzBuzz'
    assert robot(45) == 'FizzBuzz'
'''
