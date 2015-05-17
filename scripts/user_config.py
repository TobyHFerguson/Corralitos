#!/usr/bin/env python
# File:		user_config.py
# Author:	Shawn Kelley
# Date:		12-MAY-2015
# Description:	modified .bashrc files specific to each user

# globals
##
# files
ROOT_BASHRC_FILE = ('/root/.bashrc')
ROOT_VIMRC_FILE = ('/root/.vimrc')
VGRT_BASHRC_FILE = ('/home/vagrant/.bashrc')
VGRT_VIMRC_FILE = ('/home/vagrant/.vimrc')
##
# .bashrc contents 
ROOT_BASHRC = ('''# .bashrc

# User specific aliases and functions

alias c='clear'
alias x='exit'
alias ll='ls -lhF'
alias lf='ls -hF'
alias ivm='vim'
alias grpe='grep'

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
	fi
''')

_VIMRC = ('''" File:         .vimrc
" Version:      1
" Author:       Shawn Kelley
" Created:      16-APRIL-2012

" let's make things pretty
filetype plugin indent on
syntax on

" set how many lines of history VIM has to remember
set history=700

"""""""""""""""""""""""""""
" general stuff
"""""""""""""""""""""""""""
set si " smart indent
set wrap "wrap lines....probably not gonna like it...but worth a shot...
set ruler
set fileformat=unix
set foldmethod=marker
set hlsearch
''')

VGRT_BASHRC = ('''alias c='clear'
alias x='exit'
alias ll='ls -lhF'
alias lf='ls -hF'
alias ivm='vim'
alias grpe='grep'
''')

##
# functions
def update_users():
	with open(VGRT_BASHRC_FILE, 'a') as vgrt_bashrc:
		vgrt_bashrc.write(VGRT_BASHRC)
	
	with open(VGRT_VIMRC_FILE, 'w') as vgrt_vimrc:
		vgrt_vimrc.write(_VIMRC)
	
	with open(ROOT_BASHRC_FILE, 'w') as root_bashrc:
		root_bashrc.write(ROOT_BASHRC)
	
	with open(ROOT_VIMRC_FILE, 'w') as root_vimrc:
		root_vimrc.write(_VIMRC)

def main():
	update_users()

##
# main
main()
