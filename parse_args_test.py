import sys
from parse_args import Commands

def test_flag_exists():
    commands = Commands(["-v"])

    assert(commands.has_flag("v")), "Has key 'v'"
    assert(commands.string_of("v") == None), "Value of flag 'v' is None"

def test_flag_has_correct_value():
    commands = Commands(["-v", "3"])

    assert(commands.has_flag("v")), "Has key 'v'"
    assert(commands.string_of("v") == "3"), "Has value '3' (str)"
    assert(commands.int_of("v") == 3), "Has value 3 (int)"

def test_has_multiple_flags():
    commands = Commands(["-v", "3", "--foo"])

    assert(commands.has_flag("v")), "Has key 'v'"    
    assert(commands.has_flag("foo")), "Has key 'foo'"
    assert(not commands.has_flag("3")), "Does not have key '3'"

def test_gets_sys_args():
    commands = Commands([])
    print("Parsed command line args:", commands.args)
    assert(len(commands.args) == len(sys.argv) - 1), "Args is not empty and matches length of system args without file name"

test_flag_exists()
test_flag_has_correct_value()
test_has_multiple_flags()
test_gets_sys_args()
print("Passed")