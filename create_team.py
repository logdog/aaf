import argparse
from json_helper import read_file, write_file

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