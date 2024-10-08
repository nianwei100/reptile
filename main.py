from __future__ import barry_as_FLUFL

from returns.result import Result, safe
from rich import print


def divide(a, b):
    return a / b


@safe
def safe_divide(a, b) -> Result[int, float]:
    return divide(a, b)


res = safe_divide(10, 0)
print(res.failure())
