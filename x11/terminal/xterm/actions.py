# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure(" \
             --disable-full-tgetent \
             --with-app-defaults=/usr/share/X11/app-defaults \
             --disable-desktop \
             --with-utempter \
             --with-tty-group=tty \
             --enable-256-color \
             --enable-exec-xterm \
             --enable-freetype \
             --enable-luit \
             --enable-wide-chars \
             --enable-warnings \
            ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.removeDir("/usr/share/pixmaps")

    inarytools.dodoc("README.i18n", "xterm.log.html", "ctlseqs.txt", "16colors.txt")
