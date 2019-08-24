#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    #inarytools.cflags.add('-fpie -DSYSLOGD_PIDNAME=\\"syslogd.pid\\"')
    inarytools.ldflags.add("-pie -Wl,-z,relro -Wl,-z,now")

    autotools.configure("\
                         --sbindir=/usr/bin \
                         --disable-gui \
                         --disable-mysql \
                         --disable-pgsql \
                         --disable-relp \
                         --disable-gnutls \
                         --disable-static \
                         --disable-rfc3195 \
                         --disable-omjournal \
                         --disable-testbench \
                         --disable-mmnormalize \
                         --disable-gssapi-krb5 \
                         --disable-generate-man-pages \
                         --disable-uuid \
                         --enable-mail \
                         --enable-zlib \
                         --enable-imdiag \
                         --enable-imfile \
                         --enable-imptcp \
                         --enable-mmanon \
                         --enable-omprog \
                         --enable-mmaudit \
                         --enable-pmsnare \
                         --enable-impstats \
                         --enable-omstdout \
                         --enable-omuxsock \
                         --enable-largefile \
                         --enable-pmlastmsg \
                         --enable-mmjsonparse \
                         --enable-pmrfc3164sd \
                         --enable-pmcisconames \
                         --enable-sm_cust_bindcdr \
                         --enable-unlimited-select \
                         --enable-pmaixforwardedfrom \
                         --enable-cached-man-pages \
                         --with-systemdsystemunitdir=no \
                        ")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("COPYING*", "README", "AUTHORS", "ChangeLog")
    
    # create needed directory
    inarytools.dodir("/var/spool/rsyslog")
    inarytools.dodir("/var/empty/dev")
