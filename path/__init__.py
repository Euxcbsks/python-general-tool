import os

this_file_path = os.path.split(__file__)[0]

for file in os.listdir(this_file_path):
	if not file.startswith('__'):
		file  = file[:-3]
		exec(f"from .{file} import *")

del os, this_file_path, file
