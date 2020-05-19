from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import qt
from inary.actionsapi import get

WorkDir = "qt-everywhere-src-{}".format(get.srcVERSION().replace('_','-').replace('pre1', 'tp'))
absoluteWorkDir = "{}/{}".format(get.workDIR(), WorkDir)

def setup():
    filteredCFLAGS = get.CFLAGS().replace("-g3", "-g")
    filteredCXXFLAGS = get.CXXFLAGS().replace("-g3", "-g")

    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.export("CFLAGS", filteredCFLAGS)
    shelltools.export("CXXFLAGS", filteredCXXFLAGS)
    shelltools.system('parameters=\"QMAKE_CFLAGS_ISYSTEM= \"')
    shelltools.system("OPENSSL_LIBS=\'-L/usr/lib -lssl -lcrypto\'  ../configure -confirm-license -opensource \
                            -prefix {0} \
                            -libdir {1} \
                            -docdir {2} \
                            -examplesdir {3} \
                            -plugindir {4} \
                            -translationdir {5} \
                            -sysconfdir {6} \
                            -datadir {7} \
                            -importdir {8} \
                            -headerdir {9} \
                            -confirm-license \
                            -system-sqlite \
                            -system-zlib \
                            -plugin-sql-{{psql,mysql,sqlite,odbc}} \
                            -icu \
                            -ccache \
                            -webengine-icu \
                            -gstreamer 1.0 \
                            -system-libpng \
                            -system-ffmpeg \
                            -system-libjpeg \
                            -no-rpath \
                            -openssl-linked \
                            -silent \
                            -optimized-qmake \
                            -dbus \
                            -reduce-relocations \
                            -no-separate-debug-info \
                            -opengl \
                            -glib ".format(qt.prefix,
                                           qt.libdir,
                                           qt.docdir,
                                           qt.examplesdir,
                                           qt.plugindir,
                                           qt.translationdir,
                                           qt.sysconfdir,
                                           qt.datadir,
                                           qt.importdir,
                                           qt.includedir))
def build():
    shelltools.cd("build")
    autotools.make()

def install():
    shelltools.cd("build")
    autotools.rawInstall("INSTALL_ROOT={}".format(get.installDIR()))
