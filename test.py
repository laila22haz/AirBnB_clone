#!/usr/bin/python3
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from datetime import datetime
from time import sleep
import uuid

def is_valis_id(id):
    try:
        uuid.UUID(id)
        return True
    except ValueError:
        return False
    
def dispatch(obj):
    if isinstance(obj, BaseModel):
        return [obj.id, obj.created_at.strftime('%Y-%m-%d %H:%M:%S'), obj.updated_at.strftime('%Y-%m-%d %H:%M:%S')]
    return []
mymodel = BaseModel([1, 3, 4])

id, t1, t2 = dispatch(mymodel)
print(id, t1, t2, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(type(mymodel))
print(isinstance(mymodel, BaseModel))
print(is_valis_id("65bb642251e9434e9a966ad116dbc6a2"))
print(is_valis_id("11111111111111111111111111111111"))
mymodel.id = 5
print(str(mymodel))
print(type(str(mymodel)))
print(str(mymodel))
#print(type(mymodel))
#print(f"[BaseModel] ({mymodel.id}) {{'id': {mymodel.id}, 'created_at': {mymodel.created_at.strftime('datetime.datetime(%Y, %-m, %d, %-H, %-M, %-S, %f)')}, 'updated_at': {mymodel.updated_at.strftime('datetime.datetime(%Y, %-m, %d, %-H, %-M, %-S, %f)')})}}")
dict_output = (
                f"[BaseModel] ({mymodel.id}) "
                + "{{'id': {}, ".format(mymodel.id)
                + "'created_at': {}, "
                .format(mymodel.created_at.strftime("datetime.datetime(%Y, %-m, %d, %-H, %-M, %-S, %f)"))
                + "'updated_at': {} "
                .format(mymodel.updated_at.strftime("datetime.datetime(%Y, %-m, %d, %-H, %-M, %-S, %f)}"))
                )
print(dict_output)
'''
print(mymodel.id)
time1 = mymodel.created_at.strftime('%Y-%m-%d %H:%M:%S')
time2 = mymodel.updated_at.strftime('%Y-%m-%d %H:%M:%S')
time3 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(time1 == time3)
print(mymodel)
'''