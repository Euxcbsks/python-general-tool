__all__ = [
	"raise_TpE"
]

def class_name(obj):
	#type
	if obj is type:
		return obj.__class__.__name__
	#str, list, tuple, dict, ......
	if type(obj) is type:
		return obj().__class__.__name__
	#custom class
	return obj.__class__.__name__

def raise_TpE(para, *valid_types):
	if not valid_types:
		raise ValueError("the 'valid_types' can't be None")
	
	def raise_error(para, *valid_types):
		valid_types_len = len(valid_types)
		valid_types = [f"'{class_name(Type)}'" if type(Type) != str else f"'{Type}'" for Type in valid_types]
		
		if valid_types_len < 2:
			valid_types = valid_types[0]
		elif valid_types_len >= 2:
			valid_types = ", ".join(valid_types[:-1]) + f' or {valid_types[-1]}'
		
		raise TypeError(f"the '{para}' must be {valid_types}, not {class_name(para)}")
	
	#self check
	if type(para) != str:
		raise_error('para', str)
	
	#raise it as return
	raise_error(para, *valid_types)
