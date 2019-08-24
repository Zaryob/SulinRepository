#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s -C man-pages-posix-2003-a" % get.installDIR())

    # These come from attr
    inarytools.remove("/usr/share/man/man2/flistxattr.2")
    inarytools.remove("/usr/share/man/man2/removexattr.2")
    inarytools.remove("/usr/share/man/man2/fgetxattr.2")
    inarytools.remove("/usr/share/man/man2/fsetxattr.2")
    inarytools.remove("/usr/share/man/man2/lsetxattr.2")
    inarytools.remove("/usr/share/man/man2/lremovexattr.2")
    inarytools.remove("/usr/share/man/man2/listxattr.2")
    inarytools.remove("/usr/share/man/man2/getxattr.2")
    inarytools.remove("/usr/share/man/man2/setxattr.2")
    inarytools.remove("/usr/share/man/man2/llistxattr.2")
    inarytools.remove("/usr/share/man/man2/fremovexattr.2")
    inarytools.remove("/usr/share/man/man2/lgetxattr.2")
    inarytools.remove("/usr/share/man/man5/attr.5")

    # These come from libcap
    inarytools.remove("/usr/share/man/man2/capget.2")
    inarytools.remove("/usr/share/man/man2/capset.2")

    # Comes from xorg-input
    inarytools.remove("/usr/share/man/man4/mouse.4")
    
    # Comes from keyutils
    inarytools.remove("/usr/share/man/man7/*-keyring.7")
    inarytools.remove("/usr/share/man/man7/keyrings.7")

    inarytools.dodoc("man-pages-*.Announce", "README")
