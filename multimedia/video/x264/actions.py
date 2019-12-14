#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

verMAJOR = "157"
verMINOR = "0"
staticlibfile = "/usr/lib/libx264.a"

inarytools.cflags.sub("-O[\ds]", "-O3")

def getMinorVersion():
    f = file("x264.h").read()
    for i in f.split("\n"):
        if i.startswith("#define X264_BUILD"):
            return i.split()[-1]

    return "0"

def setup():
    shelltools.export("CFLAGS", "%s -O3" % get.CFLAGS())

    # force using shared gpac
    inarytools.dosed("configure", "-lgpac_static", "-lgpac")

    # these disables are here to prevent circular deps, especially with ffmpeg
    # Not delete --bit-depth=8 \
    autotools.rawConfigure("--prefix=/usr \
                            --enable-pic \
                            --enable-shared \
                            --disable-avs \
                            --disable-ffms \
                            --disable-lavf \
                            --disable-swscale \
                            --bit-depth=10 \
                            --bit-depth=8 \
                           ")

def build():
    autotools.make()

def install():
    autotools.install()

    #verMINOR = getMinorVersion()
    inarytools.dosym("libx264.so.%s" % (verMAJOR), "/usr/lib/libx264.so.%s" % (verMINOR))

    # No static libs
    if shelltools.isFile("%s/%s" % (get.installDIR(), staticlibfile)):
        inarytools.remove(staticlibfile)

