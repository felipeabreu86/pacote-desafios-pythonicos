from functools import partial


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


if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'Fizz'
    assert robot(6) == 'Fizz'
    assert robot(9) == 'Fizz'

    assert robot(5) == 'Buzz'
    assert robot(10) == 'Buzz'
    assert robot(20) == 'Buzz'

    assert robot(15) == 'FizzBuzz'
    assert robot(30) == 'FizzBuzz'
    assert robot(45) == 'FizzBuzz'
