#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -D_GNU_SOURCE" % get.CFLAGS())
    shelltools.system("""sed -i 's/test-lock..EXEEXT.//' tests/Makefile.in  &&
sed -i 's/IO_ftrylockfile/IO_EOF_SEEN/' gl/lib/*.c &&
sed -i '/unistd/a #include <sys/sysmacros.h>' gl/lib/mountlist.c &&
echo "#define _IO_IN_BACKUP 0x100" >> gl/lib/stdio-impl.h""")

    autotools.configure("""--enable-nls \
                         --with-packager="Sulin" \
                         --with-packager-version="4.6.0" \
                         --with-packager-bug-reports="https://github.com/SulinOS/SulinRepository/issues" \
                         --localstatedir=/var/lib/locate \
                         --without-included-regex \
                         --disable-rpath \
                         --disable-assert \
                         --with-fts \
                         --enable-leaf-optimisation \
                         --enable-d_type-optimization""")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("ChangeLog", "NEWS", "TODO", "README")
