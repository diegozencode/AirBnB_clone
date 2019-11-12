#!/usr/bin/python3

"""
Module Console
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    class command
    """
    intro = ''
    prompt = '(hbnb) '

    def do_quit(self, argv):
        """Quit command to exit the program"""
        return True

    def do_EOF(self):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """This method do not execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
