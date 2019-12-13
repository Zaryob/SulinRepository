#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

inarytools.cflags.add("-D_LARGEFILE64_SOURCE", "-D_FILE_OFFSET_BITS=64")

def setup():
    # fix linkage
    inarytools.dosed("pam_cap/Makefile", "(.*<\s\$\(LDLIBS\))", r"\1 -lpam")
    # no static libs
    inarytools.dosed("libcap/Makefile", "install.*STALIBNAME", deleteLine=True)
    # change shared libs mode
    inarytools.dosed("libcap/Makefile", "(.*?install -m) 0644 (.*?MINLIBNAME.*)", r"\1 0755 \2")

    inarytools.dosed("Make.Rules", "^(CC|CFLAGS|LD)\s:=.*", deleteLine=True)

    inarytools.dosed("Make.Rules", "^(PAM_CAP\s:=).*", r"\1 %s" % ("no" if get.buildTYPE() == "emul32" else "yes"))

def build():
    autotools.make("lib_prefix=/usr lib=lib%s" % ("32" if get.buildTYPE() == "emul32" else ""))

def install():
    if get.buildTYPE() == "emul32":
        autotools.rawInstall("prefix=/emul32 lib=../usr/lib32 DESTDIR=%s RAISE_SETFCAP=no" % get.installDIR())
        return

    autotools.rawInstall("prefix=/usr lib=/lib DESTDIR=%s SBINDIR=/sbin RAISE_SETFCAP=no" % (get.installDIR()))

    inarytools.insinto("/etc/security", "pam_cap/capability.conf")
    inarytools.dodoc("CHANGELOG", "License", "README", "doc/capability.notes")
