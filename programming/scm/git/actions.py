# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import perlmodules
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

config = """
V                       = 1
CFLAGS                  = %s
LDFLAGS                 = %s
INSTALLDIRS             = vendor
DESTDIR                 = %s
prefix                  = /usr
htmldir                 = /usr/share/doc/git
sysconfdir              = /etc
ETC_GITCONFIG           = /etc/gitconfig
GITWEB_CSS              = gitweb/gitweb.css
GITWEB_LOGO             = gitweb/git-logo.png
GITWEB_FAVICON          = gitweb/git-favicon.png
GITWEB_JS               = gitweb/gitweb.js
PYTHON_PATH             = /usr/bin/python3
PERL_MM_OPT             =""
GIT_TEST_OPTS           ='--no-color'
gitwebdir               = /var/www/localhost/cgi-bin
ASCIIDOC8               = 1
ASCIIDOC_NO_ROFF        = 1
BLK_SHA1                = 1
NEEDS_CRYPTO_WITH_SSL   = 1
USE_LIBPCRE             = 1
NO_CROSS_DIRECTORY_HARDLINKS = 1
MAN_BOLD_LITERAL        = 1
V                       = 1
""" % (get.CFLAGS(), get.LDFLAGS(), get.installDIR())


shelltools.export("XML_CATALOG_FILES","/etc/xml/catalog")

def setup():
    shelltools.echo("config.mak", config)

def build():
    inarytools.dosed("Makefile", "^CC = .*$", "CC = %s" % get.CC())
    autotools.make("all")

def install():
    autotools.rawInstall("DESTDIR={} install-html all".format(get.installDIR()))

    # Install bash completion
    inarytools.insinto("/etc/bash_completion.d", "contrib/completion/git-completion.bash", "git")
    shelltools.chmod("%s/etc/bash_completion.d/git" % get.installDIR(), 0o644)

    # for git-daemon
    inarytools.dodir("/pub/scm")

    # emacs support
    # autotools.install("-C contrib")
    inarytools.insinto("/usr/share/doc/emacs-git", "contrib/emacs/README")
    inarytools.insinto("/usr/share/git/", "contrib/*")

    # Some docs
    inarytools.dodoc("README.md", "COPYING", "Documentation/SubmittingPatches")

    # remove .pod and .packlist files
    perlmodules.removePodfiles()
    perlmodules.removePacklist()
