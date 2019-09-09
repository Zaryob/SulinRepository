# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools


Libdir = "/usr/lib32" if get.buildTYPE() == "emul32" else "/usr/lib"

def setup():
    autotools.autoreconf("-vif")

# --enable-sysfs option provides better hardware information support with "lspci"
# --enable-32-bit option is not present anymore. Although build fails in emul32. With --disable-asm option, not fail. Needs to be tested.

    options ="PYTHON=/usr/bin/python3 \
                        --prefix=/usr \
          		--sysconfdir=/etc \
           		--enable-llvm \
          		--enable-gbm \
          		--enable-gles1 \
          		--enable-gles2 \
          		--enable-glx-tls \
          		--enable-osmesa \
          		--enable-texture-float \
                        --enable-autotools \
          		--enable-xa \
          		--enable-vdpau \
          		--enable-llvm-shared-libs \
          		--disable-dependency-tracking \
          		--with-platforms=x11,drm,wayland \
          		--with-gallium-drivers=r300,r600,radeonsi,nouveau,virgl,svga,swrast \
                        --with-dri-drivers=i915,i965,r200,nouveau \
                        --with-vulkan-drivers=intel,radeon"

    if get.buildTYPE() == "emul32":
        shelltools.export("PKG_CONFIG_PATH","/usr/lib32/pkgconfig")
        shelltools.export("LLVM_CONFIG","/usr/bin/llvm-config-32")        
        options += " --with-dri-driverdir=/usr/lib32/xorg/modules/dri \
                            --with-clang-libdir=/usr/lib32 \
                            --disable-asm "

    elif get.ARCH() == "x86_64":
        options += " --with-clang-libdir=/usr/lib \
                            --enable-omx-bellagio \
                            --enable-opencl-icd "

    autotools.configure(options)
    inarytools.dosed("libtool","( -shared )", " -Wl,--as-needed\\1")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #inarytools.domove("%s/libGL.so.1.2.0" % Libdir, "%s/mesa" % Libdir)
    #inarytools.dosym("mesa/libGL.so.1.2.0", "%s/libGL.so.1.2" % Libdir)

    if get.buildTYPE() == "emul32":
        return

    #inarytools.dodoc("docs/COPYING")
    inarytools.dohtml("docs/*")
