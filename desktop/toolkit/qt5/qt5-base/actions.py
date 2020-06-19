#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import qt
from inary.actionsapi import get

import os

WorkDir = "qtbase-everywhere-src-%s" % get.srcVERSION().replace('_','-').replace('pre1', 'tp')

qtbase = qt.prefix
absoluteWorkDir = "%s/%s" % (get.workDIR(), WorkDir)

#Temporary bindir to avoid qt4 conflicts
bindirQt5="/usr/lib/qt5/bin"

def setup():
    checkdeletepath="%s/qtbase/src/3rdparty"  % absoluteWorkDir
    for dir in ('libjpeg', 'freetype', 'libpng', 'zlib', "xcb", "sqlite"):
        if os.path.exists(checkdeletepath+dir):
            shelltools.unlinkDir(checkdeletepath+dir)

    filteredCFLAGS = get.CFLAGS().replace("-g3", "-g")
    filteredCXXFLAGS = get.CXXFLAGS().replace("-g3", "-g")

    vars = {"SULIN_CC" :       get.CC() + (" -m32" if get.buildTYPE() == "emul32" else ""),
            "SULIN_CXX":       get.CXX() + (" -m32" if get.buildTYPE() == "emul32" else ""),
            "SULIN_CFLAGS":    filteredCFLAGS + (" -m32" if get.buildTYPE() == "emul32" else ""),
            "SULIN_LDFLAGS":   get.LDFLAGS() + (" -m32" if get.buildTYPE() == "emul32" else "")}

    for k, v in vars.items():
        inarytools.dosed("mkspecs/common/g++-base.conf", k, v)
        inarytools.dosed("mkspecs/common/g++-unix.conf", k, v)

    shelltools.export("CFLAGS", filteredCFLAGS)
    shelltools.export("CXXFLAGS", filteredCXXFLAGS)
    #check that dosed commands without releated patches
    inarytools.dosed("mkspecs/common/gcc-base-unix.conf", "\-Wl,\-rpath,")
    inarytools.dosed("mkspecs/common/gcc-base.conf", "\-O2", filteredCFLAGS)
    inarytools.dosed("mkspecs/common/gcc-base.conf", "^(QMAKE_LFLAGS\s+\+=)", r"\1 %s" % get.LDFLAGS())

    if not get.buildTYPE() == "emul32":
        #-no-pch makes build ccache-friendly
        options = "-v -confirm-license -opensource \
                            -no-rpath \
                            -no-use-gold-linker\
                            -prefix %s \
                            -bindir %s \
                            -headerdir %s \
                            -archdatadir %s\
                            -plugin-sql-{psql,mysql,sqlite,odbc} \
                            -docdir %s \
                            -plugindir %s \
                            -importdir %s \
                            -qmldir %s \
                            -datadir %s \
                            -testsdir %s \
                            -translationdir %s \
                            -sysconfdir %s \
                            -examplesdir %s \
                            -libdir %s \
                            -system-sqlite \
                            -openssl-linked \
                            -nomake tests \
                            -nomake examples \
                            -optimized-qmake \
                            -reduce-relocations \
                            -dbus-linked " % (qt.prefix, bindirQt5, qt.headerdir, qt.archdatadir, qt.docdir, qt.plugindir, qt.importdir, qt.qmldir, qt.datadir, qt.testdir, qt.translationdir, qt.sysconfdir, qt.examplesdir, qt.libdir)
    else:
        inarytools.dosed("mkspecs/linux-g++-64/qmake.conf", "-m64", "-m32")
        shelltools.export("LDFLAGS", "-m32 %s" % get.LDFLAGS())
        options = "-no-pch -v -confirm-license -opensource -no-use-gold-linker\
                   -platform linux-g++-32 \
                   -xplatform linux-g++-32 \
                   -prefix /usr/lib32 \
                   -bindir /usr/lib32/qt5/bin \
                   -docdir /usr/share/doc/qt \
                   -headerdir /usr/lib32/qt5/include/qt5 \
                   -datadir /usr/share/qt5 \
                   -sysconfdir /etc/xdg \
                   -examplesdir /usr/share/doc/qt/examples \
                   -system-sqlite \
                   -openssl-linked \
                   -nomake examples \
                   -no-xcb \
                   -no-rpath \
                   -optimized-qmake \
                   -dbus-linked \
                   -system-harfbuzz \
                   -libdir /usr/lib32/ \
                   -archdatadir /usr/lib32/qt5/"

    autotools.rawConfigure(options)

def build():
    shelltools.export("LD_LIBRARY_PATH", "%s/lib:%s" % (get.curDIR(), get.ENV("LD_LIBRARY_PATH")))
    qt.make()

def install():
    if get.buildTYPE() == "emul32":
        qt.install("INSTALL_ROOT=%s32" % get.installDIR())
        shelltools.move("%s32/usr/lib32" % get.installDIR(), "%s/usr" % get.installDIR())
        return

    inarytools.dodir(qt.libdir)
    qt.install("INSTALL_ROOT=%s" % get.installDIR())

    #I hope qtchooser will manage this issue
    for bin in shelltools.ls("%s/usr/lib/qt5/bin" % get.installDIR()):
        inarytools.dosym("/usr/lib/qt5/bin/%s" % bin, "/usr/bin/%s-qt5" % bin)

    mkspecPath = "%s/mkspecs" %  qt.archdatadir

    inarytools.dodoc("LICENSE.*")
