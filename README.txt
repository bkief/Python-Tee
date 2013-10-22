Python-Tee
==========

This module can supress, tee, or write Python's STDOUT and/or STDERR
cTee uses a fast C implimentation for writing to string objects


This module allows for user control and redirection of the text
printed to the Python shell, the STDOUT/STDERR. The module may be run
using the Python with statement for a limited redirection.
Alternativly, the module may be initialized as a class and
startlog() may be called to redirect STDOUT/STDERR until stoplog()
is called. The STDOUT/STDERR may be redirected to a file, a string, 
the screen, or any combination there of. STDOUT/STDERR may also be silenced.
Strings containting the STDOUT/STDERR can be returned using the
get() command. The first time the Tee class is called in a program,
it will create or clear the log file. All subsequent calls in that
program will append STDOUT/STDERR to that file. 


Tee(*name, *mode, *option, *RedirectSource)
Tee.startlog(*name, *mode, *option, *RedirectSource)

*name, default=None; This is the output file the STDOUT/STDERR will
    be directed to. Only needed when using options 2, 4, 6, or 7.
         
*mode, default=''; The user may use mode to write the STDOUT/STDERR file
    using binary mode or not. Leave blank to NOT use binary,
    type 'b' to use binary mode or 'b+' binary mode with reading.

*options, default 1:
    (0) Silence the STDOUT/STDERR
    (1) Default, print to screen(shell) normally
    (2) Print STDOUT/STDERR to file, must define a *name; mode optional
    (3) Print STDOUT/STDERR to string
    (4) Print STDOUT/STDERR to file and the screen
    (5) Print STDOUT/STDERR to string and the screen
    (6) Print STDOUT/STDERR to file, string, and the screen
    (7) Print STDOUT/STDERR to a file and a string

*Redirect Source, default 0:
    (0) Redirect STDOUT only
    (1) Redirect STDOUT and STDERR
    (2) Redirect STDERR only 

