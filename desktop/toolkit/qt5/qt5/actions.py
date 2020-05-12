from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import qt
from inary.actionsapi import get

WorkDir = "qt-everywhere-src-%s" % get.srcVERSION().replace('_','-').replace('pre1', 'tp')
absoluteWorkDir = "%s/%s" % (get.workDIR(), WorkDir)

def setup():
    filteredCFLAGS = get.CFLAGS().replace("-g3", "-g")
    filteredCXXFLAGS = get.CXXFLAGS().replace("-g3", "-g")

    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.export("CFLAGS", filteredCFLAGS)
    shelltools.export("CXXFLAGS", filteredCXXFLAGS)
    shelltools.system('parameters=\"QMAKE_CFLAGS_ISYSTEM= \"')
    shelltools.system("OPENSSL_LIBS=\'-L/usr/lib -lssl -lcrypto\'  ../configure -confirm-license -opensource \
                            -prefix /usr \
                            -docdir /usr/share/doc/qt5 \
                            -plugindir /usr/lib/qt5/plugins \
                            -importdir /usr/lib/qt5/imports \
                            -qmldir /usr/lib/qt5/qmldir \
                            -datadir /usr/share/qt5 \
                            -translationdir /usr/share/qt5/translations \
                            -sysconfdir /etc \
                            -examplesdir /usr/lib/qt5/examples \
                            -system-sqlite \
                            -system-zlib \
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
                            -glib ")
def build():
    shelltools.cd("build")
    autotools.make()

def install():
    shelltools.cd("build")
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
