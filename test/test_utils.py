from time import sleep
from geograph.utils import *
from io import StringIO
from contextlib import redirect_stdout
import sys


def test_timing():
    @timing
    def f():
        sleep(0.5)
        return 1

    with StringIO() as buf, redirect_stdout(buf):
        f()
        assert buf.getvalue().find("function: f took: 5") != -1
        assert buf.getvalue().find("e-01 sec.") != -1


def test_hex2name():

    assert hex2name("none") == "white"
    assert hex2name("#b22222") == "firebrick"


