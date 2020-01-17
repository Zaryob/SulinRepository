#!    inarytools.remove("/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import perlmodules
from inary.actionsapi import inarytools

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

#def check():
    #perlmodules.make("test")

def install():
    perlmodules.install()

    inarytools.dodoc("README", "Changes")

    inarytools.remove("/usr/share/man/man3/Module::Build::Authoring.3pm")
    inarytools.remove("/usr/share/man/man3/Module::Build::Platform::Windows.3pm")
    inarytools.remove("/usr/share/man/man3/Module::Build::Platform::VMS.3pm")
    inarytools.remove("/usr/share/man/man3/Module::Build::ConfigData.3pm")
    inarytools.remove("/usr/share/man/man3/Module::Build.3pm")
    inarytools.remove("/usr/share/man/man3/Module::Build::PPMMaker.3pm")
    inarytools.remove("/usr/share/man/man3/Module::Build::Compat.3pm")
    inarytools.remove("/usr/share/man/man3/Module::Build::Notes.3pm")
    inarytools.remove("/usr/share/man/man3/Module::Build::Platform::VOS.3pm")
    inarytools.remove("/usr/share/man/man3/Module::Build::Platform::Unix.3pm")
    inarytools.remove("/usr/share/man/man3/Module::Build::Platform::aix.3pm")
    inarytools.remove("/usr/share/man/man3/Module::Build::Platform::cygwin.3pm")
    inarytools.remove("/usr/share/man/man3/Module::Build::Cookbook.3pm")
    inarytools.remove("/usr/share/man/man3/Module::Build::Base.3pm")
    inarytools.remove("/usr/share/man/man3/Module::Build::Platform::Default.3pm")
    inarytools.remove("/usr/share/man/man3/Module::Build::Bundling.3pm")
    inarytools.remove("/usr/share/man/man1/config_data.1")
    inarytools.remove("/usr/share/man/man3/Module::Build::Platform::os2.3pm")
    inarytools.remove("/usr/share/man/man3/Module::Build::API.3pm")
    inarytools.remove("/usr/share/man/man3/Module::Build::Platform::MacOS.3pm")
    inarytools.remove("/usr/share/man/man3/Module::Build::Platform::darwin.3pm")
