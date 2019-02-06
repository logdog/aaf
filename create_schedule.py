import argparse
from json_helper import read_file, write_file

def init_argparse():
	parser = argparse.ArgumentParser(description='Updates the schedule, and in turn the create_team script')
	parser.add_argument('week', type=str, help='(week1, week2, ..., playoff, final)')
	parser.add_argument('away', type=str, help='away team (Atlanta)')
	parser.add_argument('home', type=str, help='home team (San Antonio)')
	parser.add_argument('--away-score', type=int, default=None)
	parser.add_argument('--home-score', type=int, default=None)
	args = parser.parse_args()
	return args

def main():
	rel_path = "data/schedule.json"
	args = init_argparse()
	data = read_file(rel_path)

	from pprint import pprint
	pprint(data)

	key = args.away + " at " + args.home
	if not data[args.week]:
		data[args.week] = {}
	print(data)
	data[args.week][key] = {
		'away team': args.away,
		'home team': args.home,
		'away score': args.away_score,
		'home score': args.home_score
	}

	print("asdfasdfasdf")
	pprint(data)

	write_file(rel_path, data)

if __name__ == "__main__":
	main()