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

NoStrip = ["/lib", "/boot"]

shelltools.export("KBUILD_BUILD_USER", "sulin")
shelltools.export("KBUILD_BUILD_HOST", "uludag")
shelltools.export("PYTHONDONTWRITEBYTECODE", "1")

def setup():
    kerneltools.configure()

def build():
    kerneltools.build(debugSymbols=False)


def install():
    kerneltools.install()

    # add objtool for external module building and enabled VALIDATION_STACK option
    inarytools.insinto("/usr/src/linux-headers-%s/tools/objtool" % get.srcVERSION(), "%s/tools/objtool/objtool" % get.curDIR())

    # Install kernel headers needed for out-of-tree module compilation
    kerneltools.installHeaders()

    kerneltools.installLibcHeaders()

    # Generate some module lists to use within mkinitramfs
    shelltools.system("./generate-module-list %s/lib/modules/%s" % (get.installDIR(), kerneltools.__getSuffix()))

    #mkinitcpio default config
    inarytools.dodir("/etc/mkinitcpio.d")
    shelltools.touch("linux.preset")

    shelltools.echo("linux.preset", "# mkinitcpio preset file for the 'linux' package\n" +

                    'ALL_config="/etc/mkinitcpio.conf"\n'+

                    'ALL_kver="/boot/kernel-%s"\n\n'% get.srcVERSION() +
                    "PRESETS=('default' 'fallback') \n\n" +
                    '#default_config="/etc/mkinitcpio.conf"\n' +
                    'default_image="/boot/initramfs-%s.img"\n'% get.srcVERSION() +

                    '#default_options=""\n\n' +
                    '#fallback_config="/etc/mkinitcpio.conf"\n'+
                    'fallback_image="/boot/initramfs-%s-fallback.img"\n'% get.srcVERSION() +
                    'fallback_options="-S autodetect"\n')

    inarytools.insinto("/etc/mkinitcpio.d", "linux.preset")
