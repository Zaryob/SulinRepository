# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import pythonmodules
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

WorkDir="setuptools-%s" % get.srcVERSION()

def build():
    if get.buildTYPE()=="rebuild_python":
        pythonmodules.run("bootstrap.py", pyVer="3")
        pythonmodules.compile(pyVer="3")
    else:
        pythonmodules.run("bootstrap.py")
        pythonmodules.compile()


def install():
    if get.buildTYPE()=="rebuild_python":
        pythonmodules.install(pyVer="3")
    else:
        pythonmodules.install()
    inarytools.remove("/usr/lib/*/site-packages/setuptools/*.exe")
