#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.autoreconf("-ivh")

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.remove("/usr/share/aclocal/ax_check_enable_debug.m4")
    inarytools.remove("/usr/share/aclocal/ax_code_coverage.m4")
