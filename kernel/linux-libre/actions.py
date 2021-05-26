#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import kerneltools
from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get
import time


NoStrip = ["/lib", "/boot"]

shelltools.export("KBUILD_BUILD_USER", "sulin")
shelltools.export("KBUILD_BUILD_HOST", "uludag")
shelltools.export("PYTHONDONTWRITEBYTECODE", "1")
shelltools.export("KBUILD_BUILD_TIMESTAMP", time.asctime())

def setup():
    kerneltools.configure()

def build():
    kerneltools.build(debugSymbols=False)


def install():
    shelltools.cd("../linux-5.12.6")
    kerneltools.install(distro="libre-sulinos")
    kerneltools.installModuleHeaders(distro="libre-sulinos")
    # add objtool for external module building and enabled VALIDATION_STACK option
    inarytools.insinto("/usr/src/linux-headers-%s-libre-sulinos/tools/objtool" % get.srcVERSION(), "%s/tools/objtool/objtool" % get.curDIR())

    # Generate some module lists to use within mkinitramfs
    shelltools.system("./generate-module-list %s/lib/modules/%s-libre-sulinos" % (get.installDIR(), kerneltools.__getSuffix()))
