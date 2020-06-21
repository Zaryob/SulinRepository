# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import get
from inary.actionsapi import shelltools


def setup():
    if get.buildTYPE()=="emul32":
        shelltools.system("./bootstrap.sh --with-toolset=gcc --with-icu --prefix=%s/emul32/usr" % get.installDIR())
    elif get.buildTYPE()=="rebuild_python":
        shelltools.system("./bootstrap.sh --with-toolset=gcc --with-icu --with-python=python3 --prefix=%s/usr" % get.installDIR())
    else:
        shelltools.system("./bootstrap.sh --with-toolset=gcc --with-icu --with-python=python2 --prefix=%s/usr" % get.installDIR())


def build():
    if get.buildTYPE()=="emul32":
        shelltools.export("PKG_CONFIG_PATH", '/usr/lib32/pkgconfig')
        shelltools.system("./b2 \
                           stage \
                           -j 1\
                           variant=release \
                           debug-symbols=off \
                           threading=multi \
                           runtime-link=shared \
                           link=shared,static \
                           toolset=gcc \
                           address-model=32 \
                           --without-python \
                           cflags=-fno-strict-aliasing \
                           --layout=system")

    elif get.buildTYPE()=="rebuild_python":
        shelltools.system("./b2 \
                           stage \
                           -j 1 \
                           variant=release \
                           debug-symbols=off \
                           threading=multi \
                           runtime-link=shared \
                           link=shared,static \
                           toolset=gcc \
                           --with-python \
                           python=3.8 \
                           cflags=-fno-strict-aliasing \
                           --layout=system")

    else:
        shelltools.system("./b2 \
                           stage \
                           -j 1 \
                           variant=release \
                           debug-symbols=off \
                           threading=multi \
                           runtime-link=shared \
                           link=shared,static \
                           toolset=gcc \
                           --with-python \
                           python=2.7 \
                           cflags=-fno-strict-aliasing \
                           --layout=system")
def install():
    if get.buildTYPE()=="emul32":
        shelltools.system("./b2 install threading=multi link=shared")
        shelltools.system("mv %s/emul32/usr/lib %s/usr/lib32" %(get.installDIR(), get.installDIR()))
        shelltools.system("rm -rf  %s/emul32" % get.installDIR())
        return
    shelltools.system("./b2 install --with-python threading=multi link=shared")
    inarytools.dobin("b2")
    inarytools.dosym("b2", "/usr/bin/bjam")
    shelltools.copytree("tools/boostbook/xsl", "%s/usr/share/boostbook/xsl" % get.installDIR())
    shelltools.copytree("tools/boostbook/dtd", "%s/usr/share/boostbook" % get.installDIR())
