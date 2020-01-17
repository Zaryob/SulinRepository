#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    #inarytools.flags.add("-fstack-protector-all", "-DLDAP_DEPRECATED=1")
    inarytools.dosed("config-scripts/cups-sharedlibs.m4", "( -shared )", " -Wl,--as-needed\\1")

    # For --enable-avahi
    autotools.aclocal("-I config-scripts")
    autotools.autoconf("-I config-scripts")

    options = '--with-cups-user=daemon \
               --with-cups-group=lp \
               --with-system-groups=lpadmin \
               --with-docdir=/usr/share/cups/html \
               --with-dbusdir=/etc/dbus-1 \
               --with-optim="%s" \
               --with-php=/usr/bin/php-cgi \
               --with-cupsd-file-perm=0755 \
               --with-log-file-perm=0600 \
               --without-java \
               --enable-acl \
               --enable-ssl=yes \
               --enable-libpaper \
               --enable-libusb=yes \
               --enable-debug \
               --enable-gssapi \
               --enable-dbus \
               --enable-pam=yes \
               --enable-relro \
               --enable-dnssd \
               --enable-browsing \
               --enable-threads \
               --enable-raw-printing \
               --enable-avahi \
               --disable-gnutls \
               --disable-launchd \
               --without-rcdir \
               --libdir=/usr/lib \
               --without-perl \
               --with-logdir=/var/log/cups \
               KRB5CONFIG=/usr/bin/krb5-config \
               --localstatedir=/var \
               --with-rundir=/run/cups \
               --with-xinetd=/etc/xinetd.d \
              ' % get.CFLAGS()

    if get.buildTYPE() == "emul32":
        options += '  \
                     --enable-libusb=no \
                     --disable-avahi \
                     --disable-dnssd \
                     --disable-gssapi \
                     --disable-dbus \
                     --bindir=/usr/bin32 \
                     --sbindir=/usr/sbin32 \
                     --libdir=/usr/lib32'

    autotools.configure(options)

def build():
    autotools.make()

#def check():
    #autotools.make("check")

def install():
    if get.buildTYPE() == "emul32":
        # SERVERBIN is hardcoded to /usr/lib/cups, thus it overwrites 64 bit libraries
        autotools.rawInstall("BUILDROOT=%s SERVERBIN=%s/usr/serverbin32 install-libs" % (get.installDIR(), get.installDIR()))
        inarytools.domove("/usr/bin32/cups-config", "/usr/bin", "cups-config-32bit")
        inarytools.removeDir("/usr/bin32")
        inarytools.removeDir("/usr/sbin32")
        inarytools.removeDir("/usr/serverbin32")

        # remove files now part of cups-filters
        #inarytools.remove("/usr/share/cups/data/testprint")
        inarytools.removeDir("/usr/share/cups/banners")
        inarytools.dodir("/usr/share/cups/banners")
        return

    autotools.rawInstall("BUILDROOT=%s install-headers install-libs install-data install-exec" % get.installDIR())
    shelltools.chmod("%s/run/cups/certs" % get.installDIR(), 0o755)

    inarytools.dodir("/usr/share/cups/profiles")

    # Serial backend needs to run as root
    #shelltools.chmod("%s/usr/lib/cups/backend/serial" % get.installDIR(), 0700)

