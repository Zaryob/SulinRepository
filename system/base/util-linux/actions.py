#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

inarytools.cflags.add("-D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64")
inarytools.cflags.sub("-O[\d]", "-Os")

def setup():
    shelltools.export("SUID_CFLAGS", "-fpie")
    shelltools.export("SUID_LDFLAGS", "-pie -Wl,-z,relro -Wl,-z,now")
    shelltools.export("AUTOPOINT", "/bin/true")

    options = "\
               --disable-rpath \
               --disable-silent-rules \
               --disable-use-tty-group \
               --disable-su  \
               --disable-last \
               --disable-mesg \
               --disable-vipw \
               --disable-wall \
               --disable-login \
               --disable-newgrp \
               --disable-nologin \
               --disable-runuser \
               --disable-sulogin \
               --disable-utmpdump \
               --disable-chfn-chsh \
               --disable-mountpoint \
               --disable-makeinstall-chown \
               --disable-socket-activation \
              "

    if get.buildTYPE() == "emul32":
        options += "\
                     --prefix=/emul32 \
                     --bindir=/emul32/bin \
                     --sbindir=/emul32/sbin \
                     --libdir=/usr/lib32 \
                     --without-ncurses \
                     --disable-static \
                     --enable-libmount \
                     --with-audit=no \
                     --without-python \
                   "
    else:
        options += "\
                     --bindir=/bin \
                     --sbindir=/sbin \
                     --enable-partx \
                     --enable-raw \
                     --enable-write \
                     --enable-tunelp \
                     --enable-runuser \
                     --without-audit \
                     --with-udev \
                     --without-utempter \
                     --with-python=3 \
                   "

    autotools.autoreconf("-fi")
    autotools.configure(options)
    inarytools.dosed("libtool", "( -shared )", r" -Wl,--as-needed\1")

    # Extra fedora switches:
    # --enable-login-utils will enable some utilities we ship in shadow
    # --enable-kill will enable the kill utility we ship in coreutils

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #inarytools.doman("sys-utils/klogconsole.man")
    inarytools.remove("/usr/share/man/man1/kill.1")
    inarytools.remove("/usr/share/bash-completion/completions/rfkill")

    if get.buildTYPE() == "emul32": return

    #inarytools.removeDir("/usr/lib32/pkgconfig")

    inarytools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING", "README*")
    inarytools.insinto("/%s/%s" % (get.docDIR(), get.srcNAME()), "Documentation")
