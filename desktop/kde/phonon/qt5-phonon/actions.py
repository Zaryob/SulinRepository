#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import kde
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    kde.configure("-DPHONON_BUILD_PHONON4QT5=ON")

def build():
    kde.make()

def install():
    kde.install()
