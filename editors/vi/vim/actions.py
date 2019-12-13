#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get


#WorkDir = "vim74"

def setup():
    # TODO: do we need that ?
    shelltools.export("CXXFLAGS", get.CXXFLAGS().replace("-D_FORTIFY_SOURCE=2", ""))
    shelltools.export("CFLAGS", get.CFLAGS().replace("-D_FORTIFY_SOURCE=2", ""))
    inarytools.dosed("runtime/tools/mve.awk", "#!/usr/bin/nawk -f", "#!/usr/bin/awk -f")

    # define the place for the global (g)vimrc file (set to /etc/vim/vimrc)
    shelltools.echo("src/feature.h", "#define SYS_VIMRC_FILE \"/etc/vim/vimrc\"")

    # our binary ctags file is names as exuberant-ctags
    inarytools.dosed("runtime/doc/syntax.txt", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")
    inarytools.dosed("runtime/doc/tagsrch.txt", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")
    inarytools.dosed("runtime/doc/usr_29.txt", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")
    inarytools.dosed("runtime/menu.vim", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")
#    inarytools.dosed("src/configure.in", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")

    # TODO: do we need that ?
#    inarytools.dosed("src/configure.in", r"libc\.h", "")

    # TODO: we could need that
    #autotools.make("-C src autoconf")

    # TODO: * We should use "big" feature instead of "huge".
    #       * Investigate impacts on current use
    options ="--with-features=huge \
              --enable-multibyte \
              --enable-perlinterp \
              --enable-pythoninterp \
              --enable-python3interp \
              --with-python3-config-dir=/usr/lib/python3.7/config-3.7m-x86_64-linux-gnu/ \
              --enable-rubyinterp \
              --enable-gui=no \
              --with-tlib=ncurses \
              --prefix=/usr \
              --localstatedir=/var/lib/vim \
              --with-features=big \
              --disable-acl \
              --with-compiledby=Sulin \
              --enable-gpm \
              --enable-acl \
              --enable-cscope \
              --disable-netbeans \
              --disable-luainterp \
              --with-x=no \
              --with-modified-by=Sulin"

    if get.buildTYPE() == "gui":
        options += " --enable-gui=gtk2 \
                     --with-vim-name=gvim \
                     --with-view-name=gview \
                     --with-x=yes"

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("VIMRCLOC=/etc/vim DESTDIR=%s" % get.installDIR())

    # enough for gui building, quit here
    if get.buildTYPE() == "gui":
        return

    # Vi != Vim, it's hard to break habbits
    inarytools.dosym("vim", "/usr/bin/vi")
    inarytools.dosym("/usr/bin/vim", "/bin/ex")
