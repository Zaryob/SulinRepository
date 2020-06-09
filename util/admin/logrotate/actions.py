#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get
def setup():
    autotools.configure("--with-compress-command=/usr/bin/gzip \
                		 --with-uncompress-command=/usr/bin/gunzip \
                		 --with-default-mail-command=/usr/bin/mail \
                		 --with-acl")
def build():
    autotools.make("RPM_OPT_FLAGS=\"%s\" WITH_ACL=yes" % get.CFLAGS())

def install():
    autotools.rawInstall("PREFIX=%s MANDIR=%s" % (get.installDIR(), get.manDIR()))

    inarytools.dodir("/etc/logrotate.d")

    inarytools.dobin("examples/logrotate.cron", "/etc/cron.daily")
