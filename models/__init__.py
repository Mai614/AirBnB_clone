#!/usr/bin/python3
"""
This script initializes the FileStorage instance and reloads stored data.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

