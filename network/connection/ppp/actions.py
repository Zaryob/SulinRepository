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
    inarytools.cflags.add("-fPIC", "-D_GNU_SOURCE")
    shelltools.copytree("%s/dhcp" % get.workDIR(), "pppd/plugins")
    inarytools.dosed("pppd/plugins/dhcp/Makefile.linux", "^(CFLAGS=.+)\s-O2", "\\1 %s" % get.CFLAGS())

    # Enable atm
    inarytools.dosed("pppd/Makefile.linux", "^#(HAVE_LIBATM=yes)", "\\1")
    # Enable pam
    inarytools.dosed("pppd/Makefile.linux", "^#(USE_PAM=y)", "\\1")
    # Enable CBCP
    inarytools.dosed("pppd/Makefile.linux", "^#(CBCP=y)", "\\1")
    # Enable IPv6
    inarytools.dosed("pppd/Makefile.linux", "^#(HAVE_INET6)", "\\1")
    # Enable dhcp
    inarytools.dosed("pppd/plugins/Makefile.linux", "^(SUBDIRS\s:=.+)", "\\1 dhcp")

    autotools.configure()

def build():
    autotools.make()

def install():
    # The build mechanism is crap. Don't remove \/usr from DESTDIR or else the paths will fail
    autotools.rawInstall("DESTDIR=%s/usr INSTROOT=%s install-etcppp" % ((get.installDIR(),)*2))

    # No suid libraries
    shelltools.chmod("%s/usr/lib/pppd/%s/*.so" % (get.installDIR(),get.srcVERSION()), 0o755)

    # Install Radius config files
    inarytools.insinto("/etc/radiusclient", "pppd/plugins/radius/etc/*")

    # Create peers directory
    inarytools.dodir("/run/ppp")
    inarytools.dodir("/etc/ppp/peers")

    inarytools.dodoc("Changes*", "README*", "FAQ")
