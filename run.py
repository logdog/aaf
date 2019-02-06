from json_helper import read_file, write_file
import argparse
import re

def get_team_names(game):
	# "Atlanta at San Antonio" -> away = Atlanta, home = San Antonio
	x = re.findall('(.+?) at (.+)', game)[0]
	away = x[0]
	home = x[1]
	return away, home

def run_simulation(teams, schedules):
	for obj in schedules.values():
		games = obj.keys() # [Atlanta at Orlando, etc.]
		for game in games:
			away, home = get_team_names(game)
			obj = obj[game] # lazy typing

			if obj["away score"] == None or obj["home score"] == None:
				continue
			elif obj["away score"] == obj["home score"]:
				teams[away]['ties'] += 1
				teams[home]['ties'] += 1
			elif obj["away score"] > obj["home score"]:
				teams[away]['wins'] += 1
				teams[home]['losses'] += 1
			elif obj["away score"] < obj["home score"]:
				teams[away]['losses'] += 1
				teams[home]['wins'] += 1

	import pprint
	pprint.pprint(teams)

def get_teams():
	teams = read_file("data/teams.json")
	return teams

def get_schedules():
	schedules = read_file("data/schedule.json")
	return schedules

def init_argparse():
	parser = argparse.ArgumentParser(description='Updates the team\'s record once the scehdule is made')
	args = parser.parse_args()
	return args

def main():
	args = init_argparse()
	teams = get_teams()
	schedules = get_schedules()
	run_simulation(teams, schedules)
	pass

if __name__ == "__main__":
	main()