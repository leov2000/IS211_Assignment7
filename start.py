
import argparse
import logging
from pprint import pprint
from game import Game
from die import Die
from player import Player


def safe_int_checker(int_str):
    """
    A function that checks if the string is actually an int. used for the CLI.

    Parameters:
        int_str(str): A string representing an int.

    Returns:
        A tuple with a boolean as the first item and a value if its successfuly cast or None if it isnt.
    """

    try:
        num = int(int_str)
        return (True, num)
    except ValueError:
        return (False, None)

def print_game_text(players):
    player_confirmation_text = f"You've chosen {players} Players to play PIG"
    dollar_text = "$" * 51

    ascii_file = open('PIG-ART.txt', 'r')
    ascii_text = ascii_file.read()

    print(dollar_text)
    print(ascii_text)
    print(dollar_text)
    print(player_confirmation_text)
    
def main():
    """
    The primary function of this application.

    Parameters:
        None

    Logs:
        An error if the string url is entered incorrectly.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('--numPlayer', default=2)
    args = parser.parse_args()
    players = args.numPlayer
    print_game_text(players)

    logging.basicConfig(filename='errors.log',
                        level=logging.ERROR, format='%(message)s')
    logging.getLogger('assignment7')

    keyed = input(
        '\nHow many games do you want to play?\n')
    (is_int, game_num) = safe_int_checker(keyed)

    if is_int and game_num:
        players = [Player(player_num) for player_num in range(1, players +1)]
        games = [Game(players, Die()) for num in range(0, game_num)]

        while len(games):
            current_game = games[0]
            game_players = current_game.get_players()
            # current_die = current_game.get_die()

            while(current_game.check_highest_score()['player_score'] < 100):

                for player in game_players:
                    player.set_player_rolling_state(True)

                    while player.get_player_rolling_state():
                        player_input = input(f'Player {player.get_player_name()} would you like to ("r") roll or ("h") hold?')
                        
                        if player_input.lower() == 'h':
                            player.set_player_rolling_state(False)
                        elif player_input.lower() == 'r':
                            print("rolling rolling rolling")
                        else:
                            print("Hmm.. not sure what that was, please click on 'r' or 'h' ")



    else:
        print(
            f'Something went wrong, you entered in "{keyed}"')

        logging.error(f'Error processing "{keyed}"')
        return SystemExit
    print("Thank you for playing PIG. Please run the script to play again!")

if __name__ == '__main__':
    main()
