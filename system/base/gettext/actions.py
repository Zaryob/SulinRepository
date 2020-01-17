#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

docdir = "/%s/%s" % (get.docDIR(), get.srcNAME())

shelltools.export("LC_ALL", "C")

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--without-emacs \
                         --enable-nls \
                         --disable-static \
                         --enable-shared \
                         --with-pic \
                         --disable-rpath \
                         --with-included-libcroco")

def build():
    autotools.make("GMSGFMT=../src/msgfmt")

def install():
    autotools.rawInstall("DESTDIR=%s docdir=/%s/html" % (get.installDIR(), docdir))

    inarytools.dobin("gettext-tools/misc/gettextize", "/usr/bin")

    # Remove C# & Java stuff
    inarytools.remove("%s/html/examples/build-aux/csharp*" % docdir)
    inarytools.remove("%s/html/examples/build-aux/java*" % docdir)
    inarytools.removeDir("%s/html/examples/*java*" % docdir)
    inarytools.removeDir("%s/html/*java*" % docdir)

    inarytools.dodoc("AUTHORS", "COPYING", "ChangeLog*", "HACKING", "NEWS", "README*", "THANKS")
