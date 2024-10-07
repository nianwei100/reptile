from returns.result import Result, safe


def divide(a, b):
    return a / b


@safe
def safe_divide(a, b) -> Result[int, str]:
    return divide(a, b)


result = safe_divide(10, 0)
print(result.failure())
