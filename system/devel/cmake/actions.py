# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    autotools.rawConfigure("--parallel=%s \
                            --system-libs \
                            --no-qt-gui \
                            --no-system-jsoncpp \
                            --prefix=/usr \
                            --datadir=/share/cmake \
                            --docdir=/share/doc/cmake \
                            --mandir=/share/man" % get.makeJOBS().replace("-j", ""))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
