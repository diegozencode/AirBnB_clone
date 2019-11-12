#!/usr/bin/python3

"""
Module Console
"""

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    class command
    """
    msg = "Welcome to the AirBnB Clone Interpreter\n"
    sp = "=======================================\n"
    intro = "{}{}type help or ? to list commands. \n".format(msg, sp)
    prompt = "(hbnb) "
    my_classes = ["BaseModel"]

    def do_quit(self, s):
        """ quit command to exit the program """
        return True

    def help_quit(self):
        """ help quit message """
        print("Quit command to exit the program\n")

    def do_EOF(self, s):
        """ quit program"""
        print("")
        return True

    def help_EOF(self):
        """ help message EOF"""
        print("Quit command to exit the program\n")

    def emptyline(self):
        """ This method does not execute anything """
        pass

    def do_create(self, s):
        """ create a new instance """
        obj = BaseModel()
        if s == "":
            print("** class name missing **\n")
        else:
            my_list = s.split()
            if my_list[0] != obj.__class__.__name__:
                print("** class doesn't exist **\n")
            else:
                obj.save()
                print(obj.id)

    def help_create(self):
        """ help massage create """
        print("Command that saves a new register in the file storage\n")

    def show(self, s):
        """ print the string representation of an instance """
        if s == "":
            print("** class name missing **\n")
        else:
            my_list = s.split()
            if my_list[0] is not in my_classes:
                print("** class doesn't exist **\n")
            else:
                if len(my_list) == 1:
                    print("** instance id is missing **")

    def help_create(self):
        print("Save it to JSON File")
        print("Usage: \n\t (hbnb) create BaseModel\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
