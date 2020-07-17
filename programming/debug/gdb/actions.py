#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    inarytools.dosed("config/override.m4", "2.64", "2.69")
    shelltools.system('sed -i "/ac_cpp=/s/\$CPPFLAGS/\$CPPFLAGS -O2/" libiberty/configure')
    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.export("PYTHON", "/usr/bin/python3")
    shelltools.system("../configure \
                       --prefix=/{0} \
                       --build={1} \
                       --mandir=/{2} \
                       --libdir=/{0}/lib \
                       --infodir=/{3} \
                       --datadir=/{4} \
                       --sysconfdir=/{5} \
                       --localstatedir=/{6} \
                       --libexecdir=/{7} \
                       --with-system-readline \
                       --with-separate-debug-dir=/usr/lib/debug \
                       --with-gdb-datadir=/usr/share/gdb \
                       --with-python=/usr/bin/{8} \
                       --with-pythondir=/usr/lib/{8}/site-packages \
                       --disable-nls \
                       --disable-rpath \
                       --with-expat".format(get.defaultprefixDIR(), get.HOST(), get.manDIR(), get.infoDIR(),
                               get.dataDIR(), get.confDIR(), get.localstateDIR(), get.libexecDIR(),
                               get.curPYTHON()))


def build():
    shelltools.cd("build")
    autotools.make()

def install():
    shelltools.cd("build")
    autotools.rawInstall('-C gdb DESTDIR="%s"' % get.installDIR())
    autotools.rawInstall('-C gdb/data-directory DESTDIR="%s"' % get.installDIR())
    # these are not necessary
    #for info in ["bfd","configure","standards"]:
        #inarytools.remove("/usr/share/info/%s.info" % info)
#    for hea in ["diagnostics","bfd_stdint","ansidecl","symcat","dis-asm", "bfd", "bfdlink", "plugin-api"]:
#    inarytools.dodoc("README*", "MAINTAINERS", "COPYING*", "ChangeLog*")    inarytools.remove("/usr/include/%s.h" % hea)
    shelltools.cd("..")
    inarytools.dodoc("README*", "MAINTAINERS", "COPYING*", "ChangeLog*")
