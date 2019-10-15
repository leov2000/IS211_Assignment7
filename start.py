
import argparse
import logging
from pprint import pprint
from game import Game
from die import Die
from player import Player
from utilities import safe_int_checker, print_graphics, print_unintended_keystroke, print_current_score, print_die_roll_message, get_winner, print_game_winner

def main():
    """
    The primary function of this application that runs the game.

    Parameters:
        None

    Logs:
        An error if the string url is entered incorrectly.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('--numPlayers', default=2)
    args = parser.parse_args()

    logging.basicConfig(filename='errors_log/errors.log', level=logging.ERROR, format='%(message)s')
    logging.getLogger('assignment7')

    players = args.numPlayers
    (player_is_int, player_num) = safe_int_checker(players)

    print_graphics('artwork/PIG-ART.txt')
    keyed = input('\nHow many games would you like to play?\n')
    (game_is_int, game_num) = safe_int_checker(keyed)

    if game_is_int and player_is_int:

        players = [Player(num) for num in range(1, player_num +1)]
        games = [Game(players, Die()) for num in range(0, game_num)]
        CLI = True
        index = 0

        while CLI:
            game_turns = len(games)
            current_game = games[index]
            game_players = current_game.get_players()

            while(current_game.check_highest_score() < 100):

                for player in game_players:
                    player.set_player_rolling_state(True)

                    while player.get_player_rolling_state() and current_game.check_highest_score() < 100:

                        player_input = input(f'Player {player.get_player_name()} would you like to ("r") roll or ("h") hold?\n')
                        
                        if player_input.lower() == 'h':
                            current_game.hold(player)
                            score_list = current_game.get_score_list()
                            print_current_score(score_list, index+1, player)

                        elif player_input.lower() == 'r':
                            num_rolled = current_game.roll_die(player)
                            score_list = current_game.get_score_list()
                            print_die_roll_message(num_rolled, player.get_player_name())
                            print_current_score(score_list, index+1, player)

                        else:
                            print_unintended_keystroke()
                            logging.error(f'unintended_keystroke for Player: {player.get_player_name()} typed in: {player_input}')
                        
            if current_game.check_highest_score() >= 100:
                high_scorer = get_winner(current_game.get_score_list())
                print_game_winner(high_scorer, index+1)
                index = index + 1
                current_game.reset_game()

            if index == game_turns:
                CLI = False

    else:
        print(f'Something went wrong, you entered in games: "{keyed}" & players: "{players}"')

        logging.error(f'Error processing games key: "{keyed}" & players key: "{players}"')
        return SystemExit
    
    print_graphics('artwork/END.txt')
    print("\nThank you for playing PIG. Please run the script to play again!\n")

if __name__ == '__main__':
    main()
