#!/usr/bin/python3
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models import storage

    
def check_class(name, cl_name):
    '''checks if name is of class cl_name or one of its subclasses'''
    return name in globals() and \
        (name == cl_name or
         issubclass(globals()[name],globals()[cl_name]))

def cmd_parsing(expr):
    pattern = r"(\w+)\.(\w+)(\((.*?)\))?"
    match = re.match(pattern, expr)
    if match:
        groups = match.groups()
        c_name, command, args = groups[0], groups[1], groups[3].split(',') if groups[3] else []
        return [command, c_name] + [el for el in args if len(args) > 0]
    return []

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    ruler = "="
    doc_header = "Documented commands (type help <topic>):"

    def default(self, line):
        if line:
            cmd_lst = cmd_parsing(line)
            if len(cmd_lst) < 2:
                print("Invalid syntax")
            else:
                command, cl_name = cmd_lst[0:2]
                args = cmd_lst[2:] if cmd_lst[2:] else []
                strs = " ".join(args)
                if strs == "":
                    eval(f"self.do_{command}('{cl_name}')")
                else:
                    eval(f"self.do_{command}('{cl_name} {strs}')")

    def do_create(self, line):
        '''Creates a new instance of a defined class'''
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if not check_class(args[0], "BaseModel"):
                print(f"** class doesn't exist **")
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
            args = arg.split()
            if not check_class(args[0], "BaseModel"):
                print(f"** class doesn't exist **")
            else:
                lst = []
                for k in dict.keys():
                    exp = k.split(".")
                    cl_name = exp[0]
                    if cl_name == args[0]:
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

    def do_count(self, line):
        '''Creates a new instance of a defined class'''
        count = 0
        if not line:
            print("** class name missing **")
        else:
            dict = storage.all()
            args = line.split()
            if not check_class(args[0], "BaseModel"):
                print(f"** class doesn't exist **")
            else:
                for k in dict.keys():
                    exp = k.split('.')
                    cl_name = exp[0]
                    if (cl_name == args[0]):
                        count += 1
                print(count)
                

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, line):
        '''EOF command to exit the program'''
        return True

if __name__ == '__main__':
 HBNBCommand().cmdloop()
