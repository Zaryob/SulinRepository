#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import perlmodules
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()

    inarytools.remove("/usr/share/man/man3/WWW::RobotRules::AnyDBM_File.3pm")
    inarytools.remove("/usr/share/man/man3/WWW::RobotRules.3pm")

    inarytools.dodoc("Changes", "MANIFEST", "README")
