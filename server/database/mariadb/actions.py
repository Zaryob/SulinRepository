#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import cmaketools


#inarytools.flags.add("-fno-strict-aliasing -DBIG_JOINS=1")
#inarytools.cflags.add("-fomit-frame-pointer")
#inarytools.cxxflags.add("-felide-constructors -fno-rtti -fno-delete-null-pointer-checks")

def setup():
    #inarytools.dosed("storage/tokudb/ft-index/ft/ft-ops.cc", "LEAFENTRY leaf_entry;", "LEAFENTRY leaf_entry = 0;")
    shelltools.export("CFLAGS", get.CFLAGS())
    shelltools.export("CXXFLAGS", get.CXXFLAGS())
    cmaketools.configure("  -DCOMPILATION_COMMENT=\"Sulin\" \
                            -DBUILD_CONFIG=mysql_release \
                            -DCMAKE_INSTALL_PREFIX=/usr \
                            -DSYSCONFDIR=/etc \
                            -DSYSCONF2DIR=/etc/my.cnf.d \
                            -DMYSQL_DATADIR=/var/lib/mysql \
                            -DMYSQL_UNIX_ADDR=/run/mysqld/mysqld.sock \
                            -DDEFAULT_CHARSET=utf8mb4 \
                            -DDEFAULT_COLLATION=utf8mb4_general_ci \
                            -DENABLED_LOCAL_INFILE=ON \
                            -DINSTALL_INFODIR=share/info \
                            -DINSTALL_MANDIR=share/man \
                            -DINSTALL_PLUGINDIR=lib/$pkgname/plugin \
                            -DINSTALL_SCRIPTDIR=bin \
                            -DINSTALL_INCLUDEDIR=include/mysql \
                            -DINSTALL_DOCREADMEDIR=share/doc/$pkgname \
                            -DINSTALL_SUPPORTFILESDIR=share/$pkgname \
                            -DINSTALL_MYSQLSHAREDIR=share/$pkgname \
                            -DINSTALL_DOCDIR=share/doc/$pkgname \
                            -DTMPDIR=/var/tmp \
                            -DCONNECT_WITH_MYSQL=ON \
                            -DCONNECT_WITH_LIBXML2=system \
                            -DCONNECT_WITH_ODBC=NO \
                            -DCONNECT_WITH_JDBC=NO \
                            -DPLUGIN_ARCHIVE=YES \
                            -DPLUGIN_ARIA=YES \
                            -DPLUGIN_BLACKHOLE=YES \
                            -DPLUGIN_CASSANDRA=NO \
                            -DPLUGIN_CSV=YES \
                            -DPLUGIN_MYISAM=YES \
                            -DPLUGIN_MROONGA=NO \
                            -DPLUGIN_OQGRAPH=NO \
                            -DPLUGIN_PARTITION=YES \
                            -DPLUGIN_SPHINX=NO \
                            -DPLUGIN_TOKUDB=NO \
                            -DPLUGIN_AUTH_GSSAPI=NO \
                            -DPLUGIN_AUTH_GSSAPI_CLIENT=OFF \
                            -DPLUGIN_CRACKLIB_PASSWORD_CHECK=NO \
                            -DWITH_ASAN=OFF \
                            -DWITH_EMBEDDED_SERVER=ON \
                            -DWITH_EXTRA_CHARSETS=complex \
                            -DWITH_INNODB_BZIP2=OFF \
                            -DWITH_INNODB_LZ4=OFF \
                            -DWITH_INNODB_LZMA=ON \
                            -DWITH_INNODB_LZO=OFF \
                            -DWITH_INNODB_SNAPPY=OFF \
                            -DWITH_ROCKSDB_BZIP2=OFF \
                            -DWITH_ROCKSDB_JEMALLOC=OFF \
                            -DWITH_ROCKSDB_LZ4=OFF \
                            -DWITH_ROCKSDB_ZSTD=OFF \
                            -DWITH_ROCKSDB_SNAPPY=OFF \
                            -DWITH_JEMALLOC=NO \
                            -DWITH_LIBARCHIVE=system \
                            -DWITH_LIBNUMA=NO \
                            -DWITH_LIBWRAP=OFF \
                            -DWITH_LIBWSEP=OFF \
                            -DWITH_MARIABACKUP=ON \
                            -DWITH_PCRE=system \
                            -DWITH_READLINE=ON \
                            -DWITH_SYSTEMD=no \
                            -DWITH_SSL=system \
                            -DWITH_VALGRIND=OFF \
                            -DWITH_ZLIB=system \
                            -DSKIP_TESTS=ON")
#-DCMAKE_EXE_LINKER_FLAGS='-ljemalloc' \
def build():
    cmaketools.make()

def install():
    cmaketools.install("DESTDIR=%s benchdir_root=\"/usr/share/mysql\"" % get.installDIR())

    # Config
    inarytools.insinto("/etc/mysql", "%s/usr/share/mysql/my-medium.cnf" % get.installDIR(), "my.cnf")
    inarytools.insinto("/etc/mysql", "%s/%s/scripts/mysqlaccess.conf" % (get.workDIR(), get.srcDIR()))
    inarytools.insinto("/usr/bin", "%s/%s/scripts/mysql_config" % (get.workDIR(), get.srcDIR()))
    # Data dir
    inarytools.dodir("/var/lib/mysql")

    # Documents
    inarytools.dodoc("%s/%s/support-files/my-*.cnf" % (get.workDIR(), get.srcDIR()))
    inarytools.dodoc("COPYING", "INSTALL-SOURCE", "README", "VERSION")

    # Remove not needed files
    inarytools.removeDir("/usr/data")
    inarytools.removeDir("/usr/mysql-test")
    inarytools.removeDir("/usr/sql-bench")
    inarytools.remove("/usr/share/man/man1/mysql-test-run.pl.1")

    # Remove -lprobes_mysql
    #inarytools.dosed("%s/usr/bin/mysql_config" % get.installDIR(), "-lprobes_mysql")
