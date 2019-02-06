import argparse
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

def init_argparse():
	parser = argparse.ArgumentParser(description='Generate a team, and add them to the JSON list of teams (teams.json)')
	parser.add_argument('city', type=str, help='city name')
	parser.add_argument('mascot', type=str, help='mascot')
	parser.add_argument('--wins', default=0, type=int, help='number of wins')
	parser.add_argument('--losses', default=0, type=int, help='number of losses')
	parser.add_argument('--ties', default=0, type=int, help='number of ties')
	args = parser.parse_args()
	return args

def main():
	rel_path = "data/teams.json"
	args = init_argparse()
	data = read_file(rel_path)

	data[args.city] = {
		'city': args.city,
		'mascot': args.mascot,
		'wins': args.wins,
		'losses': args.losses,
		'ties': args.ties
	}

	write_file(rel_path, data)

if __name__ == "__main__":
	main()