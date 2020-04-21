# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools



def setup():
    inarytools.cxxflags.remove("-fPIC")
    shelltools.export("SHELL", "/bin/bash")
    shelltools.makedirs("moz-build")
    shelltools.cd("moz-build")
    shelltools.system(" ../js/src/configure   --prefix=/usr       \
                        --disable-debug                    \
                        --disable-debug-symbols            \
                        --disable-jemalloc                 \
                        --disable-strip                    \
                        --enable-hardening                 \
                        --enable-linker=gold               \
                        --enable-optimize                  \
                        --enable-posix-nspr-emulation      \
                        --enable-readline                  \
                        --enable-release                   \
                        --enable-shared-js                 \
                        --enable-tests                     \
                        --with-intl-api                    \
                        --with-system-zlib                 \
                        --without-system-icu")
def build():
    shelltools.cd("moz-build")
    shelltools.export("SHELL", "/bin/bash")
    autotools.make()


def install():
    shelltools.cd("moz-build")
    shelltools.export("SHELL", "/bin/bash")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #BUG: at issue #24 in gitlab
    inarytools.remove("/usr/lib/*.ajs")
