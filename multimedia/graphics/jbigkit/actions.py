#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def build():
    autotools.make("CC='%s %s' CFLAGS='%s'" % (get.CC(),"-m32 " if get.buildTYPE() == "emul32" else "-m64" ,get.CFLAGS()))


def install():
    destDir="/usr/lib32" if get.buildTYPE() == "emul32" else "/usr/lib"
    inarytools.dolib("libjbig/libjbig.a", destinationDirectory = destDir, mode=755)
    inarytools.dolib("libjbig/libjbig85.a", destinationDirectory = destDir, mode=755)
    inarytools.insinto("/usr/include", "libjbig/jbig.h")
    inarytools.insinto("/usr/include", "libjbig/jbig_ar.h")
    inarytools.insinto("/usr/include", "libjbig/jbig85.h")

    if get.buildTYPE() == "emul32":
        inarytools.dobin("pbmtools/jbgtopbm")
        inarytools.dobin("pbmtools/pbmtojbg")
        inarytools.dobin("pbmtools/jbgtopbm85")
        inarytools.dobin("pbmtools/pbmtojbg85")

        inarytools.doman("pbmtools/jbgtopbm.1", "pbmtools/pbmtojbg.1")

        inarytools.dodoc("ANNOUNCE", "CHANGES", "COPYING", "TODO")
