#!/usr/bin/python3

"""
Module Console
"""

import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """
    class command
    """
    msg = "Welcome to the AirBnB Clone Interpreter\n"
    sp = "=======================================\n"
    intro = "{}{}type help or ? to list commands. \n".format(msg, sp)
    prompt = "(hbnb) "

    def do_quit(self, args):
        """ quit command to exit the program """
        return True

    def help_quit(self):
        """ help quit message """
        print("Quit command to exit the program\n")

    def do_EOF(self, args):
        """ quit program"""
        print("")
        return True

    def help_EOF(self):
        """ help message EOF"""
        print("Quit command to exit the program\n")

    def emptyline(self):
        """ This method does not execute anything """
        pass

    def do_create(self, args):
        """ create a new instance """
        obj = BaseModel()
        if args == "":
            print("** class name missing **\n")
        else:
            my_list = args.split()
            if my_list[0] != obj.__class__.__name__:
                print("** class doesn't exist **\n")
            else:
                obj.save()
                print(obj.id)

    def help_create(self):
        """ help massage create """
        print("Command that saves a new register in the file storage\n")
        print("Save it to JSON File")
        print("Usage: \n\t (hbnb) create BaseModel\n")

    def do_show(self, args):
        """ print the string representation of an instance """
        my_classes = ["BaseModel"]
        if args == "":
            print("** class name missing **\n")
        else:
            my_list = args.split()
            if my_list[0] not in my_classes:
                print("** class doesn't exist **\n")
            else:
                if len(my_list) == 1:
                    print("** instance id is missing **\n")
                else:
                    myobj = "{}.{}".format(my_list[0], my_list[1])
                    if myobj in models.storage.all().keys():
                        print(models.storage.all()[myobj])
                    else:
                        print("** no instance found **\n")

    def do_destroy(self, args):
        """Deletesan instance based on the class name and id"""
        my_list = args.split()
        if len(my_list) is 0:
            print("** class name missing **")
            return False
                    
        if my_list[0] in classes:
            if my_list > 1:
                key = my_list[0] + "." + my_list[1]
                if key in my_list:
                    del model.storage.all()[key]
                    models.storage.save()
                else:
                    print("** instance id missing **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
