#!/usr/bin/python3
import inspect
from models import storage
from models.base_model import BaseModel, User, City, Notaclass
from models.engine.file_storage import FileStorage

objector = BaseModel()
objector1 = BaseModel()
lst = []
dict = storage.all()
#lst = [str(dict[obj]) for obj in dict.keys()]
#print(lst)
'''
for k in dict.keys():
    exp = k.split(".")
    cl_name = exp[0]
    lst.append(cl_name)
print(lst)
for str in lst:
    print(eval(str))
mst = set(lst)
print(mst)
mst.add("chocobono")
print(mst)'''
def check_class(name, cl_name):
    if name in globals():
        return name == cl_name or issubclass(globals()[name], globals()[cl_name])
    return -1
    
name = input()
print(check_class(name, "BaseModel"))
    