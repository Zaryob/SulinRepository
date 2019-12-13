#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

lib_version=get.srcVERSION()[0] + "." + get.srcVERSION()[2] + "." + get.srcVERSION()[3]

def setup():
    # FIXME: shelltools.echo() appends to the end of the file by default so clear them first
    shelltools.unlink('conf-cc')
    shelltools.unlink('conf-ld')
    shelltools.unlink('conf-home')

    shelltools.echo('conf-cc', "%s %s -malign-double -fPIC -DPIC" % (get.CC(), get.CFLAGS().replace("-D_FORTIFY_SOURCE=2", "").replace("-fomit-frame-pointer", "")))
    shelltools.echo('conf-ld', "%s %s" % (get.CC(), get.LDFLAGS()))
    shelltools.echo('conf-home', "%s/usr" % get.installDIR())

def build():
    autotools.make('LIBDJBFFT="libdjbfft.so.%s" LIBPERMS="0755"' % lib_version)

def install():
    inarytools.dolib("libdjbfft.so.%s" % lib_version)
    inarytools.dosym("/usr/lib/libdjbfft.so.%s" % lib_version,"/usr/lib/libdjbfft.so")
    inarytools.dosym("/usr/lib/libdjbfft.so.%s" % lib_version,"/usr/lib/libdjbfft.so.0")

    for header in ["fftc4.h", "complex4.h", "real4.h"]:
        inarytools.insinto("/usr/include", header)

    inarytools.dodoc("CHANGES","README","TODO")
