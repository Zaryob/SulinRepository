#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import pythonmodules
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get


def build():
    shelltools.system("python3 configure.py --bootstrap")
    shelltools.system("asciidoc doc/manual.asciidoc")
    #shelltools.system("emacs -Q --batch -f batch-byte-compile misc/ninja-mode.el")

def check():
    #needs new package gtest -> ignore it for now
    shelltools.system("python3 ./configure.py")
    shelltools.system("./ninja ninja_test")
    shelltools.system("./ninja_test --gtest_filter=-SubprocessTest.SetWithLots")

def install():
    inarytools.dobin("ninja", "/usr/bin")

    inarytools.insinto("/usr/share/bash-completion/completions", "misc/bash-completion", "ninja")

    inarytools.dodoc("HACKING.md", "COPYING", "RELEASING", "README", "doc/manual.asciidoc")

    inarytools.dohtml("doc/manual.html")
