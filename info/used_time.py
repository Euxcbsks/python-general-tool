from time import time

__all__ = [
	'used_time'
]

def used_time(target = None, round_long = None):
	'''
	'''
	test_result = "function '{func_name}' used {use_time} seconds"
	
	if target.__class__.__name__ == 'function':
		def time_test(*args, **kargs):
			start_time = time()
			func_result = target(*args, **kargs)
			end_time = time()
			
			print(test_result.format(func_name = target.__name__, use_time = end_time - start_time))
			
			return func_result
		return time_test
	
	elif type(target) is int or type(round_long) is int:
		def decorator(func, round_long = target if type(target) is int else round_long, test_result = test_result):
			def time_test(*fargs, **fkargs):
				start_time = time()
				func_result = func(*fargs, **fkargs)
				end_time = time()
				
				if round_long > 0:
					print(test_result.format(func_name = func.__class__.__name__, use_time = round(end_time - start_time, round_long)))
				elif round_long == 0:
					print(test_result.format(func_name = func.__class__.__name__, use_time = end_time - start_time))
				
				return func_result
			return time_test
		return decorator
	
	else:
		if target is None:
			from inspect import currentframe
			deco_frame = currentframe().f_back
			deco_line = deco_frame.f_lineno
			deco_file = deco_frame.f_globals['__file__'].join('""')
			raise ValueError(f"File {deco_file}, line {deco_line}\n  detected '@used_time()', please remove '()' or enter a number in the '()'")
		raise ValueError(f"the 'target' must be 'int' or 'function', not {target.__class__.__name__}")
