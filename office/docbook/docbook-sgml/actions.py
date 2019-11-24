#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir="."

def install():
    inarytools.insinto("/usr/share/sgml/docbook/sgml-dtd-%s" % get.srcVERSION(), "*.dcl")
    inarytools.insinto("/usr/share/sgml/docbook/sgml-dtd-%s" % get.srcVERSION(), "*.dtd")
    inarytools.insinto("/usr/share/sgml/docbook/sgml-dtd-%s" % get.srcVERSION(), "*.mod")
    inarytools.insinto("/usr/share/sgml/docbook/sgml-dtd-%s" % get.srcVERSION(), "docbook.cat", "catalog")

    inarytools.dodoc("README")
