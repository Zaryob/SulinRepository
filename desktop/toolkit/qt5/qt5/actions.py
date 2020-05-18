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
                            -prefix {} \
                            -libdir {} \
                            -docdir {} \
                            -examplesdir {} \
                            -demosdir {}\
                            -plugindir {} \
                            -translationdir {} \
                            -sysconfdir {} \
                            -datadir {} \
                            -importdir {} \
                            -headerdir {} \
                            -moduledir {} \
                            -confirm-license \
                            -prefix /usr \
                            -docdir /usr/share/doc/qt5 \
                            -plugindir /usr/lib/qt5/plugins \
                            -importdir /usr/lib/qt5/imports \
                            -qmldir /usr/lib/qt5/qml \
                            -datadir /usr/share/qt5 \
                            -translationdir /usr/share/qt5/translations \
                            -sysconfdir /etc \
                            -examplesdir /usr/lib/qt5/examples \
                            -system-sqlite \
                            -system-zlib \
                            -plugin-sql-{psql,mysql,sqlite,odbc,ibase} \
                            -icu \
                            -ccache \
                            -webengine-icu \
                            -gstreamer 1.0 \
                            -system-libpng \
                            -system-ffmpeg \
                            -system-libjpeg \
                            -no-sql-mysql \
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
                                           qt.demosdir,
                                           qt.plugindir,
                                           qt.sysconfdir,
                                           qt.translationdir,
                                           qt.datadir,
                                           qt.importdir,
                                           qt.includedir,
                                           qt.moduledir))
def build():
    shelltools.cd("build")
    autotools.make()

def install():
    shelltools.cd("build")
    autotools.rawInstall("INSTALL_ROOT={}".format(get.installDIR()))
