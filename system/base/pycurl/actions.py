#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import pythonmodules
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

shelltools.export("PYCURL_SSL_LIBRARY", "openssl")

def install():
    # no static libs
    inarytools.dosed("setup.py", ", \"--static-libs\"")
    if get.buildTYPE()=="rebuild_python":
        pyVer=3
    else:
        pyVer=2.7
    pythonmodules.install("--curl-config=/usr/bin/curl-config --prefix=/usr --optimize=1", pyVer=pyVer)


    inarytools.dodoc("ChangeLog", "COPYING*")
