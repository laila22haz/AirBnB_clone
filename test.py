#!/usr/bin/python3
import re
from models import storage
from models.base_model import BaseModel
from models.user import User

def cmd_parsing(expr):
    pattern = r"(\w+)\.(\w+)(\((.*?)\))?"
    match = re.match(pattern, expr)
    groups = match.groups()
    c_name, command, args = groups[0], groups[1], groups[3].split(',') if groups[3] else []
    return [command, c_name] + [el.strip('" ') for el in args if len(args) > 0]
    #return [el for el in match.groups() if el]
    

strg = 'BaseModel.all("arg1", "arg2", "argus 3")'
valid = cmd_parsing(strg)
print(valid)
str = ""
for el in valid[1:]:
    str += f"{el} "
print(str)
command, cl_name = valid[0:2]
args = valid[2:] if valid[2:] else []
strs = " ".join(args)
if strs == "":
    print(f"self.do_{command}({cl_name})")
else:
    print(f"self.do_{command}({cl_name} {strs})")
'''
cl_name = match.group(1)
cmd = match.group(2)
args = match.group(3)
print(f"{cl_name}, {cmd}, {args.split(',')}")
'''
'''
parts = str.split('.')
print(parts[1])
parts2 = parts[1].split('(')

print(parts2)
'''