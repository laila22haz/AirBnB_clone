#!/usr/bin/python3
"""package handler to call Filestorage"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
