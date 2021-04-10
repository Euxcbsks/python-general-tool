__all__ = ["asgmt_brench"]

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

def asgmt_brench(obj, brench_type: str, brench: dict, *, obj_sig = None):
	def str_brench(obj, brench):
		if type(obj) is not str:
			raise_TpE("obj when brench_type == 'str'", str)

		return brench[obj]

	def type_brench(obj, brench, obj_sig):
		obj_type = class_name(obj)
		
		if obj_type not in brench:
			raise_TpE(obj_sig, *brench.keys())
		
		return brench[obj_type]

	return eval(str_brench(brench_type, {
		"str": "str_brench(obj, brench)",
		"type": "type_brench(obj, brench, obj_sig)"
		}))