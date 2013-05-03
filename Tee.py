import StringIO
import sys


newlog = True
class Tee(object):

    """This module allows for user control and redirection of the text
       printed to the Python shell, the STDOUT. The module may be run
       using the Python with statement for a limited redirection.
       Alternativly, the module may be initialized as class and
       startlog() may be called to redirect STDOUT until stoplog()
       is called. The STDOUT may be redirected to a file, a string, 
       the screen, or any combination there of. STDOUT may also be silenced.
       Strings containting the STDOUT can be returned using the
       get() command. The first time the Tee class is called in a program,
       it will create or clear the log file. All subsequent calls in that
       program will append STDOUT to that file. 


       Tee(*name, *mode, *option)

       *name, default=None; This is the output file the STDOUT will
           be directed to. Only needed when using options 2, 4, 6, or 7.
           
       *mode, default=''; The user may use mode to write the STDOUT file
           using binary mode or not. Leave blank to NOT use binary,
           type 'b' to use binary mode or 'b+' binary mode with reading.

       *options, default 1:
           (0) Silence the STDOUT
           (1) Default, print to screen(shell) normally
           (2) Print STDOUT to file, must define a *name, mode optional
           (3) Print STDOUT to string
           (4) Print STDOUT to file and the screen
           (5) Print STDOUT to string and the screen
           (6) Print STDOUT to file, string, and the screen
           (7) Print STDOUT to a file and a string
        

       """
    
    def __init__(self, name=None, mode='', option=1):
        self.name = name
        self.mode = mode
        self.option = option
            
    def __enter__(self):
        self.startlog(self.name, self.mode, self.option)
        return self

    def __exit__(self, name, mode, data):
        sys.stdout = self.stdout
        sys.stderr = self.stderr
        if ((self.option == 2) or
            (self.option == 4) or
            (self.option == 6) or
            (self.option == 7)):
            self.filename.close()
        elif ((self.option == 3) or
              (self.option == 5) or
              (self.option == 6) or
              (self.option == 7)):
            self.text.close()

    def __del__(self):
        try:
            self.filename.close()
        except:
            pass

        try:
            self.text.close()
        except:
            pass
        finally:
            sys.stdout = self.stdout
            sys.stderr = self.stderr

    def startlog(self, name=None, mode=None, option=None):
        """ This function starts redirecting the STDOUT once the Tee class
        has been initialized. It may be stopped by using the stoplog()
        function.

        *name, default=None; This is the output file the STDOUT will
           be directed to. Only needed when using options 2, 4, 6, or 7.
           
        *mode, default=''; The user may use mode to write the STDOUT file
           using binary mode or not. Leave blank to NOT use binary,
           type 'b' to use binary mode or 'b+' binary mode with reading.

        *options, default 1:
           (0) Silence the STDOUT
           (1) Default, print to screen(shell) normally
           (2) Print STDOUT to file, must define a *name, mode optional
           (3) Print STDOUT to string
           (4) Print STDOUT to file and the screen
           (5) Print STDOUT to string and the screen
           (6) Print STDOUT to file, string, and the screen
           (7) Print STDOUT to a file and a string"""
        
        global newlog
        if (name == None) and (mode == None) and (option == None):
            name = self.name
            mode = self.mode
            option = self.option
 
        self.option = option
        if (option == 2) or (option == 4) or (option == 6) or (option == 7):
            if newlog:
                self.filename = open(name, 'w'+mode)
                newlog = False
            else:
                self.filename = open(name, 'a'+mode)

        if (option == 3) or (option == 5) or (option == 6) or (option == 7):
            self.text = StringIO.StringIO()

        self.temp = ''
        self.temp2 = ''
        self.stderr = sys.stderr
        sys.stderr = self

        self.stdout = sys.stdout
        sys.stdout = self
        

    def stoplog(self):
        """This function may be called from the class to stop redirecting
            STDOUT."""
        
        sys.stdout = self.stdout
        sys.stderr = self.stderr
        try:
            self.filename.close()
        except:
            pass
        try:
            self.text.close()
        except:
            pass

    def write(self, data):
        data = data.replace("\n", "\r\n")
        if self.option == 1:
            self.stdout.write(data)
        elif self.option == 2:
            self.filename.write(data)
            self.filename.flush()
        elif self.option == 3:
            self.text.write(data)
            self.text.flush()
        elif self.option == 4:
            self.stdout.write(data)
            self.filename.write(data)
            self.filename.flush()
        elif self.option == 5:
            self.stdout.write(data)
            self.text.write(data)
            self.text.flush()
        elif self.option == 6:
            self.stdout.write(data)
            self.filename.write(data)
            self.filename.flush()
            self.text.write(data)
            self.text.flush()
        elif self.option == 7:
            self.filename.write(data)
            self.filename.flush()
            self.text.write(data)
            self.text.flush()
        else:
            pass

    def get(self):
        """The get() function can be used to return the string containing
            STDOUT"""

        try:
            x = self.text.getvalue()
            x = x.rstrip("\r\n")
        except:
            x = 'Error: String Catcher Not Initalized'
        return x

#############################################################################

def test():
    with Tee('logfile.log', 'b', option=3) as Redirect:
        print 'I am the walrus'
        x = Redirect.get()

    print x   
    
    print 'coocoocachoo'

    with Redirect:
        print 'test'

    print 'notest'
    x = Redirect.get()
    print x
    Redirect.startlog()
    print 'I am the eggman'
    Redirect.stoplog()

    print 'coocoocachoo'
    print "\n"

    Redirect.startlog(option=3)
    print 'Because, it was the'
    x = Redirect.get()
    Redirect.stoplog()
    
    print x

    with Tee(option=0):
        print 'Sound of Silence'
        print 'Simon and Garfunkel'
        
      

if __name__ == '__main__':
    help(Tee)
    test()

