#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools

libdir = "lib32" if get.buildTYPE() == "emul32" else "lib"
jobs = get.makeJOBS().replace("-j", "")

def setup():
    autotools.configure("\
                         --sysconfdir=/etc/samba \
                         --builtin-libraries=replace \
                         --bundled-libraries=NONE \
                         --disable-rpath \
                         --disable-rpath-install \
                         --disable-silent-rules \
                         --enable-talloc-compat1 \
                        ")

def build():
    autotools.make("JOBS=%s" % jobs)

def install():
    autotools.rawInstall("DESTDIR=%s JOBS=%s" % (get.installDIR(), jobs))

    #inarytools.removeDir("/usr/share/swig")

    #inarytools.remove("/usr/lib*/*.a")
    #inarytools.remove("/usr/lib*/libtalloc-compat1-%s.so" % get.srcVERSION())

    # Create symlinks for so file
    #inarytools.dosym("libtalloc.so.%s" % get.srcVERSION(), "/usr/%s/libtalloc.so.%s" % (libdir, get.srcVERSION().split(".")[0]))
    #inarytools.dosym("libtalloc.so.%s" % get.srcVERSION(), "/usr/%s/libtalloc.so" % libdir)

    inarytools.dodoc("NEWS")
