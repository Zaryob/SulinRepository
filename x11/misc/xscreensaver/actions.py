#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Süleyman POYRAZ (Zaryob)
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.autoconf()
    autotools.configure("--with-x-app-defaults=/usr/share/X11/app-defaults \
    --with-pam \
    --with-login-manager \
    --with-gtk \
    --with-gl \
    --without-gle \
    --with-pixbuf \
    --with-jpeg")

def build():
    autotools.make()

def install():
    inarytools.dodir("/etc/pam.d")

    autotools.rawInstall("install_prefix=%s" % get.installDIR())
    f=open("{}//etc/pam.d/xscreensaver".format(get.installDIR()),"w")
    f.write("# Begin /etc/pam.d/xscreensaver\n")
    f.write("auth    include system-auth\n")
    f.write("account include system-account\n")
    f.write("# End /etc/pam.d/xscreensaver\n")
    f.close()

