" Vim plugin
" Purpose:      Intelligently create content for INARY's action.py files
" Author:       A. Murat Eren
" Copyright:    Copyright (c) 2005 A. Murat Eren & S. Çağlar Onur
" Licence:      You may redistribute this under the terms of the GNU GPL v2..

if &compatible || v:version < 603
    finish
endif

fun! MakeNewActionsPY()
    set nopaste

    0 put = '# -*- coding: utf-8 -*-'
    put = '#'
    put = '# Copyright (C) YEAR, YOUR NAME'
    put = '# Licensed under the GNU General Public License, version 2.'
    put = '# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt'
    put = ''
    put = 'from inary.actionsapi import autotools'
    put = 'from inary.actionsapi import inarytools'
    put = 'from inary.actionsapi import get'
    put = ''
    put = 'def setup():'
    put = '    pass'
    put = ''
    put = 'def build():'
    put = '    pass'
    put = ''
    put = 'def install():'
    put = '    pass'
    14
endfun

com! -nargs=0 NewActionsPY call MakeNewActionsPY()

augroup NewActionsPY
    au!
    autocmd BufNewFile actions.py call MakeNewActionsPY()
augroup END

" vim: set et foldmethod=marker : "
