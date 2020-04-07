#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get
from inary.actionsapi import shelltools

def setup():
    shelltools.export("SYSTEMD_LIBS","-lelogind")
    shelltools.export("SYSTEMD_CFLAGS","-I/usr/include/elogind")
    shelltools.system("sed 's@systemd@elogind@' -i data/pam-lfs/gdm-launch-environment.pam")
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--disable-static \
		--without-plymouth \
		--with-initial-vt=1 \
		--enable-wayland-support \
		--without-tcp-wrappers \
		--with-pid-file=/var/run/gdm.pid \
		--enable-authentication-scheme=pam \
		--with-default-pam-config=arch \
		--with-log-dir=/var/log/gdm \
		--with-pam-mod-dir=/lib/security")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.system('sed -i "s/pam_systemd\.so/pam_elogind.so/" {}/etc/pam.d/*'.format(get.installDIR()))

