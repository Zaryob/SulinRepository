# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get


def install():
    inarytools.dodir("/usr/include")
    inarytools.dodir("/usr/lib")
    inarytools.dodir("/usr/lib/pkgconfig")
    inarytools.readable_insinto("{}/usr/include/".format(get.installDIR()), "interface/*.h")
    inarytools.readable_insinto("{}/usr/lib/pkgconfig/".format(get.installDIR()),"*.pc")
