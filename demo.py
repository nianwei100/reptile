from random import randint

from rich import print
from rich.highlighter import Highlighter


class RainbowHighlighter(Highlighter):

    def highlight(self, text: str) -> None:
        for index in range(len(text)):
            text.stylize(f"color({randint(16, 255)})", index, index + 1)


rainbow = RainbowHighlighter()
print(rainbow('台下的少年'))
