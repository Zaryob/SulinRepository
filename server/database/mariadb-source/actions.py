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
    cmaketools.configure("-DBUILD_CONFIG=mysql_release \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DSYSCONFDIR=/etc/mysql \
                          -DMYSQL_DATADIR=/var/lib/mysql \
                          -DMYSQL_UNIX_ADDR=/run/mysqld/mysqld.sock \
                          -DDEFAULT_CHARSET=utf8 \
                          -DDEFAULT_COLLATION=utf8_general_ci \
                          -DENABLED_LOCAL_INFILE=ON \
                          -DINSTALL_INFODIR=share/mysql/docs \
                          -DINSTALL_MANDIR=share/man \
                          -DINSTALL_PLUGINDIR=lib/mysql/plugin \
                          -DINSTALL_SCRIPTDIR=bin \
                          -DINSTALL_INCLUDEDIR=include/mysql \
                          -DINSTALL_DOCREADMEDIR=share/mysql \
                          -DINSTALL_SUPPORTFILESDIR=share/mysql \
                          -DINSTALL_MYSQLSHAREDIR=share/mysql \
                          -DINSTALL_DOCDIR=share/mysql/docs \
                          -DINSTALL_SHAREDIR=share/mysql \
                          -DWITH_READLINE=ON \
                          -DWITH_ZLIB=system \
                          -DWITH_SSL=system \
                          -DWITH_PCRE=bundled \
                          -DWITH_LIBWRAP=OFF \
                          -DWITH_JEMALLOC=ON \
                          -DWITH_EXTRA_CHARSETS=complex \
                          -DWITH_EMBEDDED_SERVER=ON \
                          -DWITH_ARCHIVE_STORAGE_ENGINE=1 \
                          -DWITH_BLACKHOLE_STORAGE_ENGINE=1 \
                          -DWITH_INNOBASE_STORAGE_ENGINE=1 \
                          -DWITH_PARTITION_STORAGE_ENGINE=1 \
                          -DWITHOUT_TOKUDB_STORAGE_ENGINE=1 \
                          -DWITHOUT_EXAMPLE_STORAGE_ENGINE=1 \
                          -DWITHOUT_FEDERATED_STORAGE_ENGINE=1 \
                          -DWITHOUT_PBXT_STORAGE_ENGINE=1 \
                          -DCMAKE_C_FLAGS='-fPIC %s -fno-strict-aliasing -DBIG_JOINS=1 -fomit-frame-pointer -fno-delete-null-pointer-checks' \
                          -DCMAKE_CXX_FLAGS='-fPIC %s -fno-strict-aliasing -DBIG_JOINS=1 -felide-constructors -fno-rtti -fno-delete-null-pointer-checks' \
                          -DWITH_MYSQLD_LDFLAGS='-pie %s,-z,now'" % (get.CFLAGS(), get.CXXFLAGS(), get.LDFLAGS()))
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
