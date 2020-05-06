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
    #empity dir for buggy kerneltools
    inarytools.dodir("/lib/modules/5.6.4-sulinos/source")
    inarytools.dodir("/lib/modules/5.6.4-sulinos/build")
    kerneltools.install()
    inarytools.removeDir("/lib/modules/5.6.4-sulinos/source")
    inarytools.removeDir("/lib/modules/5.6.4-sulinos/build")
    inarytools.removeDir("/usr/bin")
    kerneltools.installHeaders()
    kerneltools.installLibcHeaders()
    #fix libre kernel suffix bug
    shelltools.system("mv {0}/boot/linux-5.6.4 {0}/boot/linux-5.6.4-libre-sulinos".format(get.installDIR()))
    shelltools.system("mv {0}/usr/src/libre-headers-5.6.4-sulinos {0}/usr/src/linux-headers-5.6.4-libre-sulinos".format(get.installDIR()))
    shelltools.system("mv {0}/lib/modules/5.6.4-sulinos {0}/lib/modules/5.6.4-libre-sulinos".format(get.installDIR()))
    # add objtool for external module building and enabled VALIDATION_STACK option
    inarytools.insinto("/usr/src/linux-headers-%s-libre-sulinos/tools/objtool" % get.srcVERSION(), "%s/tools/objtool/objtool" % get.curDIR())

    # Generate some module lists to use within mkinitramfs
    shelltools.system("./generate-module-list %s/lib/modules/%s-libre-sulinos" % (get.installDIR(), kerneltools.__getSuffix()))
    #kernel include dirs from linux
    shelltools.system("rm -rf  {0}/usr/include".format(get.installDIR()))

