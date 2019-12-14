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
    autotools.configure("PYTHON=/usr/bin/python3 \
                         --enable-gpl \
                         --enable-gpl3 \
                         --enable-gtk2 \
                         --enable-gtk3 \
                         --qt-libdir=/usr/lib/ \
                         --qt-includedir=/usr/include/qt5 \
                         --avformat-swscale")

    # Enable bindings
    shelltools.echo("%s/src/swig/config.mak" % get.curDIR(), "SUBDIRS = perl python")

def build():
    autotools.make()
    autotools.make("-C src/swig")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # We should manually install the bindings :(
    inarytools.insinto("/usr/lib/python3.7/site-packages/", "src/swig/python/mlt.py")
    inarytools.dolib("src/swig/python/_mlt.so", "/usr/lib/python3.7/site-packages/")

    inarytools.insinto("/usr/lib/perl5/vendor_perl/{}/".format(get.curPERL()), "src/swig/perl/blib/lib/mlt.pm")
    inarytools.dolib("src/swig/perl/blib/arch/auto/mlt/mlt.so", "/usr/lib/perl5/vendor_perl/{}/i686-linux-thread-multi/auto/mlt/".format(get.curPERL()))

    inarytools.dodoc("ChangeLog", "COPYING", "GPL*", "README")
