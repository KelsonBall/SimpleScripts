import sys

class Commands:

    flags = {}

    def __init__(self, args):
        if len(args) == 0:
            args = sys.argv[1:]
        self.args = args
        self.parse_commands(args)

    def parse_commands(self, args):
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

    def has_flag(self, flag):
        return flag in self.flags
    
    def string_of(self, flag):
        if self.has_flag(flag):
            return self.flags[flag]
        return None

    def int_of(self, flag):
        if self.has_flag(flag):
            return int(self.flags[flag])
        return None
