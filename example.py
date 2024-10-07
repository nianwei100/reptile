from functools import lru_cache, reduce
from random import randint
from typing import List, Union

from rich import print
from rich.highlighter import Highlighter
from rich.text import Text


@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


class RainbowHighlighter(Highlighter):
    def highlight(self, text: Text) -> None:
        for index in range(len(text)):
            text.stylize(f'color({randint(16, 255)})', index, index + 1)


class Microware:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False

    def turn_on(self) -> None:
        if self.turned_on:
            print(f'Microwave ({self.brand}) is already turned on.')
        else:
            self.turned_on = True
            print(f'Microwave ({self.brand}) is now turned on.')

    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f'Microwave ({self.brand}) is now turned off.')
        else:
            self.turned_on = True
            print(f'Microwave ({self.brand}) is already turned off.')

    def run(self, seconds: int) -> None:
        if self.turned_on:
            print(f'Running ({self.brand}) for {seconds} seconds')
        else:
            print('A mystical force whispers: "Turn on my microwave first..."')

    def __str__(self) -> str:
        return f'{self.brand} (Rating: {self.power_rating})'

    def __repr__(self) -> str:
        return f'Microwave(brand="{self.brand}", power_rating="{self.power_rating}")'


smeg: Microware = Microware('Smeg', 'B')
bosch: Microware = Microware('Bosch', 'C')
samsung: Microware = Microware('Samsung', 'A')


def factorial(n):
    assert n >= 0, 'n should be greater than 0'
    if n == 0 or n == 1:
        return 1
    return reduce(lambda a, b: a * b, range(1, n + 1))


def partition(arr: List[Union[float, int]], low: int, high: int) -> Union[int, float]:
    the_one = arr[low]

    i = low
    j = high

    while i < j:
        while arr[j] >= the_one and i < j:
            j = j - 1

        while arr[i] <= the_one and i < j:
            i = i + 1

        arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[low] = arr[low], arr[i]

    return i


def quick_sort(arr, low, high):
    if low < high:
        index = partition(arr, low, high)

        quick_sort(arr, low, index - 1)
        quick_sort(arr, index + 1, high)


def sort(arr):
    print('before')
    print(arr)
    quick_sort(arr, 0, len(arr) - 1)
    print('after')
    print(arr)


if __name__ == '__main__':
    input_arr = [
        24,
        5,
        8,
        954,
        6,
        49,
        55,
        66,
        86,
        32,
        431,
        42,
        36,
        3242,
        78,
        4.5,
    ]
    sort(input_arr)
