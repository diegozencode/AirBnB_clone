#!/usr/bin/python3
"""
    Module Console
"""
import cmd
from models.base_model import BaseModel
import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class command

    Attributes:
        msg (str): console welcome message
        sp (str): separator text
        intro (str): helpful welcome message
        my_classes (obj:list of str): classes options
    """
    msg = "Welcome to the AirBnB Clone Interpreter\n"
    sp = "=======================================\n"
    intro = "{}{}type help or ? to list commands. \n".format(msg, sp)
    prompt = "(hbnb) "
    my_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

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
        print("Quit command to exit the program")

    def emptyline(self):
        """ This method does not execute anything """
        pass

    def do_create(self, args):
        """ create a new instance """
        obj = BaseModel()
        if args == "":
            print("** class name missing **")
        else:
            my_list = args.split()
            if my_list[0] != obj.__class__.__name__:
                print("** class doesn't exist **")
            else:
                obj.save()
                print(obj.id)

    def help_create(self):
        """ help massage create """
        print("Command that saves a new register in the file storage\n")
        print("Usage: \n\t (hbnb) create BaseModel\n")

    def do_show(self, args):
        """ print the string representation of an instance """
        if args == "":
            print("** class name missing **")
        else:
            my_list = args.split()
            if my_list[0] not in self.my_classes:
                print("** class doesn't exist **")
            else:
                if len(my_list) == 1:
                    print("** instance id is missing **")
                else:
                    myobj = "{}.{}".format(my_list[0], my_list[1])
                    if myobj in models.storage.all().keys():
                        print(models.storage.all()[myobj])
                    else:
                        print("** no instance found **")

    def do_destroy(self, args):
        """Delete an instance based on the class name and id"""
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
        my_list = args.split()
        my_all = []
        if len(my_list) == 0 or my_list[0] in self.my_classes:
            my_dict = models.storage.all()
            for i in my_dict.keys():
                obj = my_dict[i]
                my_list.append(str(obj))
            print(my_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Update data"""
        if args == "":
            print("** class name missing **")
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
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
