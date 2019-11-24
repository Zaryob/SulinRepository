#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Lime GNU/Linux 2017
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.


from inary.actionsapi import inarytools, get, shelltools, autotools


WorkDir = "node-v%s-linux-x64" % get.srcVERSION()

def install():
    inarytools.insinto("/usr/include" , "include/*")
    inarytools.insinto("/usr/lib" , "lib/*")
    inarytools.insinto("/usr/bin", "bin/*")
    inarytools.dodoc("CHANGELOG.md", "README*", "LICENSE")
