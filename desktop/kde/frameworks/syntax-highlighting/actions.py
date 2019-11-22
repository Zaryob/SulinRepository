#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import kde
from inary.actionsapi import inarytools

# if inary can't find source directory, see /var/inary/syntax-highlighting/work/ and:
# WorkDir="syntax-highlighting-"+ get.srcVERSION() +"/sub_project_dir/"

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    inarytools.dodoc("COPYING.LIB", "README.md")

