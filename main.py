from __future__ import barry_as_FLUFL

from functools import reduce
from random import randint
from typing import Dict, List, NewType, Optional, Set, Tuple, Union

import pretty_errors
from rich.highlighter import Highlighter
from rich.text import Text

pretty_errors.configure(display_link=True)


class RainbowHighlighter(Highlighter):

    def highlight(self, text: Text) -> None:
        for index in range(len(text)):
            text.stylize(f"color({randint(16, 255)})", index, index + 1)


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


# smeg: Microware = Microware('Smeg', 'B')
# bosch: Microware = Microware('Bosch', 'C')
# samsung: Microware = Microware('Samsung', 'A')


def greeting(name: Optional[str]) -> str:
    return f'Hello {name}'


def double_or_square(number: Union[int, float]) -> Union[int, float]:
    if isinstance(number, int):
        return number * 2
    else:
        return number**2


UserId = NewType('UserId', int)
some_id = UserId(1243)


def add(x: int, y: int) -> int:
    return x + y


num_list = [i for i in range(1, 101)]
result = reduce(add, num_list)


def factorial(n):
    assert n >= 0, 'n should be greater than 0'
    if n == 0 or n == 1:
        return 1
    return reduce(lambda a, b: a * b, range(1, n + 1))


def get_name_age() -> Tuple[str, int]:
    return '王五', 18


def get_students() -> List[str]:
    return ["小黑", "小华", "小米"]


def get_scores() -> Dict[str, int]:
    return {"python": 100, "java": 80, "go": 80}


def get_unique_numbers() -> Set[Union[str, int]]:
    return {1, 2, 3, 4, 5, 6, '7'}


if __name__ == '__main__':
    pass
