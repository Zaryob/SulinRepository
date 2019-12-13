#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import kde
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools


def setup():
    shelltools.system("./Setup-kf5.sh")
    kde.configure("-DKS_KF5=ON")

def build():
    kde.make()

def install():
    kde.install()

    inarytools.dodoc("ChangeLog", "LICENSE")

