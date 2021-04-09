import json

config_file_path = 'config.json'

def load_config(*paras):
	def load():
		with open(config_file_path, 'r', encoding = 'UTF-8') as config_file:
			return json.load(config_file)
	
	config_data = load()
	
	if not paras:
		return config_data
	if len(paras) == 1:
		return config_data[paras[0]]
	return [config_data[para] for para in paras]

def config(**paras):
	config_data = load_config()
	
	def update_config_data():
		changelog = 'change log:'
		#all_checks = {"check_name": check_by_default}
		all_checks = {"type_check": True}

		#auto generate
		need_check = {check: paras.get(check, all_checks[check]) for check in all_checks}
		check_to_func = {check: locals()[f"check_{check.split('_')[0]}"] for check in all_checks}
		checks = [check_to_func[k] for k, v in need_check if v]
		
		#customize check
		def check_type():
			if type(v) != type(config_data[k]):
				raise TypeError(f"value of '{k}' must be '{config_data[k].__class__.__name__}', not '{v.__class__.__name__}'")
		
		#run check and update
		def update_config_data():
			if v != config_data[k]:
				changelog += f"\n  '{k}': {config_data[k]} -> {v}"
				config_data[k] = v
		
		if checks:
			for k, v in paras:
				for check in checks:
					check()
				update_config_data()
		else:
			for k, v in paras:
				update_config_data()
		
		if changelog == 'change log:':
			changelog += '\n  Nothing changed'
		
		return changelog
	
	def save_config():
		with open(config_file_path, 'w', encoding = 'UTF-8') as config_file:
			json.dump(config_data, config_file, indent = '\t')
		
	if not paras:
		return json.dumps(config_data, indent = '    ')
	
	print(update_config_data())
	
	save_config()
