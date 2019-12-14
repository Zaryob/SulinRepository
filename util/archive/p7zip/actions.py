#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir = "p7zip_%s" % get.srcVERSION()

makefiles = {
             'i686'     : "makefile.linux_x86_asm_gcc_4.X",
             'x86_64'   : "makefile.linux_amd64_asm"
            }

def setup():
    shelltools.copy(makefiles[get.ARCH()], "makefile.machine")

    for i in shelltools.ls("makefile.*"):
        inarytools.dosed(i, "^CC=gcc ", "CC=%s " % get.CC())
        inarytools.dosed(i, "^CXX=g\+\+ ", "CXX=%s " % get.CXX())

def build():
    # do not force CC and CXX here since asm build fails
    autotools.make('OPTFLAGS="%s -DHAVE_GCCVISIBILITYPATCH -fvisibility=hidden -fvisibility-inlines-hidden" \
                    all3' % get.CFLAGS())

def install():
    inarytools.insinto("/usr/lib/p7zip","bin/*")

    # p7zip wrapper
    inarytools.dobin("contrib/gzip-like_CLI_wrapper_for_7z/p7zip")
    inarytools.doman("contrib/gzip-like_CLI_wrapper_for_7z/man1/p7zip.1")

    inarytools.dohtml("DOC/MANUAL/*")
    inarytools.dodoc("ChangeLog", "README", "TODO", "DOC/*.txt")
