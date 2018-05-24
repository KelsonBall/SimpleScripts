import sys

# Represents a key-value map of flags/values
class Commands:

    flags = {}

    # creates a parsed commands instance from an array of args
    # pass an empty args array to use args from sys.argv
    def __init__(self, args):
        if len(args) == 0:
            args = sys.argv[1:] # skip name of file
        self.args = args
        self._parse_commands(args)

    def _parse_commands(self, args):
        flag = None
        for arg in args:
            if not flag == None: 
                self.flags[flag] = arg 
                flag = None
            elif arg[0] == "-": 
                if arg[1] == "-": 
                    flag = arg[2:]
                else:
                    flag = arg[1:]
                self.flags[flag] = None 
            else: 
                self.flags[arg] = None

    # checks if a the specified flag exists
    def has_flag(self, flag):
        return flag in self.flags
    
    # returns the string value of the flag, or None
    def string_of(self, flag):
        if self.has_flag(flag):
            return self.flags[flag]
        return None

    # returns the integer value of the flag, or None
    # will error if the value of the flag cannot be parsed as an int
    def int_of(self, flag):
        if self.has_flag(flag):
            return int(self.flags[flag])
        return None
