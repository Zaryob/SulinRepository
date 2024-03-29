# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import get
from inary.actionsapi import shelltools


def setup():
    shelltools.system("./bootstrap.sh --with-toolset=gcc --with-icu --with-python=/usr/bin/python2.7 --prefix=%s/usr" % get.installDIR())
    
    shelltools.echo("project-config.jam","using python : 3.6 : /usr/bin/python3 : /usr/include/python3.6m : /usr/lib ;")
    #shelltools.echo("project-config.jam","--without-mpi ;")

def build():
    shelltools.system("./b2 \
                       variant=release \
                       debug-symbols=off \
                       threading=multi \
                       runtime-link=shared \
                       link=shared,static \
                       toolset=gcc \
                       python=2.7 \
                       cflags=-fno-strict-aliasing \
                       --layout=system")

def install():
    inarytools.dobin("b2")
    inarytools.dobin("bjam")
    shelltools.copytree("tools/boostbook/xsl", "%s/usr/share/boostbook/xsl" % get.installDIR())
    shelltools.copytree("tools/boostbook/dtd", "%s/usr/share/boostbook" % get.installDIR())
    shelltools.system("./b2 install threading=multi link=shared")
