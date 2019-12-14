#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import kde
from inary.actionsapi import inarytools

def setup():
    kde.configure("-DHTML_INSTAL_DIR=/usr/share/doc/kdelibs4support/html")

def build():
    kde.make()

def install():
    kde.install()

    inarytools.dodoc("README.md", "COPYING.LIB")