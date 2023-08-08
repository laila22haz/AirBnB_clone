#!/usr/bin/python3
import cmd
import inspect
from models.base_model import BaseModel
from models import storage

    
def check_class(name, cl_name):
    '''checks if name is of class cl_name or one of its subclasses'''
    if name in globals():
        return name == cl_name or issubclass(globals()[name], globals()[cl_name])
    return -1

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    ruler = "="
    doc_header = "Documented commands (type help <topic>):"
    
    def do_create(self, line):
        "Creates a new instance of a defined class"
        args = line.split()
        if len(args) == 1:
            print("** class name missing **")
        elif len(args) > 1 and not check_class(args[1], "BaseModel"):
            print("** class doesn't exist **")
        else:
            inst = BaseModel()
            inst.save()
            print(inst.id)
             
    def help_create(self):
        '''displays the corresponding help message'''
        print("Creates a new instance of a defined class")

    def do_show(self, line):
        """Prints the string representation of an instance\
        based on the class name and id"""
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            dict = storage.all()
            if len(args) == 1:
                if not check_class(args[0], "BaseModel"):
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            elif f"{args[0]}.{args[1]}" not in dict.keys():
                print("** no instance found **")
            else:
                key = f"{args[0]}.{args[1]}"
                obj = dict[key]
                print(obj)

    def help_show(self):
        '''displays the corresponding help message'''
        print('\n'.join([' '.join(["Prints the string representation of an",
                        "instance based on the class name and id"]),
                        "Usage : show <class_name> <instance id>"]))
    
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            dict = storage.all()
            if len(args) == 1:
                if not check_class(args[0], "BaseModel"):
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            elif f"{args[0]}.{args[1]}" not in dict.keys():
                print("** no instance found **")
            else:
                cl_name, id = args
                key = f"{cl_name}.{id}"
                del dict[key]
                storage.save()

    def help_destroy(self):
        '''displays the corresponding help message'''
        print("Deletes an instance based on the class name and id")

    def do_all(self, arg):
        '''Prints all string representation of all instances
        based or not on the class name'''
        dict = storage.all()
        if not arg:
            lst = [str(dict[obj]) for obj in dict.keys()]
            print(lst)
        else:
            if not check_class(arg, "BaseModel"):
                print("** class doesn't exist **")
            else:
                for k in dict.keys():
                    exp = k.split()
                    cl_name = exp[0]
                lst = [str(dict[obj]) for obj in dict.keys() if cl_name == arg]
                print(lst)

    def help_all(self):
        '''displays the corresponding help message'''
        print(' '.join(["Prints all string representation of all",
                      "instances based or not on the class name"]))
    """
    def do_update(self, line):
        '''Updates an instance based on the class name and id
        by adding or updating attribute'''
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            dict = storage.all()
            if len(args) == 1:
                if args[0] not in globals():
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            elif f"{args[0]}.{args[1]}" not in dict.keys():
                print("** no instance found **")
    """
        
    def help_update(self):
        print('\n'.join([' '.join(["Updates an instance based on the class",
                        "name and id by adding or updating attribute"]),
                        ' '.join(['Usage: update <class name> <id>',
                                  '<attribute name> "<attribute value>"'])]))

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    def do_EOF(self, line):
        "EOF command to exit the program"
        return True

if __name__ == '__main__':
 HBNBCommand().cmdloop()
