# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    inarytools.flags.add("-fno-strict-aliasing")
    inarytools.dosed("configure", '(wx_cv_std_libpath="lib)64"', r'\1"')

    autotools.configure("--enable-gtk2 \
                         --enable-shared \
                         --disable-optimise \
                         --disable-debug \
                         --enable-no_deps \
                         --disable-rpath \
                         --enable-intl \
                         --enable-geometry \
                         --enable-timer \
                         --enable-unicode \
                         --enable-sound \
                         --enable-mediactrl \
                         --enable-xrc \
                         --enable-graphics_ctx \
                         --enable-display \
                         --enable-joystick \
                         --disable-gtktest \
                         --disable-sdltest \
                         --disable-precomp-headers \
                         --with-gtk=2 \
                         --with-libpng=sys \
                         --with-libjpeg=sys \
                         --with-libtiff=sys \
                         --with-libxpm=sys \
                         --with-sdl \
                         --without-gnomeprint \
                         --without-gnomevfs \
                         --without-odbc \
                         --with-opengl \
                         --with-regex=builtin \
                         --with-zlib=sys \
                         --with-expat=sys")

def build():
    autotools.make()
    autotools.make("-C contrib")
    autotools.make("-C locale allmo")

def install():
    autotools.install()
    autotools.install("-C contrib")

    # dont add conflicts files
    # inarytools.dodoc("docs/*.txt", "docs/*.htm")
    #inarytools.dosym("/usr/bin/wxrc-2.8", "/usr/bin/wxrc")
    inarytools.dosym("/usr/bin/wx-config-2.8", "/usr/bin/wxconfig")
    # inarytools.rename("/usr/bin/wxrc-2.8", "wxrc")
    # inarytools.rename("/usr/bin/wx-config-2.8", "wxconfig")
