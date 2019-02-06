import json
import os

def read_file(rel_path):
	script_dir = os.path.dirname(__file__)
	file_path = os.path.join(script_dir, rel_path)
	if not os.path.exists(file_path):
		with open(file_path, 'w') as fi:
			fi.write("")
	data = {}
	with open(file_path, 'r') as fi:
		try:
			data = json.load(fi)
		except Exception as e:
			data = {}
	return data

def write_file(rel_path, data):
	script_dir = os.path.dirname(__file__)
	file_path = os.path.join(script_dir, rel_path)
	with open(file_path, 'w') as fi:
	    json.dump(data, fi)