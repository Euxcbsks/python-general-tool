__all__ = ["asgmt_brench"]

def class_name(obj):
	#built-in
	if type(obj) is type:
		return obj().__class__.__name__
	#type or custom class
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

def asgmt_brench(obj, conditional, brench: dict, *, obj_sig = None, additional = None):
	def str_brench(obj, brench):
		try:
			return brench[obj]
		except KeyError:
			raise_TpE("obj when conditional == 'str'", str)

	def type_brench(obj, brench, obj_sig):
		try:
			return brench[class_name(obj)]
		except KeyError:
			raise_TpE(obj_sig, *brench.keys())
	
	return eval(type_brench(conditional, {
		"str": """eval(str_brench(conditional, {
			"str": "str_brench(obj, brench)",
			"type": "type_brench(obj, brench, obj_sig)"
		}))""",
		"function": "eval(conditional(obj, brench))"
	}))
