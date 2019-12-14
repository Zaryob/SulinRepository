#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import inarytools

def install():
    inarytools.dobin("makeself.sh")
    inarytools.dodir("/usr/share/man")
    inarytools.dodir("/usr/share/makeself")
    inarytools.dobin("makeself-header.sh", "/usr/share/makeself/")
    inarytools.doman("makeself.1")    

    inarytools.dodoc("COPYING", "README*")
