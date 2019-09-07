# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s install-sh" % get.installDIR())

    # Move data files and create symlinks for asciidoc to work
    for d in ("dblatex", "docbook-xsl", "images", "javascripts", "stylesheets"):
        inarytools.domove("/etc/asciidoc/%s" % d, "/usr/share/asciidoc")
        inarytools.dosym("/usr/share/asciidoc/%s" % d, "/etc/asciidoc/%s" % d)

    # Python module
    inarytools.insinto("/usr/lib/%s/site-packages" % get.curPYTHON(), "asciidocapi.py")

    # Vim syntax and filetype plugins
    inarytools.insinto("/usr/share/vim/vimfiles/syntax/" , "vim/syntax/asciidoc.vim")

    inarytools.dodoc("BUGS", "CHANGELOG", "COPYING", "README")
    inarytools.dodoc("docbook-xsl/asciidoc-docbook-xsl.txt", "filters/code/code-filter-readme.txt")
