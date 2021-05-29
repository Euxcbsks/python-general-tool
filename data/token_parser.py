def token_parser(target: dict, token, separate = '.'):
	if separate in token:
		#overwrite "target" with subtarget
		for k in token.split(separate):
			target = target[k]
	else:
		target = target[token]
	
	return target
