
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

def print_graphics(file_name):
    """
    A print utility function that prints out the PIG and END logo

    Parameters:
        file_name(<text_file>): A text file
    """
    
    text_header = "$" * 51

    ascii_file = open(file_name, 'r')
    ascii_text = ascii_file.read()

    print(text_header)
    print(ascii_text)
    print(text_header)

def print_unintended_keystroke():
    """
    A print utility function that prints out an error message 

    Parameters:None
    """

    print("Hmm.. not sure what that was, please click on 'r' or 'h' ")

def print_current_score(score_list, game_num, current_player = None):
    """
    A print utility function that prints out the curent score

    Parameters:
        score_list(list[dict[str, int]])
        game_num(int)
        current_player(<Player>)
    """

    (player_name, player_tally) = (current_player.get_player_name(), current_player.sum_tally())
    text_header = '$' * 17 
    text_footer = '$' * 51

    print(f'{text_header}[-GAME-{game_num}-SCORE-]{text_header}')
    print('\n')

    for player_score_details in score_list:
        append_string = f'TALLY: {player_tally}' if player_score_details['player_name'] == player_name and current_player.get_player_rolling_state() else ''
        print(f'PLAYER {player_score_details["player_name"]} SCORE: {player_score_details["player_score"]} {append_string}')
        print('\n')

    print(text_footer)

def print_die_roll_message(num, player_name):
    """
    A print utility function that prints out the player's current roll

    Parameters:
        num(int)
        player_name(str)
    """

    print(f'Player {player_name} rolled a {num}! Adding it to the tally...\n')

def get_winner(player_list):
    """
    A utility function that retrieves the winner of the game when the game ends.
    
    Parameters:
        player_list(list[dict[str, int]])
    """

    highest_score = sorted(player_list, key= lambda k: k['player_score'])
    highest_score.reverse()
    
    return highest_score[0]

def print_game_winner(score_dict, game_num):
    """
    A utility function that prints the game winner

    Parameters:
        score_dict(dict[str,int])
        game_num(int)
    """

    name = score_dict.get('player_name')
    score = score_dict.get('player_score')

    print(f'\nPlayer {name} won GAME:{game_num} with a SCORE OF: {score}\n')

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

    logging.basicConfig(filename='errors_log/errors.log', level=logging.ERROR, format='%(message)s')
    logging.getLogger('assignment7')

    players = args.numPlayer
    (player_is_int, player_num) = safe_int_checker(players)

    print_graphics('artwork/PIG-ART.txt')
    keyed = input('\nHow many games do you want to play?\n')
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
