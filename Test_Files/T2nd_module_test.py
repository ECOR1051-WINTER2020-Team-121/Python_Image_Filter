
#import module_test

#print("--2nd module_test prints --")
#print("After import __name__ is", __name__, "and module_test.__name__ is", module_test.__name__)

# In conclusion, calling __name__ gives the name of the file, if it is not the main file.
# Doesn't this sound an awful lot like C??? I suppose it is. The main file has __main__.
# And the rest have a value of __name__ = filename. There is only one __main__. And that is
# the main program file. Not the modules. No matter whether __main__ is called inside of a module,
# if it is not the main file, then __main__ is the main file.

# Hypothesis: Importing modules is import, and executing modules is when you literally
# execute it like as if it were any file

def print_name():
    print(__name__)