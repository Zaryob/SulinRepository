#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

    # Use secure delete. Even if the data is deleted with sqlite query, the traces of the deleted data still remains in the file
    # but cannot be seen with sqlite query. However, it can be seen by opening the file with a text editor.
    # SQLITE_SECURE_DELETE overwrites written data with zeros.
def setup():
    inarytools.cflags.add("-DSQLITE_SECURE_DELETE=1",
                         "-DSQLITE_ENABLE_UNLOCK_NOTIFY=1",
                         "-DSQLITE_ENABLE_COLUMN_METADATA=1",
                         "-DSQLITE_DISABLE_DIRSYNC",
                         "-DSQLITE_ENABLE_FTS3=1",
                         "-DSQLITE_ENABLE_FTS4",
                         "-DSQLITE_ENABLE_FTS5",
                         "-DSQLITE_ENABLE_DBSTAT_VTAB=1",
                         "-DSQLITE_ENABLE_FTS3_PARENTHESIS",
                         "-DSQLITE_ENABLE_FTS3_TOKENIZER=1",
                         "-DSQLITE_ENABLE_STMT_SCANSTATUS",
                         "-DSQLITE_SOUNDEX",
                         "-DSQLITE_ENABLE_RTREE",
                         "-DSQLITE_ENABLE_API_ARMOR")

    inarytools.cflags.sub("-O[s\d]", "-O3")

    autotools.configure("--disable-static \
                         --disable-editline \
                         --enable-fts3 \
                         --enable-fts4 \
                         --enable-fts5 \
                         --enable-rtree \
                         --enable-json1 \
                         --enable-threadsafe")

def build():
    autotools.make("-j1")


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("README*")

    shelltools.cd("%s/sqlite-doc-3260000" % get.workDIR())
    shelltools.system("pwd")

    inarytools.insinto("/usr/share/doc/sqlite", "../sqlite-doc-3260000/*")

    shelltools.system("find %s -type f -perm 755 -exec ls -lha {} \;" % get.installDIR())
    shelltools.system("find %s -type f -perm 755 -exec chmod 644 {} \;" % get.installDIR())
    shelltools.system("find %s -type f -name '*~' -exec ls -lha {} \;" % get.installDIR())
    shelltools.system("find %s -type d -name '*~' -exec ls -lha {} \;" % get.installDIR())
    shelltools.system("find %s -name '*~' -exec rm -f {} \;" % get.installDIR())
    shelltools.system("find %s -type f -name '.~*' -exec ls -lha {} \;" % get.installDIR())# /build/pkg/sqlite-doc/usr/share/doc/sqlite/images/fileformat/.~lock.indexpage.odg#
    shelltools.system("find %s -type d -name '.~*' -exec ls -lha {} \;" % get.installDIR())
    shelltools.system("find %s -name '.~*' -exec rm -f {} \;" % get.installDIR())
