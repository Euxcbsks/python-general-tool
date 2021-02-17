import os

from inspect import currentframe

__all__ = [
	'run_here'
]

class run_here():
	"""**Type**: context manager, class decorator without parameters
	
	**Description**: Execute the function in the directory where the function is located
	
	**Usage**:
	
	- with … as
	
		.. code-block:: python
			:linenos:
			
			with run_here(function[, args[, kargs]]) as function_return:
				pass
	
	- decorator
		.. code-block:: python
			:linenos:
			
			@run_here
			def func():
				pass
	
	**Example**:
		
		Main file directory: /folder/subfolder/run_here_example.py
		
		Another file directory: /folder/target.txt
	
	- with run_here(func, *args, **kargs) as …
		
		.. code-block:: python
			:linenos:
			
			def relat_open():
				os.chdir('..')
				
				with open('target.txt') as f:
					return t.read()
			
			with run_here(relat_open) as data:
				print(data)
	
	- decorator
		
		.. code-block:: python
			:linenos:
			
			@run_here
			def relat_open():
				os.chdir('..')
				
				with open('target.txt') as f:
					return t.read()
			
			print(relat_open())
	
	*run_here will auto restore work directory after function end*
	"""
	def __init__(self, func, *args, **kargs):
		if func.__class__.__name__ != "function":
			raise TypeError(f"the 'func' must be function, not '{func.__class__.__name__}'")
		
		self.func = func
		self.args = args
		self.kargs = kargs
		self.orig_path = os.getcwd()
		func_frame = currentframe().f_back
		
		if func_frame.f_globals['__file__'] == __file__:
			self.func_path = os.path.split(func_frame.f_back.f_globals['__file__'])[0]
		else:
			self.func_path = os.path.split(func_frame.f_globals['__file__'])[0]
	
	def __enter__(self):
		os.chdir(self.func_path)
		return self.func(*self.args, **self.kargs)
	
	def __exit__(self, exc_type, exc_value, exc_trackback):
		os.chdir(self.orig_path)
	
	def __call__(self, *args, **kargs):
		with run_here(self.func, *args, **kargs) as result:
			return result
