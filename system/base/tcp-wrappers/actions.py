#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import libtools
from inary.actionsapi import get

WorkDir = "tcp_wrappers-7.6-ipv6.4"

def setup():
    shelltools.chmod("Makefile", 0o755)
    inarytools.dosed("Makefile", "@make", "@$(MAKE) ")
    inarytools.dosed("Makefile", "make;", "$(MAKE);")

def build():
    MINOR = "7"
    REL = "6"

    shelltools.export("SULIN_CFLAGS", "%s" % get.CFLAGS())

    args = 'REAL_DAEMON_DIR=%s \
            SULIN_OPT="-fPIC -DPIC -D_REENTRANT -DHAVE_STRERROR -DHAVE_WEAKSYMS -DINET6=1 -Dss_family=__ss_family -Dss_len=__ss_len" \
            MAJOR=0 MINOR=%s REL=%s' % ( get.sbinDIR(), MINOR, REL )

    autotools.make("%s config-check" % args)
    autotools.make('%s LDFLAGS="-pie %s" linux' % (args, get.LDFLAGS()))

def install():
    for app in ["tcpd","tcpdchk","tcpdmatch","safe_finger","try-from"]:
        inarytools.dosbin(app)

    inarytools.insinto("/usr/include", "tcpd.h")

    inarytools.dolib("libwrap.a")

    # FIXME: this seems not necessary anymore
    # inarytools.domove("libwrap.so", "libwrap.so.0.%s" % get.srcVERSION())
    inarytools.dolib("libwrap.so.0.%s" % get.srcVERSION(), "/lib")

    inarytools.dosym("/lib/libwrap.so.0.%s" % get.srcVERSION(), "/lib/libwrap.so.0")
    inarytools.dosym("/lib/libwrap.so.0", "/lib/libwrap.so")

    libtools.gen_usr_ldscript("libwrap.so")

    inarytools.dosym("hosts_access.5", "/usr/share/man/man5/hosts.allow.5")
    inarytools.dosym("hosts_access.5", "/usr/share/man/man5/hosts.deny.5")

    inarytools.doman("*.3", "*.5", "*.8")
    inarytools.dodoc("BLURB", "CHANGES", "DISCLAIMER", "README*")
