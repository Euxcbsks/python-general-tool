target = dict()
token_separate = "."

def token_parser(token):
	if token_separate in token:
		#don't want use "global" to avoid Unbound local error
		copy_target = target
		
		#overwrite "copy_target" with subtarget
		for k in token.split(token_separate):
			copy_target = copy_target[k]
	else:
		copy_target = target[token]
	
	return copy_target
