from os import chdir

__all__ = [
	'rel_chdir'
]

def rel_chdir(path):
	if path.startswith('...'):
		layer, path = path.split('/', 1)
		
		while len(layer) > 1:
			chdir('..')
			layer = layer[1:]
	
	chdir(path)
