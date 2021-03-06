#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import autotools
from inary.actionsapi import get

import os

def setup():
    autotools.configure()

def build():
    autotools.make("bash_completion.sh")

def install():
    autotools.rawInstall('DESTDIR=%s' % get.installDIR())

    inarytools.dodoc("AUTHORS", "CHANGES", "COPYING", "README.md")
