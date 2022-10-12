import matplotlib.pyplot as plt
import main
import pytest
from datetime import datetime

arr_time_got = []
arr_size_got = []
arr = main.file_reader("tests/test_accuracy")
arr_big = main.file_reader("tests/test_duration")
arr_big_with_0 = arr_big.copy()
arr_big_with_0.append(0)


def test_sum():
    assert main._sum(arr) == 210


def test_min():
    assert main._min(arr) == 1


def test_max():
    assert main._max(arr) == 20


def test_mult():
    assert main._mult(arr) == 2432902008176640000


def test_sum_big():
    assert main._sum(arr_big)


def test_min_big():
    assert main._min(arr_big)


def test_max_big():
    assert main._max(arr_big)


def test_mult_big():
    assert main._mult(arr_big)


def test_mult_if_0_in():  # если в файле содержится ноль, то произведение всегда равно нулю
    assert main._mult(arr_big_with_0) == 0


def test_sum_time():
    for i in range(1, 100):
        tick = datetime.now()
        a = main.file_reader("tests/test_{}".format(i))
        assert main._sum(a)
        arr_time_got.append((datetime.now() - tick).microseconds / 100000)
        arr_size_got.append(len(a))
        plt.plot(arr_size_got, arr_time_got)
        plt.title("Зависимость времени выполнения от объема файла")
        plt.xlabel("Кол-во чисел в тесте")
        plt.ylabel("Время выполнения")
        plt.draw()
        plt.pause(0.001)
    plt.show()
