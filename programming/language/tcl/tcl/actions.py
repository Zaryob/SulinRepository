# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import get
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    sql_ver="3.30.1.2"
    shelltools.unlinkDir("{}/tcl{}/pkgs/sqlite{}".format(get.workDIR(), get.srcVERSION(), sql_ver))
    shelltools.cd("unix")

    autotools.autoreconf("-fi")
    if get.buildTYPE()=="emul32":
        option="--enable-32bit"
    else:
        option="--enable-64bit"
    autotools.configure("--with-encoding=utf-8 \
                         --enable-threads \
                         --enable-man-compression=gzip \
                         --mandir=/usr/share/man \
                         --enable-man-symlinks \
                         --enable-shared \
                         {}".format(option))
def build():
    shelltools.cd("unix")
    autotools.make()

def install():
    shelltools.cd("unix")
    if get.buildTYPE()=="emul32":
        autotools.rawInstall("DESTDIR=%s" % get.installDIR())
        return
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Collect private headers, 3rd party apps like Tile depends on this
    shelltools.cd("..")
    inarytools.dodir("/usr/include/tcl-private/generic")
    inarytools.dodir("/usr/include/tcl-private/unix")
    shelltools.copy("unix/*.h","%s/usr/include/tcl-private/unix" % get.installDIR())
    shelltools.copy("generic/*.h", "%s/usr/include/tcl-private/generic" % get.installDIR())

    # Remove duplicated headers
    inarytools.remove("/usr/include/tcl-private/generic/tcl.h")
    inarytools.remove("/usr/include/tcl-private/generic/tclDecls.h")
    inarytools.remove("/usr/include/tcl-private/generic/tclPlatDecls.h")

    # Expect package needs these symlinks
    inarytools.dosym("../unix/tclUnixPort.h","/usr/include/tcl-private/generic/tclUnixPort.h")
    inarytools.dosym("../unix/tclUnixThrd.h","/usr/include/tcl-private/generic/tclUnixThrd.h")

    # Remove tmp path from tclConfig.sh
    inarytools.dosed("%s/usr/lib/tclConfig.sh" % get.installDIR(),"%s/unix" % get.curDIR() ,"/usr/lib/")
    inarytools.dosed("%s/usr/lib/tclConfig.sh" % get.installDIR(),"%s" % get.curDIR() ,"/usr/include/tcl-private")

    # Some apps need compat headers
    inarytools.dodir("/usr/include/tcl-private/compat")
    shelltools.copy("compat/*.h", "%s/usr/include/tcl-private/compat" % get.installDIR())

    inarytools.dosym("tclsh8.6","/usr/bin/tclsh")

    inarytools.dodoc("ChangeLog","changes","license.terms","README.md")
