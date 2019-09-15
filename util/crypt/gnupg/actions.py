#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    #shelltools.export("CFLAGS","%s -fPIE" % get.CFLAGS())
    #shelltools.export("LDFLAGS", "%s -pie -Wl,-z,relro,-z,now"  % get.LDFLAGS())

    autotools.configure("--enable-symcryptrun \
                         --disable-rpath \
                         --enable-gpgtar \
                         --enable-maintainer-mode")

def build():
    autotools.make("-j1")
    autotools.make("-C doc html")

def check():
    autotools.make("check")

def install():
    autotools.rawInstall('DESTDIR=%s libexecdir="/usr/libexec"' % get.installDIR())

    # Compat symlinks
    inarytools.dosym("gpg2", "/usr/bin/gpg")
    inarytools.dosym("gpgv2", "/usr/bin/gpgv")
    inarytools.dosym("gpg2.1", "/usr/share/man/man1/gpg.1")
    inarytools.dosym("gpgv2.1", "/usr/share/man/man1/gpgv.1")

    # Lets make doc
    inarytools.dohtml("doc/*")
    inarytools.dohtml("doc/gnupg.html/*")
    inarytools.dodoc("ChangeLog", "NEWS", "README", "THANKS", "TODO")
