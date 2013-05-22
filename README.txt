Python-Tee
==========

This module can supress, tee, or write Python's STDOUT and/or STDERR


This module allows for user control and redirection of the text
printed to the Python shell, the STDOUT/STDERR. The module may be run
using the Python with statement for a limited redirection.
Alternativly, the module may be initialized as a class and
startlog() may be called to redirect STDOUT until stoplog()
is called. The STDOUT may be redirected to a file, a string, 
the screen, or any combination there of. STDOUT may also be silenced.
Strings containting the STDOUT can be returned using the
get() command. The first time the Tee class is called in a program,
it will create or clear the log file. All subsequent calls in that
program will append STDOUT to that file. 


Tee(*name, *mode, *option)
Tee.startlog(*name, *mode, *option)

*name, default=None; This is the output file the STDOUT will
  be directed to. Only needed when using options 2, 4, 6, or 7.
           
*mode, default=''; The user may use mode to write the STDOUT file
  using binary mode or not. Leave blank to NOT use binary,
  type 'b' to use binary mode or 'b+' binary mode with reading.

*options, default 1:
  (0) Silence the STDOUT
  (1) Default, print to screen(shell) normally
  (2) Print STDOUT to file, must define a *name; mode optional
  (3) Print STDOUT to string
  (4) Print STDOUT to file and the screen
  (5) Print STDOUT to string and the screen
  (6) Print STDOUT to file, string, and the screen
  (7) Print STDOUT to a file and a string
  
*Redirect Source, default 0:
  (0) Redirect STDOUT only
  (1) Redirect STDOUT and STDERR
  (2) Redirect STDERR only 

