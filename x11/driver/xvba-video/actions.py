# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir = "%s-%s.%s" % (get.srcNAME(), get.srcVERSION(), get.ARCH())

def install():
    if get.buildTYPE() == "emul32":
        inarytools.insinto("/usr/lib32", "../%s-%s.i686/usr/lib/*" % (get.srcNAME(), get.srcVERSION()))
        return
    else:
        inarytools.insinto("/usr/lib", "usr/lib/*")

    inarytools.dodoc("AUTHORS", "COPYING", "NEWS", "README")
