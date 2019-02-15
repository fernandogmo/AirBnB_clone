#!/usr/bin/python3
import cmd
import sys
import os

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    file = None

    def do_EOF(self, args):
        """EOF command to exit the program
        """
        print()
        return True

    def help_help(self):
        pass

    def do_quit(self, args):
        """Quit command to exit the program
        """
        raise SystemExit

    def do_create(self, args):
        """Creates a new instance of BaseModel
        """
        pass

    def do_show(self, args):
        """Prints the string representation of an instance
        """
        pass

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        """
        pass

    def do_all(self, args):
        """Prints all string representation of all instances
        """
        pass

    def do_update(self, args):
        """Updates an instance based on the class name and id
        """
        pass

    def emptyline(self):
        """Called when empty line is entered in prompt
        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

def parse(args):
    """Convert a series of zero or more numbers to an argument tuple
    """
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
