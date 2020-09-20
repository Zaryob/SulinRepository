# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import mesontools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools


Libdir = "/usr/lib32" if get.buildTYPE() == "emul32" else "/usr/lib"


def clangize():
    clang="{}".format("clang" if get.buildTYPE()!="emul32" else "clang -m32")
    clangpp="{}".format("clang++" if get.buildTYPE()!="emul32" else "clang++ -m32")
    shelltools.export("CC", clang)
    shelltools.export("CXX", clangpp)
def setup():
    #clangize()

    options ="\
    -D b_lto=true \
    -D b_ndebug=true \
    -D platforms=x11,wayland,drm,surfaceless \
    -D dri-drivers=i915,i965,r100,r200,nouveau \
    -D gallium-drivers=r300,r600,radeonsi,nouveau,virgl,svga,swrast,swr,iris,zink \
    -D vulkan-drivers=amd,intel \
    -D vulkan-overlay-layer=true \
    -D vulkan-device-select-layer=true \
    -D swr-arches=avx,avx2 \
    -D dri3=true \
    -D egl=true \
    -D gallium-extra-hud=true \
    -D gallium-nine=true \
    -D gallium-omx=bellagio \
    -D gallium-opencl=icd \
    -D gallium-va=true \
    -D gallium-vdpau=true \
    -D gallium-xa=true \
    -D gallium-xvmc=false \
    -D gbm=true \
    -D gles1=false \
    -D gles2=true \
    -D glvnd=true \
    -D glx=dri \
    -D libunwind=true \
    -D llvm=true \
    -D lmsensors=true \
    -D osmesa=gallium \
    -D shared-glapi=true \
    -D valgrind=false \
    -D zstd=false"
    

    if get.buildTYPE() == "emul32":
        shelltools.export("CC","gcc -m32")
        shelltools.export("CXX","g++ -m32")
        shelltools.export("LDFLAGS","-m32")
        shelltools.export("PKG_CONFIG_PATH","/usr/lib32/pkgconfig")
        options += " --libdir=/usr/lib32 --native-file crossfile.ini"
    else:
        shelltools.export("PKG_CONFIG_PATH","/usr/lib/pkgconfig")
        options += " --libdir=/usr/lib"


    mesontools.meson_configure(options)

def build():
    #clangize()
    mesontools.ninja_build("xmlpool-pot xmlpool-update-po xmlpool-gmo")
    shelltools.system("meson compile -C inaryPackageBuild")

def install():
    #clangize()
    if get.buildTYPE() == "emul32":
        shelltools.system("DESTDIR='{}' ninja -C inaryPackageBuild install".format(get.installDIR()))
        return
    mesontools.ninja_install()

    #inarytools.domove("%s/libGL.so.1.2.0" % Libdir, "%s/mesa" % Libdir)
    #inarytools.dosym("mesa/libGL.so.1.2.0", "%s/libGL.so.1.2" % Libdir)
