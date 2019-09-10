#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get
from inary.actionsapi import shelltools


def setup():
    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-fiv")
    autotools.configure("--disable-static \
                         --prefix=/usr \
                         --with-x \
                         --enable-nls \
                         --sysconfdir=/etc \
                         --libexecdir=/usr/libexec/openbox \
                         --enable-startup-notification \
                         --docdir=/%s/%s" % (get.docDIR(), get.srcNAME()))

    inarytools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    inarytools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    inarytools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    # GNOME Panel is no longer available in the official repositories
    inarytools.remove("/usr/bin/gdm-control")
    inarytools.remove("/usr/bin/gnome-panel-control")
    inarytools.remove("/usr/bin/openbox-gnome-session")
    inarytools.remove("/usr/share/man/man1/openbox-gnome-session.1")
    inarytools.remove("/usr/share/xsessions/openbox-gnome.desktop")
    inarytools.removeDir("/usr/share/gnome-session")

    inarytools.dodoc("AUTHORS", "CHANGELOG", "COPYING", "README")
