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
		
		for k, v in paras.items():
			#Check type
			if type(v) != type(config_data[k]):
				raise TypeError(f"value of '{k}' must be {config_data[k].__class__.__name__}, not {v.__class__.__name__}")
			#Check value, if not same, update changelog and config_data
			if config_data[k] != v:
				changelog = changelog + f"\n  '{k}': {config_data[k]} -> {v}"
				config_data[k] = v
		
		if changelog == 'change log:':
			changelog = changelog + '\n  Nothing changed'
		
		return changelog
		
	def save_config():
		with open(config_file_path, 'w', encoding = 'UTF-8') as config_file:
			json.dump(config_data, config_file, indent = '\t')
		
	if len(paras) == 0:
		print(json.dumps(config_data, indent = '    '))
		return
	
	print(update_config_data())
	
	save_config()
