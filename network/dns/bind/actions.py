#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from inary.actionsapi import autotools
from inary.actionsapi import libtools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get


BINDDIR="/var/named"
CHROOT="%s/chroot" % BINDDIR

shelltools.export("CPPFLAGS", "%s -DDIG_SIGCHASE" % get.CXXFLAGS())

def setup():
    shelltools.makedirs("m4")

    libtools.libtoolize("-cf")
    autotools.aclocal("-I m4")
    autotools.autoreconf("-vfi")

    autotools.configure("PYTHON=/usr/bin/python3 \
                        --localstatedir=/var \
                         --sysconfdir=/etc/bind \
                         --with-openssl \
                         --with-libtool \
                         --with-python \
                         --with-pic \
                         --with-lmdb \
                         --with-randomdev=/dev/urandom \
                         --enable-linux-caps \
                         --enable-threads \
                         --includedir=/usr/include/bind9 \
                         --enable-ipv6 \
                         --enable-largefile \
                         --enable-geoip \
                         --disable-static")
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Prepare chroot jail
    for d in ("dev", "etc/bind", "etc/pki/dnssec-keys", "lib/bind", "var/tmp", "var/log", "var/run/named", "var/named"):
        inarytools.dodir("%s/%s" % (CHROOT, d))

    # At least drop a file in it
    shelltools.echo("%s%s/README" % (get.installDIR(), CHROOT), "Chroot jail for named")

    # Create directories
    inarytools.dodir("/var/run/named")
    for d in ("pri", "sec", "slaves", "data", "dynamic"):
        inarytools.dodir("%s/%s" % (BINDDIR, d))

    # Create symlinks
    for src, dest in [("named.ca", "%s/root.cache" % BINDDIR),
                      ("%s/pri" % BINDDIR, "/etc/bind/pri"),
                      ("%s/sec" % BINDDIR, "/etc/bind/sec")]:
        inarytools.dosym(src, dest)

    # Documentation
    inarytools.dodoc("CHANGES", "COPYRIGHT", "README")
    inarytools.dodoc("doc/misc/*", "contrib/scripts/named-bootconf.sh", "contrib/scripts/nanny.pl")
    inarytools.dohtml("doc/arm/*")
    inarytools.remove("/usr/share/doc/%s/Makefile*" % get.srcNAME())
