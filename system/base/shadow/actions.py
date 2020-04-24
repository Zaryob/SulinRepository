#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure('--prefix=/usr \
		--sysconfdir=/etc \
		--mandir=/usr/share/man \
		--infodir=/usr/share/info \
		--localstatedir=/var \
		--disable-nls \
		--enable-man \
		--with-libpam \
		--with-audit \
		--without-selinux \
		--without-acl \
		--without-attr \
		--without-tcb \
		--without-nscd \
		--with-group-name-max-length=32')

def build():
    # Rebuild gmo catalogs
    autotools.make("-C po update-gmo")

    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.insinto("/etc/", "etc/login.access")
    shelltools.chmod("%s/etc/login.access" % get.installDIR(), 0o600)

    inarytools.insinto("/etc/", "etc/limits")
    shelltools.chmod("%s/etc/limits" % get.installDIR(), 0o644)

    # groups come from coreutils package
    inarytools.remove("/usr/share/man/man1/groups.1")
    inarytools.remove("/bin/groups")

    # Conflicts with man-pages
    inarytools.remove("/usr/share/man/man3/getspnam.3")
    inarytools.remove("/usr/share/man/man5/passwd.5")

    inarytools.dodoc("ChangeLog","README","NEWS")
