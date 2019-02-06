import argparse
from json_helper import read_file, write_file

def init_argparse():
	parser = argparse.ArgumentParser(description='Reset all teams back to empty records')
	args = parser.parse_args()
	return args

def main():
	rel_path = "data/teams.json"
	args = init_argparse()
	data = read_file(rel_path)

	for team, stats in data.items():
		stats['wins'] = 0
		stats['losses'] = 0
		stats['ties'] = 0

	write_file(rel_path, data)

if __name__ == "__main__":
	main()