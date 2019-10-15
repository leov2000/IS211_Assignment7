
import logging
from game import Game
from die import Die
from player import Player
from utilities import print_current_score, print_die_roll_message, get_winner, print_game_winner

class Play:
    
    def __init__(self, players_num, games_num):
        self.players = [Player(num) for num in range(1, players_num +1)]
        self.games = [Game(self.players, Die()) for num in range(0, games_num)]
        self.CLI = True 
        self.game_num = 0

    def start(self):
        while self.CLI:
            game_turns = len(self.games)
            current_game = self.games[self.game_num]
            game_players = current_game.get_players()

            while(current_game.check_highest_score() < 100):

                for player in game_players:
                    player.set_player_rolling_state(True)

                    while player.get_player_rolling_state() and current_game.check_highest_score() < 100:

                        player_input = input(f'Player {player.get_player_name()} would you like to ("r") roll or ("h") hold?\n')
                        
                        if player_input.lower() == 'h':
                            current_game.hold(player)
                            score_list = current_game.get_score_list()
                            print_current_score(score_list, self.game_num+1, player)

                        elif player_input.lower() == 'r':
                            num_rolled = current_game.roll_die(player)
                            score_list = current_game.get_score_list()
                            print_die_roll_message(num_rolled, player.get_player_name())
                            print_current_score(score_list, self.game_num+1, player)

                        else:
                            print_unintended_keystroke()
                            logging.error(f'unintended_keystroke for Player: {player.get_player_name()} typed in: {player_input}')
                        
            if current_game.check_highest_score() >= 100:
                high_scorer = get_winner(current_game.get_score_list())
                print_game_winner(high_scorer, self.game_num+1)
                self.game_num  = self.game_num  + 1
                current_game.reset_game()

            if self.game_num == game_turns:
                self.CLI = False
