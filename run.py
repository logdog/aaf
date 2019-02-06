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
			ogame = obj[game]

			if ogame["away score"] == None or ogame["home score"] == None:
				continue
			elif ogame["away score"] == ogame["home score"]:
				teams[away]['ties'] += 1
				teams[home]['ties'] += 1
			elif ogame["away score"] > ogame["home score"]:
				teams[away]['wins'] += 1
				teams[home]['losses'] += 1
			elif ogame["away score"] < ogame["home score"]:
				teams[away]['losses'] += 1
				teams[home]['wins'] += 1
	return teams

def get_teams():
	teams = read_file("data/teams.json")
	return teams

def get_schedules():
	schedules = read_file("data/schedule.json")
	return schedules

def update_teams(teams):
	write_file("data/teams.json", teams)
	return teams

def init_argparse():
	parser = argparse.ArgumentParser(description='Updates the team\'s record once the scehdule is made')
	args = parser.parse_args()
	return args

def main():
	args = init_argparse()
	teams = get_teams()
	schedules = get_schedules()
	new_teams = run_simulation(teams, schedules)
	update_teams(new_teams)
	pass

if __name__ == "__main__":
	main()