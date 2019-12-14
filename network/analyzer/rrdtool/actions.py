#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import perlmodules
from inary.actionsapi import get


def setup():
    shelltools.export("AUTOPOINT", "/bin/true")
#    autotools.autoreconf("-vfi")
    autotools.configure("--disable-silent-rules \
                         --disable-static \
                         --disable-rpath \
                         --enable-perl \
                         --enable-ruby \
                         --enable-lua \
                         --enable-tcl \
                         --enable-python \
                         --with-rrd-default-font=/usr/share/fonts/dejavu/DejaVuSansMono.ttf \
                         --with-perl-options='installdirs=vendor destdir=%(DESTDIR)s' \
                         --with-ruby-options='sitedir=%(DESTDIR)s/usr/lib/ruby' \
                         " % {"DESTDIR": get.installDIR()})
 
    inarytools.dosed("Makefile", "^RRDDOCDIR.*$", "RRDDOCDIR=${datadir}/doc/${PACKAGE}")
    inarytools.dosed("doc/Makefile", "^RRDDOCDIR.*$", "RRDDOCDIR=${datadir}/doc/${PACKAGE}")
    inarytools.dosed("bindings/Makefile", "^RRDDOCDIR.*$", "RRDDOCDIR=${datadir}/doc/${PACKAGE}")
    inarytools.dosed("examples/Makefile", "examplesdir = .*$", "examplesdir = $(datadir)/doc/${PACKAGE}/examples")
    
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s includedir=/usr/include" % get.installDIR())

    # remove unnecessary files
    perlmodules.removePacklist()
    perlmodules.removePodfiles()
