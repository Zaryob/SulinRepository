#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
import os


movetobin = ["arch", "basename", "cat", "chgrp", "chmod", "chown", "cp", "cut", "date", "dd", "df",
             "dir", "echo", "env", "false", "link", "ln", "ls", "mkdir", "mknod", "mktemp", "mv",
             "nice", "pwd", "readlink", "rm", "rmdir", "sleep", "sort", "stty", "sync", "touch",
             "true", "uname", "unlink", "vdir","coreutils"]

symtousrbin = ["env", "cut", "readlink","coreutils"]

def setup():
    inarytools.cflags.add("-fno-strict-aliasing -fPIC -D_GNU_SOURCE=1")
    #shelltools.export("gl_cv_func_printf_directive_n", "yes")
    #shelltools.export("gl_cv_func_isnanl_works", "yes")
    shelltools.export("DEFAULT_POSIX2_VERSION", "200112")
    shelltools.export("AUTOPOINT", "true")
    shelltools.export("FORCE_UNSAFE_CONFIGURE","1")
    shelltools.export("AT_M4DIR", "m4")
    autotools.autoreconf("-vfi")

    # Fedora also installs su and hostname
    autotools.configure("""--with-packager="Sulin" \
                         --with-packager-version="coreutils-8.32" \
                         --without-selinux \
                         --with-packager-bug-reports="https://gitlab.com/sulinos/main/issues" \
                         --enable-largefile \
                         --enable-single-binary=symlinks \
                         --enable-install-program=arch \
                         --with-openssl \
                         --libexecdir=/usr/lib""")

def build():
    autotools.make("CFLAGS='-Ofast -O3 -s'")


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    for prog in [ "faillog", "hostname", "login", "lastlog", "uptime" ]:
        if os.path.isfile("{}/usr/bin/{}".format(get.installDIR(),prog)):
            os.unlink("{}/usr/bin/{}".format(get.installDIR(),prog))
    autotools.make("mandir=%s/%s install-man" % (get.installDIR(), get.manDIR()))
    #~ autotools.install("mandir=%s/%s" % (get.installDIR(), get.manDIR()))

    # Use dircolors from the package
    inarytools.insinto("/etc", "src/dircolors.hin", "DIR_COLORS")

    # move critical files into /bin
    for f in movetobin:
        inarytools.domove("/usr/bin/%s" % f, "/bin/")

    for f in symtousrbin:
        inarytools.dosym("../../bin/%s" % f, "/usr/bin/%s" % f)
    

    inarytools.dodoc("AUTHORS", "ChangeLog*", "NEWS", "README*", "THANKS", "TODO")
