#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    #write sed comands using inarytools.dosed
    shelltools.system('sed -i "/gets is a security hole/d" lib/stdio.in.h')

    # disable automagic libsigsegv dependency
    shelltools.export("AUTOPOINT", "true")
    shelltools.export("ac_cv_libsigsegv", "no")

    autotools.autoreconf("-vfi")
    autotools.configure("""--with-packager="Sulin" \
                           --with-packager-version="3.6" \
                           --with-packager-bug-reports="https://gitlab.com/sulinos/main/issues" \
                           --enable-nls""")

def build():
    autotools.make('LDFLAGS="%s"' % get.LDFLAGS())

#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("ChangeLog", "NEWS", "README")
