#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

shelltools.export("LC_ALL", "POSIX")

def setup():
    autotools.configure("--enable-pam \
                         --with-socket-dir=/run/screen \
                         --with-sys-screenrc=/etc/screenrc \
                         --with-pty-mode=0620 \
                         --with-pty-group=5 \
                         --enable-rxvt_osc \
                         --enable-telnet \
                         --enable-colors256")

def build():
    autotools.make()

def install():
    inarytools.dobin("screen")

    inarytools.dodir("/run/screen")
    inarytools.dodir("/etc/pam.d")

    inarytools.insinto("/usr/share/terminfo", "terminfo/screencap")
    inarytools.insinto("/usr/share/screen/utf8encodings", "utf8encodings/??")

    shelltools.chmod("%s/run/screen" % get.installDIR(), 0o775)

    inarytools.doman("doc/screen.1")
    inarytools.dodoc("README", "ChangeLog", "TODO", "NEWS*", "doc/FAQ", "doc/README.DOTSCREEN")
