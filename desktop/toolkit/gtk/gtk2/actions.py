#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get
from inary.actionsapi import shelltools
from inary.actionsapi import libtools

def setup():
    options = "--prefix=/usr \
        --sysconfdir=/etc \
        --localstatedir=/var \
        --with-xinput=yes \
        --enable-gtk-doc \
        --enable-test-print-backend"

    #shelltools.export("CFLAGS", get.CFLAGS().replace("-fomit-frame-pointer",""))
    #gtk2 needs -DGTK_COMPILATION CPPFLAG when compiling itself
    #Avoid "Only <gtk/gtk.h> can be included directly error"
    shelltools.export("CPPFLAGS", "-DGTK_COMPILATION")

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32 \
                     --bindir=/usr/bin32 \
                     --sbindir=/usr/sbin32"

        shelltools.export("CC","%s -m32" % get.CC())
        shelltools.export("CXX","%s -m32" % get.CC())
        shelltools.export("CXXFLAGS","-m32")
        shelltools.export("LDFLAGS","-m32")
    else:
        shelltools.export("CFLAGS","")
        shelltools.export("CXXFLAGS","")
        shelltools.export("LDFLAGS","")
        
    autotools.autoconf()
    autotools.configure(options)

    inarytools.dosed("libtool"," -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # fix conflict with gtk3
    #inarytools.removeDir("/usr/share/man")

    inarytools.dodoc("AUTHORS", "README*", "HACKING", "ChangeLog*", "NEWS*")

    if get.buildTYPE() == "emul32":
        for binaries in ["gtk-query-immodules-2.0", "gtk-demo"]:
            inarytools.domove("/usr/bin32/%s" % binaries, "/usr/bin/", "%s-32bit" % binaries)
        inarytools.removeDir("/usr/bin32")
        #hack to install gdkconfig.h in gdk headers dir
        inarytools.dosym("/usr/lib/gtk-2.0/include/gdkconfig.h","/usr/include/gtk-2.0/gdk/gdkconfig.h")
