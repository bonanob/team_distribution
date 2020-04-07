import sys
import constants as cons
import random


def validate_input(prompt, err_msg, options, loop=False):
    if loop is True:
        while True:
            try:
                val = input(prompt)
                if val.lower() not in (options):
                    raise ValueError
            except ValueError:
                print(err_msg)
                continue
            else:
                return val
    else:
        try:
            val = input(prompt)
            if val.lower() not in options:
                raise ValueError
        except ValueError:
            print(err_msg)
        else:
            return val


def data_clean_up(players):
    for i in range(len(players)):
        players[i]['height'] = int(players[i]['height'].strip(' inches'))
        players[i]['guardians'] = players[i]['guardians'].split(' and ')
        if players[i]['experience'] == 'YES':
            players[i]['experience'] = True
        else:
            players[i]['experience'] = False
    return players


def divide_exp_inexp(players):
    exp = []
    inexp = []
    for i in range(len(players)):
        if players[i]['experience'] == 'YES':
            exp.append(all_players[i])
        else:
            inexp.append(all_players[i])
    return exp, inexp


def distribute_players(exp, inexp, whole_roaster):
    for i in range(len(exp)):
        whole_roaster[i % len(cons.TEAMS)].append(exp[i])

    # Negative values for uneven number of players for teams
    for i in range(len(inexp)):
        whole_roaster[-(i % len(cons.TEAMS))].append(inexp[i])
    return whole_roaster



if __name__ == '__main__':
    all_players = cons.PLAYERS
    all_teams_players = [[] for i in range(len(cons.TEAMS))]
    exp_players = []
    inexp_players = []

    all_players = data_clean_up(all_players)
    exp_players, inexp_players = divide_exp_inexp(all_players)

    # For different results each time
    random.shuffle(exp_players)
    random.shuffle(inexp_players)

    all_teams_players = distribute_players(exp_players, inexp_players, all_teams_players)

    print("\n************************************")
    print("            TEAM DIVIDER            ")
    print("************************************\n\n")

    restart = 'y'
    while restart.lower() == 'y':
        # Choose to start or quit
        print("----------------------------------\n")
        print("   1. Display Team Stats")
        print("   2. Quit\n")
        start_or_quit_options = ('1', '2')
        start_or_quit = str(validate_input("Enter an option:  ", "Please enter 1 or 2.\n\n", start_or_quit_options))

        if start_or_quit == '1':
            print("")
            # Choose a team to see the stats
            for i, team in enumerate(cons.TEAMS, 1):
                print(f'   {i}. {team}')

            try:
                choose_team_option = [str(i) for i in range(1, (len(all_teams_players)+1)) ]
                print()
                choose_team = validate_input("Enter an option:  ", "Please choose a number from the displayed teams.\n\n", choose_team_option)
                choose_team = int(choose_team) - 1
            except TypeError:
                continue

            # Print Stats
            print("\n-----------------\n")
            print("TEAM:", cons.TEAMS[choose_team], end='\n\n')
            print("Number of players:  ", len(all_teams_players[choose_team]))
            num_team_exp_plyrs = 0
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

            avg_team_height = total_team_height / len(all_teams_players[choose_team])
            print("Average team height: %.2f inches" % avg_team_height, end='\n\n')
            print("Players:\n  ", ', '.join(names_team_plyrs), end='\n\n')

            # Add 'and' in between the names of guardians
            for i in range(len(all_teams_players[choose_team])):
                if len(all_teams_players[choose_team][i]['guardians']) > 1:
                    add_and = [' and '.join(all_teams_players[choose_team][i]['guardians'])]
                    guardians_team_plyrs.extend(add_and)
                else:
                    guardians_team_plyrs.extend(all_teams_players[choose_team][i]['guardians'])
            print("Guardians:\n  ", ', '.join(guardians_team_plyrs))
            print("\n-----------------\n")

            restart_option = ('y', 'n')
            restart = choose_team = validate_input(
                "Would you like to divide the players again? (Y/N):   ", "Please choose Y for yes, N for no.\n\n", restart_option, True)

            if restart.lower() == "y":
                continue
        if start_or_quit == '2':
            restart = 'n'

    else:
        print("\nBye.\n")
print(sys.version)
