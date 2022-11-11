#!/usr/bin/python3
"""
This contains the Entry point of the command interpreter
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """
    Command Line Enterprerter class
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program
        """
        sys.exit(1)

    def do_EOF(self, args):
        """ Implement EOF so (Ctrl + D) will quit"""
        return True

    def emptyline(self):
        """If line is empty"""
        return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
