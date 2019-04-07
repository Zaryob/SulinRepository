 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get
from inary.actionsapi import shelltools

def setup():
    autotools.configure("--libexecdir=/usr/lib/dhcpcd \
                         --dbdir=/var/lib/dhcpcd \
                         --localstatedir=/var \
                         --sbindir=/usr/bin \
                         --rundir=/run")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    # Set Options in /etc/dhcpcd.conf Disable ip4vall
    shelltools.echo("%s/etc/dhcpcd.conf" % get.installDIR(), "noipv4ll")
    # Remove hooks install the compat one
    inarytools.remove("/usr/lib/dhcpcd/dhcpcd-hooks/*")
    inarytools.insinto("/usr/lib/dhcpcd/dhcpcd-hooks", "hooks/50-dhcpcd-compat")

    inarytools.dodoc("README.md")
#DBDIR=/var/lib/dhcpcd LIBEXECDIR=/usr/lib/dhcpcd
