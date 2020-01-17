# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import get
from inary.actionsapi import shelltools

#WorkDir = "broadcom-wl-%s" % get.srcVERSION()

def install():
    inarytools.dodir("/lib/firmware")

    for obj in ("wl_apsta-3.130.20.0.o", "broadcom-wl-6.30.163.46.wl_apsta.o"):
        shelltools.system("b43-fwcutter -w %s/lib/firmware %s" % (get.installDIR(), obj))
