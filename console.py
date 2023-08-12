#!/usr/bin/python3
"""build the console class"""


import cmd
from models.base_model import BaseModel
from models import storage
import sys

class HBNBCommand(cmd.Cmd):
    """start the program that that contains the entry point of the command interpreter""" 
    prompt = "(hbnb) "

    def do_quit(self, line):
        sys.exit()

    def do_EOF(self, line):
        "Quit command to exit the program"
        return True

    def do_create(self, line):
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        try:
            user_input = globals()[args[0]]
            obj = user_input()
            storage.save()
            print(obj.id)
        except Exception :
            print("** class doesn't exist **")


    def do_show(self, line):
        argv = line.split()
        if len(argv) < 1:
            print("** class name missing **")
            return
        try:
            globals()[argv[0]]
        except:
            print("** class doesn't exist **")
            return
        if len(argv) < 2:
            print("** instance id missing **")
            return
        try:
            key = argv[0] + "." + argv[1]
            print(storage.all()[key])
        except Exception:
            print("** no instance found **")


    def do_destroy(self, line):
        argv = line.split()
        if len(argv) < 1:
            print("** class name missing **")
            return
        try:
            globals()[argv[0]]
        except:
            print("** class doesn't exist **")
            return
        if len(argv) < 2:
            print("** instance id missing **")
            return
        try:
            key = argv[0] + "." + argv[1]
            del storage.all()[key]
            storage.save()
        except:
            print("** no instance found **")

    def do_all(self, line):
        argv = line.split()
        try:
            user_input = globals()[argv[0]]
            variable = storage.all().values()
            result = [str(value) for value in variable if isinstance(value, user_input)]
            print(result)
        except:
            print("** class doesn't exist **")
            return


    def do_update(self, line):
        args = line.split()
        class_name = globals()(args[0])
        key = args[0] + "." + args[1]
        split_id = key.split(".")
        if not args:
            print("** class name missing **")
            return
        elif not class_name:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif not split_id[1]:
            print("** no instance found **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        dict = storage.all(split_id[1])
        for value in dict.values():
            if value == args[2]:
                dict[key] == value
        return dict


    def help_quit(self):
        print("Quit command to exit the program")

    def help_create(self):
        print("Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id")

    def help_show(self):
        print("hello")

    def help_destroy(self):
        print("hello")

    def help_all(self):
        print("hello")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
