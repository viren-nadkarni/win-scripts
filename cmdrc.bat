@echo off
doskey ls=dir /b
doskey cat=type $*
doskey rm=del $*
doskey diff=fc $*
doskey mv=move $*
doskey cp=copy $*

doskey py=C:\Python27\python $*
doskey ipy=ipython
doskey p=ping goo.gl
doskey a=arp -a