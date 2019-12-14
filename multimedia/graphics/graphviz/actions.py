#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    shelltools.system("./autogen.sh")

    autotools.configure("\
                         --disable-dependency-tracking \
                         --disable-io \
                         --disable-lua \
                         --disable-ocaml \
                         --disable-php \
                         --disable-r \
                         --disable-rpath \
                         --disable-sharp \
                         --disable-static \
                         --with-devil=no \
                         --with-fontconfig \
                         --with-libgd \
                         --with-pangocairo \
                        ")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #remove empty directories
    #for lang in ["lua", "ocaml", "php", "python23", "python24", "python25", "R", "sharp"]:
        #inarytools.removeDir("/usr/lib/graphviz/%s" % lang)



    inarytools.dohtml(".")
    inarytools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README*")

    inarytools.removeDir("/usr/share/graphviz/doc")

    # everything has been built against cgraph, but use graph as default api
    inarytools.dosed("%s/usr/include/graphviz/types.h" % get.installDIR(), r"#define WITH_CGRAPH 1", deleteLine=True)
