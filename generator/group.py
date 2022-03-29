import os.path
from model.group import Group
import random
import string
import getopt
import sys
from mimesis import Generic
from mimesis.locales import Locale
import json
from fixture.application import Application
import pytest
import os.path
import importlib
import jsonpickle

g = Generic(locale=Locale.RU)

# Читаем опции с командной строки.
# Опция n: - задает кол-во генерируемых данных
# Опция f: - задает файл, в который должно помещаться
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

testdata = [Group(name="", header="", footer="")] + [
    Group(name=g.text.word(), header=g.text.word(), footer=g.text.word())
    for i in range(n)
]

# Путь к файлу.
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

# Открытие файла для записи. 'w' - режим записи.
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2, ensure_ascii=False)
    out.write(jsonpickle.encode(testdata))

