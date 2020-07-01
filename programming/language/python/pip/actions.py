#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import pythonmodules
from inary.actionsapi import shelltools
from inary.actionsapi import get
from inary.actionsapi import inarytools

WorkDir="pip-%s" % get.srcVERSION()

def setup():
    pythonmodules.compile(pyVer="3")


def install():
    pythonmodules.install(pyVer="3")
    inarytools.rename("/usr/bin/pip", "pip3")
    inarytools.dosym("pip3", "/usr/bin/pip")



    shelltools.system("sed -i 's|#!/usr/bin/env python$|#!/usr/bin/env python3|' %s/usr/lib/python3.*/site-packages/pip/__init__.py" % get.installDIR())
    shelltools.system("python3 -m compileall %s/usr/lib/python3.*/site-packages/pip/__init__.py" % get.installDIR())
