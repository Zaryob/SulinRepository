#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.insinto("/etc/bash_completion.d/", "extra/bash-completion-atool_0.1-1", "atool")

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "NEWS", "TODO")
