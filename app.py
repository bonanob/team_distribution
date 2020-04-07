import sys
import constants as cons
import random


def validate_input(prompt, options, loop=False):
    if loop is True:
        while True:
            try:
                val = input(prompt)
                if val.lower() not in (options):
                    raise ValueError
            except ValueError:
                print("Ooops! Something went wrong. try again.\n\n")
                continue
            else:
                return val
    else:
        try:
            val = input(prompt)
            if val.lower() not in options:
                raise ValueError
        except ValueError:
            print("Ooops! Something went wrong. try again.\n\n")
        else:
            return val


if __name__ == '__main__':
    all_players = cons.PLAYERS
    all_teams_players = [[] for i in range(len(cons.TEAMS))]
    exp_players = []
    inexp_players = []

    for i in range(len(all_players)):
        all_players[i]['height'] = int(all_players[i]['height'].strip(' inches'))
        all_players[i]['guardians'] = all_players[i]['guardians'].split(' and ')
        if all_players[i]['experience'] == 'YES':
            exp_players.append(all_players[i])
            all_players[i]['experience'] = True
        else:
            inexp_players.append(all_players[i])
            all_players[i]['experience'] = False

    random.shuffle(exp_players)
    random.shuffle(inexp_players)

    for i in range(len(exp_players)):
        all_teams_players[i % len(all_teams_players)].append(exp_players[i])

    for i in range(len(inexp_players)):
        all_teams_players[-(i % len(all_teams_players))].append(inexp_players[i])

    print("\n************************************")
    print("            TEAM DIVIDER            ")
    print("************************************\n\n")

    restart = 'y'
    while restart.lower() == 'y':
        print("----------------------------------\n")
        print("   1. Display Team Stats")
        print("   2. Quit\n")
        start_or_quit_options = ('1', '2')
        start_or_quit = str(validate_input("Enter an option:  ", start_or_quit_options))

        if start_or_quit == '1':
            print("\n")
            for i, team in enumerate(cons.TEAMS, 1):
                print(f'   {i}. {team}')

            try:
                choose_team_option = [str(i) for i in range(1, (len(all_teams_players)+1)) ]
                print()
                choose_team = validate_input("Enter an option:  ", choose_team_option)
                choose_team = int(choose_team) - 1
            except TypeError:
                continue

            num_team_exp_plyrs = 0
            print("\n-----------------\n")
            print("TEAM:", cons.TEAMS[choose_team], end='\n\n')
            print("Number of players:  ", len(all_teams_players[choose_team]))
            for i in range(len(all_teams_players[choose_team])):
                if all_teams_players[choose_team][i]['experience'] is True:
                    num_team_exp_plyrs += 1
            print("Number of experienced players:", num_team_exp_plyrs)
            print("Number of inexperienced players:",
                  (len(all_teams_players[choose_team]) - num_team_exp_plyrs))

            total_team_height = 0
            names_team_plyrs = []
            guardians_team_plyrs = []

            for i in range(len(all_teams_players[choose_team])):
                total_team_height += all_teams_players[choose_team][i]['height']
                names_team_plyrs.append(all_teams_players[choose_team][i]['name'])
                guardians_team_plyrs.extend(all_teams_players[choose_team][i]['guardians'])

            avg_team_height = total_team_height / len(all_teams_players[choose_team])
            print("Average team height: %.2f inches" % avg_team_height, end='\n\n')
            print("Players:\n  ", ', '.join(names_team_plyrs), end='\n\n')
            print("Guardians:\n  ", ', '.join(guardians_team_plyrs))
            print("\n-----------------\n")

            restart_option = ('y', 'n')
            restart = choose_team = validate_input(
                "Would you like to try again? (Y/N):   ", restart_option, True)

            if restart.lower() == "y":
                continue
        if start_or_quit == '2':
            restart = 'n'

    else:
        print("\nBye.\n")
print(sys.version)
