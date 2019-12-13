#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    options = "--disable-static"

    if not get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib"

    autotools.configure(options)

    #inarytools.dosed("libtool", "^sys_lib_dlsearch_path_spec=.*", "sys_lib_dlsearch_path_spec=\"/%{_lib} %{_libdir} \"")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32": return

    inarytools.dodoc("ChangeLog", "README.md", "NEWS", "AUTHORS", "LICENSE")
