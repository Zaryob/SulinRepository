#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import shelltools
from inary.actionsapi import inarytools

if get.buildTYPE() == "emul32":
    shelltools.export("CC", "gcc -m32")
    shelltools.export("CXX", "g++ -m32")
    shelltools.export("LDFLAGS","-m32")
    shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
    
def setup():
    shelltools.system("sed -i s/3000/5000/ libxslt/transform.c doc/xsltproc.{1,xml}")
    shelltools.system("sed -e 's@http://cdn.docbook.org/release/xsl@https://cdn.docbook.org/release/xsl-nons@' \
    -e 's@\$Date\$@31 October 2019@' -i doc/xsltproc.xml")
    config_opt="--disable-static --without-threads"
    if get.buildTYPE() == "emul32":    
        config_opt+=" --without-python"
    else:
        if get.buildTYPE()=="rebuild_python":
            config_opt+=" --with-python=python2 "
        else:
            shelltools.export("PYTHON", "python3.8")
            config_opt+=" --with-python=python3 "
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")

    autotools.configure(config_opt)

def build():
    
    autotools.make()

#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "ChangeLog", "Copyright", "FEATURES", "NEWS", "README", "TODO")
