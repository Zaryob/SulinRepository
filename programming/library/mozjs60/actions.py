# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools



WorkDir = "mozjs-%s/js/src" % get.srcVERSION()

def setup():
    inarytools.cxxflags.remove("-fPIC")
    shelltools.export("SHELL", "/bin/bash")
    shelltools.makedirs("moz-build")
    shelltools.cd("moz-build")
    shelltools.system(" ../configure   --prefix=/usr       \
                            --with-intl-api     \
                            --with-system-zlib  \
                            --with-system-icu   \
                            --disable-jemalloc  \
                            --enable-readline  ")

def build():
    shelltools.cd("moz-build")
    shelltools.export("SHELL", "/bin/bash")
    autotools.make()


def install():
    shelltools.cd("moz-build")
    shelltools.export("SHELL", "/bin/bash")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
