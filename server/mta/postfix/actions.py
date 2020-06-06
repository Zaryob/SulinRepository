#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    inarytools.dosed("src/util/sys_defs.h", "hash:\/etc\/aliases", "hash:/etc/mail/aliases")

def build():
    cc_args = "-DHAS_PCRE -DHAS_MYSQL -I/usr/include/mysql -DHAS_PGSQL -I/usr/include/postgresql \
               -DUSE_TLS -DUSE_SASL_AUTH -DUSE_CYRUS_SASL -I/usr/include/sasl -DHAS_LDAP -fPIC"
    cc_libs = "-pie -Wl,-z,relro -Wl,-z,now -L/usr/lib -lpcre -lcrypt -lpthread -lpam -lssl -lcrypto -lsasl2 -lmysqlclient -lpq -lm -lz -lldap -llber"

    # Default paths
    inarytools.dosed("src/global/mail_params.h", \
                    "#define DEF_README_DIR\s+\"no\"", \
                    "#define DEF_README_DIR \"/usr/share/doc/%s/readme\"" % get.srcNAME())

    inarytools.dosed("src/global/mail_params.h", \
                    "#define DEF_HTML_DIR\s+\"no\"", \
                    "#define DEF_HTML_DIR \"/usr/share/doc/%s/html\"" % get.srcNAME())

    inarytools.dosed("src/global/mail_params.h", \
                    "#define DEF_MANPAGE_DIR\s+\"/usr/local/man\"", \
                    "#define DEF_MANPAGE_DIR \"/usr/share/man\"")

    inarytools.dosed("src/util/sys_defs.h", \
                    "#define NATIVE_DAEMON_DIR \"/usr/libexec/postfix\"", \
                    "#define NATIVE_DAEMON_DIR \"/usr/lib/postfix\"")

    autotools.make('CC=%s \
                    OPT="%s" \
                    CCARGS="%s" \
                    AUXLIBS="%s" makefiles' % (get.CC(), get.CFLAGS(), cc_args, cc_libs))

    autotools.make()

def install():
    shelltools.system('/bin/sh postfix-install \
                       -non-interactive \
                       install_root="%(installDIR)s" \
                       config_directory="/usr/share/doc/%(srcNAME)s/defaults" \
                       readme_directory="/usr/share/doc/%(srcNAME)s/readme" \
                       ' % {'installDIR': get.installDIR(), 'srcNAME': get.srcNAME()})

    inarytools.removeDir("/var/")

    # lets make dirs
    inarytools.dodir("/var/spool/postfix/")
    inarytools.dodir("/etc/mail/")
    inarytools.dodir("/etc/postfix/")
    inarytools.dodir("/var/spool/mail/")
    inarytools.dodir("/var/lib/postfix")
    inarytools.dosym("/var/spool/mail", "/var/mail")

    # qshape comes
    inarytools.dosbin("auxiliary/qshape/qshape.pl")
    inarytools.rename("/usr/sbin/qshape.pl", "qshape")

    # legacy FSH
    inarytools.dosym("/usr/sbin/sendmail", "/usr/lib/sendmail")

    # performance tuning tools.
    inarytools.dosbin("bin/smtp-source")
    inarytools.dosbin("bin/smtp-sink")
    inarytools.dosbin("bin/qmqp-source")
    inarytools.dosbin("bin/qmqp-sink")
    inarytools.doman("man/man1/smtp-source.1")
    inarytools.doman("man/man1/smtp-sink.1")
    inarytools.doman("man/man1/qmqp-source.1")
    inarytools.doman("man/man1/qmqp-sink.1")

    # Move some files
    inarytools.domove("/usr/share/doc/%s/defaults/master.cf" % get.srcNAME(), "/etc/postfix/")

    # Docs
    inarytools.insinto("/usr/share/doc/%s/" % get.srcNAME(), "html/")
    inarytools.insinto("/usr/share/doc/%s/" % get.srcNAME(), "examples/")
    for s in ["*README", "COMPATIBILITY", "HISTORY", "LICENSE", "RELEASE_NOTES"]:
        inarytools.insinto("/usr/share/doc/%s/" % get.srcNAME(), s)
