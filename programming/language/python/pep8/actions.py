#!/usr/bin/env python3

from inary.actionsapi import pythonmodules
from inary.actionsapi import inarytools


def build():
    pythonmodules.compile()
    pythonmodules.compile(pyVer = "3")


def install():
    pythonmodules.install()
    inarytools.rename("/usr/bin/pep8", "pep8-2.7")
    pythonmodules.install(pyVer = "3")
