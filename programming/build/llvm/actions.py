# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get
from inary.actionsapi import cmaketools

libdir = "/usr/lib32/llvm" if get.buildTYPE() == "emul32" else "/usr/lib/llvm"
lib = "lib32" if get.buildTYPE() == "emul32" else "lib"

WorkDir="llvm-10.0.0.src"


def setup():
    shelltools.export("PYTHON", "/usr/bin/python3")
    for dirs in ["tools", "projects"]:
        if not shelltools.can_access_directory(dirs):
            shelltools.makedirs(dirs)
        
    if not shelltools.can_access_directory("tools/clang"):
        shelltools.system("tar -xvf ../clang-%s.src.tar.xz -C tools" % get.srcVERSION())
        shelltools.move("tools/clang-%s.src" % get.srcVERSION(), "tools/clang")

        shelltools.system("tar -xvf ../clang-tools-extra-%s.src.tar.xz -C tools" % get.srcVERSION())
        shelltools.move("tools/clang-tools-extra-*", "tools/clang/extra")

    if get.buildTYPE() != "emul32":
        shelltools.system("tar -xvf ../lldb-%s.src.tar.xz -C tools" % get.srcVERSION())
        shelltools.move("tools/lldb-*", "tools/lldb")

    if not shelltools.can_access_directory("tools/polly"):
        shelltools.system("tar -xvf ../polly-%s.src.tar.xz -C tools" % get.srcVERSION())
        shelltools.move("tools/polly-*", "tools/polly")

    if not shelltools.can_access_directory("projects/compiler-rt"):
        shelltools.system("tar -xvf ../compiler-rt-%s.src.tar.xz -C projects" % get.srcVERSION())
        shelltools.move("projects/compiler-rt-%s.src" % get.srcVERSION(), "projects/compiler-rt")


        shelltools.export("CC", "gcc")
        shelltools.export("CXX", "g++")


    if get.buildTYPE() == "emul32":
        shelltools.export("CC", "gcc -m32")
        shelltools.export("CXX", "g++ -m32")
        shelltools.export("PKG_CONFIG_PATH","/usr/lib32/pkgconfig")

    shelltools.makedirs("inary-build")

    shelltools.cd("inary-build")

    if get.buildTYPE() != "emul32":
        options = "-DCMAKE_C_FLAGS:STRING=-m64 \
                            -DCMAKE_INSTALL_PREFIX=/usr \
                            -DCMAKE_CXX_FLAGS:STRING=-m64 \
                            -DLLVM_TARGET_ARCH:STRING=x86_64 \
                            -DLLVM_DEFAULT_TARGET_TRIPLE=%s " % get.HOST()


    if get.buildTYPE() == "emul32":
        options = "  -DCMAKE_C_FLAGS:STRING=-m32 \
                            -DCMAKE_INSTALL_PREFIX=/emul32 \
                            -DLLVM_TARGET_ARCH:STRING=i686  \
                            -DLLVM_INCLUDE_TESTS=NO \
                            -DLLVM_LIBDIR_SUFFIX=32 \
                            -DLLVM_DEFAULT_TARGET_TRIPLE='i686-pc-linux-gnu' \
                            -DCMAKE_CXX_FLAGS:STRING=-m32"


    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                                        %s \
                                        -DLLVM_ENABLE_FFI=ON \
                                        -DLLVM_BUILD_DOCS=OFF \
                                        -DBUILD_SHARED_LIBS=ON \
                                        -DLLVM_ENABLE_RTTI=ON \
                                        -DLLVM_INCLUDEDIR=/usr/include \
                                        -DLLVM_ENABLE_ASSERTIONS=OFF \
                                        -DPOLLY_ENABLE_GPGPU_CODEGEN=ON \
                                        -DFFI_INCLUDE_DIR=/usr/lib/libffi-3.2.1/include \
                                        -DENABLE_SHARED=ON" % options, sourceDir=".." )

def build():
    shelltools.export("PYTHON", "/usr/bin/python3")
    shelltools.makedirs("inary-build")
    shelltools.cd("inary-build")

    cmaketools.make()

def install():
    shelltools.makedirs("inary-build")
    shelltools.cd("inary-build")

    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":

        inarytools.domove("/emul32/lib32/", "/usr/")
        inarytools.insinto("/usr/include/llvm/Config/","%s/emul32/include/llvm/Config/llvm-config.h" % get.installDIR(),"llvm-config-32.h")
        inarytools.insinto("/usr/bin/","%s/emul32/bin/llvm-config" % get.installDIR(),"llvm-config-32")
        inarytools.removeDir("/emul32")
        return
    inarytools.remove("/usr/lib/python3.8/site-packages/six.py")

    shelltools.cd ("..")

    inarytools.dodoc("CREDITS.TXT", "LICENSE.TXT", "README.txt")
