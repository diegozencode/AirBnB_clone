#!/usr/bin/python3

"""
Module Console
"""

import cmd
from models.base_model import BaseModel
import models
from models.user import User

class HBNBCommand(cmd.Cmd):
    """
    class command
    """
    msg = "Welcome to the AirBnB Clone Interpreter\n"
    sp = "=======================================\n"
    intro = "{}{}type help or ? to list commands. \n".format(msg, sp)
    prompt = "(hbnb) "
    my_classes = ["BaseModel"]

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
        # my_classes = ["BaseModel"]
        if args == "":
            print("** class name missing **\n")
        else:
            my_list = args.split()
            if my_list[0] not in self.my_classes:
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
                    
        if my_list[0] in self.my_classes:
            if len(my_list) > 1:
                key = my_list[0] + "." + my_list[1]
                if key in models.storage.all().keys():
                    del models.storage.all()[key]
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all registers"""
        # my_classes = ["BaseModel"]
        my_list = args.split()
        my_all = []
        if len(my_list) == 0 or my_list[0] in self.my_classes:
            my_dict = models.storage.all()
            for i in my_dict.keys():
                obj = my_dict[i]
                my_list.append(str(obj))
            print(my_list)
        else:
            print("** class doesn't exist **\n")

    def do_update(self, args):
        """Update data"""
        # my_classes = ["BaseModel"]
        if args == "":
            print("** class name missing **\n")
        else:
            my_list = args.split()
            if my_list[0] in self.my_classes:
                if len(my_list) > 1:
                    key = my_list[0] + "." + my_list[1]
                    my_dict = models.storage.all()
                    if key in my_dict.keys():
                        if len(my_list) > 2:
                            if len(my_list) > 3:
                                new_str = my_list[3].strip('\"')
                                setattr(my_dict[key], my_list[2], new_str)
                                models.storage.save()
                            else:
                                print("** value missing **\n")
                        else:
                            print("** attribute name missing **\n")
                    else:
                        print("** no instance found **\n")
                else:
                    print("** instance id missing **\n")
            else:
                print("** class doesn't exist **\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
