#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools


movetobin = ["arch", "basename", "cat", "chgrp", "chmod", "chown", "cp", "cut", "date", "dd", "df",
             "dir", "echo", "env", "false", "link", "ln", "ls", "mkdir", "mknod", "mktemp", "mv",
             "nice", "pwd", "readlink", "rm", "rmdir", "sleep", "sort", "stty", "sync", "touch",
             "true", "uname", "unlink", "vdir"]

symtousrbin = ["env", "cut", "readlink"]

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
    autotools.configure("""--with-packager="Gentoo" \
    		             --with-packager-version="coreutils-8.28-r1" \
    		             --with-packager-bug-reports="https://gitlab.com/sulinos/main/issues" \
                         --enable-largefile \
                         --enable-install-program=arch \
                         --enable-no-install-program=faillog,hostname,login,lastlog,uptime \
                         --libexecdir=/usr/lib""")

def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
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
