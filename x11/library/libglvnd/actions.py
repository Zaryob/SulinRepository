#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Lime GNU/Linux 2017
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import get, mesontools



def setup():
    mesontools.meson_configure("-D gles1=false")
    
def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()
    #fix conflict with mesa
    for file in ["libGL.so","libGLESv2.so.2","libEGL.so.1","libGL.so.1","libEGL.so","libGLESv2.so"]:
        inarytools.remove("/usr/lib/{}".format(file))
    # fix conflict with mesa-devel
    for file in [  "/GLES3/gl31.h" , "/GLES3/gl3platform.h" , "/GLES3/gl3.h" , "/GLES3/gl3ext.h" , "/GLES3/gl32.h" , "/KHR/khrplatform.h" , "/GL/gl.h" , "/GL/glcorearb.h" , "/GL/glx.h" , "/GL/glext.h" , "/GL/glxext.h" , "/EGL/egl.h" , "/EGL/eglplatform.h" , "/EGL/eglext.h" , "/GLES2/gl2platform.h" , "/GLES2/gl2.h" , "/GLES2/gl2ext.h" ]:
        inarytools.remove("/usr/include/{}".format(file))
    for file in [ "glesv2.pc" , "gl.pc" , "egl.pc" ]:
        inarytools.remove("/usr/lib/pkgconfig/{}".format(file))
