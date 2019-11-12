#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import cmaketools
from inary.actionsapi import get


def setup():
    if get.buildTYPE()=="emul32":
        inarytools.dosed("CMakeLists.txt", 'lib/cmake' 'lib32/cmake')
        inarytools.dosed("CMakeLists.txt", 'pkg_search_module.*ibus-1.0' 'lib32/cmake')
        options = "-DCMAKE_INSTALL_PREFIX=/usr \
                  -DLIB_SUFFIX=32 \
                  -DSDL_STATIC=OFF \
                  -DSDL_DLOPEN=ON \
                  -DARTS=OFF \
                  -DESD=OFF \
                  -DNAS=OFF \
                  -DALSA=ON \
                  -DPULSEAUDIO_SHARED=ON \
                  -DVIDEO_WAYLAND=ON \
                  -DRPATH=OFF \
                  -DCLOCK_GETTIME=ON \
                  -DJACK_SHARED=ON \
                  -DSDL_VIDEO_DRIVER_X11_SUPPORTS_GENERIC_EVENTS=1 \
                  -DSDL_VIDEO_DRIVER_X11_CONST_PARAM_XEXTADDDISPLAY=1 "
    else:
        options = "-DCMAKE_INSTALL_PREFIX=/usr \
                   -DSDL_STATIC=OFF \
                  -DSDL_DLOPEN=ON \
                  -DARTS=OFF \
                  -DESD=OFF \
                  -DNAS=OFF \
                  -DALSA=ON \
                  -DPULSEAUDIO_SHARED=ON \
                  -DVIDEO_WAYLAND=ON \
                  -DRPATH=OFF \
                  -DCLOCK_GETTIME=ON \
                  -DJACK_SHARED=ON"

    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure(options, sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    #inarytools.dosed("/usr/lib/cmake/SDL2/SDL2Targets-noconfig.cmake", "libSDL2.a","libSDL2main.a")

    shelltools.cd("..")
    inarytools.dodoc("COPYING.txt")
