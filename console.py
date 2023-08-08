#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage

    
def check_class(name, cl_name):
    '''checks if name is of class cl_name or one of its subclasses'''
    return name in globals() and \
        (name == cl_name or
         issubclass(globals()[name],globals()[cl_name]))

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    ruler = "="
    doc_header = "Documented commands (type help <topic>):"
    
    def do_create(self, line):
        "Creates a new instance of a defined class"
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if not check_class(args[0], "BaseModel"):
                print("** class doesn't exist **")
            else:
                inst = eval(f"{args[0]}()")
                inst.save()
                print(inst.id)
             
    def help_create(self):
        '''displays the corresponding help message'''
        print("Creates a new instance of a defined class")

    def do_show(self, line):
        '''Prints the string representation of an instance\
        based on the class name and id'''
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            dict = storage.all()
            if not check_class(args[0], "BaseModel"):
                print("** class doesn't exist **")
            elif len(args) < 2:
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
        '''Deletes an instance based on the class name and id'''
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            dict = storage.all()
            if not check_class(args[0], "BaseModel"):
                print("** class doesn't exist **")
            elif len(args) < 2:
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
                lst = []
                for k in dict.keys():
                    exp = k.split(".")
                    cl_name = exp[0]
                    if cl_name == arg:
                        lst.append(str(dict[k]))
                print(lst)

    def help_all(self):
        '''displays the corresponding help message'''
        print(' '.join(["Prints all string representation of all",
                      "instances based or not on the class name"]))
    
    def do_update(self, line):
        '''Updates an instance based on the class name and id
        by adding or updating attribute'''
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            dict = storage.all()
            if not check_class(args[0], "BaseModel"):
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif f"{args[0]}.{args[1]}" not in dict.keys():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                cl_name, id, attr, val = args[:4]
                key = f"{cl_name}.{id}"
                obj = dict[key]
                setattr(obj, attr, val)
                storage.save()
                
    
        
    def help_update(self):
        print('\n'.join([' '.join(["Updates an instance based on the class",
                        "name and id by adding or updating attribute"]),
                        ' '.join(['Usage: update <class name> <id>',
                                  '<attribute name> "<attribute value>"'])]))

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, line):
        '''EOF command to exit the program'''
        return True

if __name__ == '__main__':
 HBNBCommand().cmdloop()
