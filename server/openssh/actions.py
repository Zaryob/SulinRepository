#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

#WorkDir = "openssh-%s" % get.srcVERSION().replace("_","")

def setup():
    shelltools.export("CFLAGS","%s -fpie" % get.CFLAGS())
    shelltools.export("LDFLAGS","%s -pie" % get.LDFLAGS())

    #inarytools.dosed("pathnames.h", "/usr/X11R6/bin/xauth", r"/usr/bin/xauth")
    #inarytools.dosed("sshd_config", "(?m)^(^#UsePAM ).*", r"UsePAM yes")
    #inarytools.dosed("sshd_config", "(?m)^(^#PasswordAuthentication ).*", r"PasswordAuthentication no")
    #inarytools.dosed("sshd_config", "(?m)^(^#X11Forwarding ).*", r"X11Forwarding yes")
    #inarytools.dosed("sshd_config", "(?m)^(^#UseDNS ).*", r"UseDNS no")
    #inarytools.dosed("sshd_config", "(?m)^(^#PermitRootLogin ).*", r"PermitRootLogin no")

    autotools.autoreconf("-fi")

    # Kerberos support is a must, libedit is optional
    # Update configure parameters when both are ready
    autotools.configure("--sysconfdir=/etc/ssh \
                         --libexecdir=/usr/libexec/openssh \
                         --datadir=/usr/share/openssh \
                         --disable-strip \
                         --with-pam \
                         --with-libedit \
                         --with-kerberos5 \
                         --with-tcp-wrappers \
                         --with-md5-passwords \
                         --with-ipaddr-display \
                         --with-privsep-user=sshd \
                         --with-privsep-path=/var/empty \
                         --without-zlib-version-check \
                         --without-ssl-engine")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # fixes #10992
    inarytools.dobin("contrib/ssh-copy-id")
    inarytools.doman("contrib/ssh-copy-id.1")
    
    # an script in contrib
    inarytools.dobin("contrib/findssl.sh")
    
    shelltools.chmod("%s/etc/ssh/sshd_config" % get.installDIR(), 0o600)
    # special request by merensan
    shelltools.echo("%s/etc/ssh/ssh_config" % get.installDIR(), "ServerAliveInterval 5")

    inarytools.dodir("/var/empty/sshd")

    inarytools.dodoc("ChangeLog", "CREDITS", "OVERVIEW", "README*", "TODO", "sshd_config")
