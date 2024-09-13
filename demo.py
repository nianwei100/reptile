from __future__ import barry_as_FLUFL

import configparser
import os
import re
import time
from random import randint

import colorama
import jieba
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
from faker import Faker
from rich import print
from rich.console import Console
from rich.highlighter import Highlighter
from rich.markdown import Markdown
from rich.pretty import pprint
from rich.progress import track
from rich.table import Table
from rich.tree import Tree
from textblob import TextBlob

console = Console()
fake = Faker('zh_CN')

table = Table(title='UserInfo', show_header=True)
table.add_column("Name", style="cyan", no_wrap=True)
table.add_column("Phone", style="magenta")
table.add_column("Email", style="green")
for x in range(6):
    table.add_row(fake.name(), fake.phone_number(), fake.email())
console.print(table)

# for step in track(range(100)):
#     time.sleep(0.1)


class RainbowHighlighter(Highlighter):
    '''
    override highlight method in Highlighter
    '''

    def highlight(self, text: str) -> None:
        for index in range(len(text)):
            text.stylize(f"color({randint(16, 255)})", index, index + 1)
