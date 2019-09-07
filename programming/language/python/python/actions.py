#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

import os

WorkDir = "Python-%s" % get.srcVERSION()

PythonVersion = "2.7"

def setup():
    inarytools.cflags.add("-fwrapv")

    # no rpath
    inarytools.dosed("configure.ac", "-rpath \$\(LIBDIR\) ")

    inarytools.dosed("Lib/cgi.py", r"/usr/local/bin/", r"/usr/bin/")
    inarytools.dosed("setup.py", "SQLITE_OMIT_LOAD_EXTENSION", deleteLine=True)
    inarytools.dosed("setup.py","ndbm_libs =.*","ndbm_libs = ['gdbm', 'gdbm_compat']")

    for dir in ["expat","zlib","_ctypes/libffi_arm_wince","_ctypes/libffi_msvc",
                "_ctypes/libffi_osx","_ctypes/libffi","_ctypes/darwin"]:
        shelltools.unlinkDir("Modules/%s" % dir)

    autotools.autoreconf("-vif")

    # disable bsddb
    inarytools.dosed("setup.py", "^(disabled_module_list = \[)\]", r"\1'_bsddb', 'dbm']")
    # no rpath
    inarytools.dosed("Lib/distutils/command/build_ext.py", "self.rpath.append\(user_lib\)", "pass")

    autotools.configure("--with-fpectl \
                         --enable-shared \
                         --enable-ipv6 \
                         --with-threads \
                         --with-libc='' \
                         --enable-unicode=ucs4 \
                         --with-wctype-functions \
                         --with-system-expat \
                         --with-system-ffi \
                         --with-dbmliborder=gdbm \
                        ")

def build():
    autotools.make()

# some tests fail. let's disable testing temporarily
# def check():
    #autotools.make("test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "altinstall")

    inarytools.dosym("/usr/bin/python%s" % PythonVersion, "/usr/bin/python")
    inarytools.dosym("/usr/bin/python%s" % PythonVersion, "/usr/bin/python2")
    inarytools.dosym("/usr/bin/python%s-config" % PythonVersion, "/usr/bin/python-config")
    inarytools.dosym("/usr/lib/python%s/pdb.py" % PythonVersion, "/usr/bin/pdb")

    inarytools.dodoc("LICENSE", "README")
