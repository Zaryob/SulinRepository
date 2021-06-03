# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import mesontools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools


Libdir = "/usr/lib32" if get.buildTYPE() == "emul32" else "/usr/lib"

shelltools.export("CFLAGS","-DUSE_MGL_NAMESPACE")
shelltools.export("CXXFLAGS","-DUSE_MGL_NAMESPACE")
shelltools.export("LDFLAGS","")

def setup():

    options ="\
    -D b_lto=true \
    -D b_ndebug=true \
    -D zstd=disabled \
    -D platforms=x11,wayland \
    -D dri-drivers=i915,i965,r100,r200,nouveau \
    -D gallium-drivers=r300,r600,radeonsi,nouveau,virgl,svga,swrast,swr,iris,zink \
    -D vulkan-drivers=amd,intel,swrast \
    -D vulkan-layers=device-select,intel-nullhw,overlay \
    -D swr-arches=avx,avx2 \
    -D dri3=enabled \
    -D egl=enabled \
    -D gallium-extra-hud=true \
    -D gallium-nine=true \
    -D gallium-omx=bellagio \
    -D gallium-opencl=icd \
    -D gallium-va=enabled \
    -D gallium-vdpau=enabled \
    -D gallium-xa=enabled \
    -D gallium-xvmc=disabled \
    -D gbm=enabled \
    -D gles1=disabled \
    -D gles2=enabled \
    -D glvnd=true \
    -D glx=dri \
    -D libunwind=enabled \
    -D llvm=enabled \
    -D lmsensors=enabled \
    -D osmesa=true \
    -D shared-glapi=enabled \
    -D microsoft-clc=disabled \
    -D valgrind=disabled \
    -D LLVM_BUILD_LLVM_DYLIB=ON \
    -D LLVM_LINK_LLVM_DYLIB=ON "

    if get.buildTYPE() == "emul32":
        shelltools.export("CC","gcc -m32")
        shelltools.export("CXX","g++ -m32")
        options += " --libdir=/usr/lib32 --native-file crossfile.ini"
    else:
        shelltools.export("CC","gcc")
        shelltools.export("CXX","g++")
        options += " --libdir=/usr/lib"


    mesontools.meson_configure(options)

def build():
    #mesontools.ninja_build("xmlpool-pot xmlpool-update-po xmlpool-gmo")
    shelltools.system("meson compile -C inaryPackageBuild")

def install():
    if get.buildTYPE() == "emul32":
        shelltools.system("DESTDIR='{}' ninja -C inaryPackageBuild install".format(get.installDIR()))
        return
    mesontools.ninja_install()

    #inarytools.domove("%s/libGL.so.1.2.0" % Libdir, "%s/mesa" % Libdir)
    #inarytools.dosym("mesa/libGL.so.1.2.0", "%s/libGL.so.1.2" % Libdir)
