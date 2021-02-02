import os
# Usage: run_here

from inspect import currentframe
# Usage: run_here

__all__ = [
	'run_here'
]

class run_here():
	"""
	**Type**: context manager
	
	**Usage**:
	
	.. code-block:: python
		:linenos:
		
		with run_here(function[, args[, kargs]]) as function_return:
			# do something...
	
	**Description**: Execute the function in the directory where the function is located
	
	**Example**:
	
	 File directory: /folder/subfolder/run_here_example.py
	 
	 Another file directory: /folder/target.txt
	 
	.. code-block:: python
		:linenos:
		
		def relat_open(encoding = 'UTF-8'):
			os.chdir('..')
			
			with open('target.txt', encoding = encoding) as f:
				return t.read()
			
		with run_here(relat_open, 'utf-8') as f:
			print(f)
	
	*run_here will auto restore work directory after function end*
	"""
	def __init__(self, func, *args, **kargs):
		if func.__class__.__name__ != "function":
			raise TypeError(f"the 'func' must be function, not '{func.__class__.__name__}'")
		
		self.func = func
		self.args = args
		self.kargs = kargs
		self.orig_path = os.getcwd()
		self.func_path = os.path.split(currentframe().f_back.f_globals['__file__'])[0]
	
	def __enter__(self):
		os.chdir(self.func_path)
		return self.func(*self.args, **self.kargs)
	
	def __exit__(self, exc_type, exc_value, exc_trackback):
		os.chdir(self.orig_path)
