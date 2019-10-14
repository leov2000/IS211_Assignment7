class Game:

    def __init__(self, players, die):
        self.players = players
        self.die = None 
        self.turn = None
        self.end = False
        self.die = die 

    def reset_game(self):
        """
        A function delegated to resetting the state of the game.
        
        Parameters: None
        """
        for player in self.players:
            player.reset_score()

        self.die = None 
        self.turn = None

    def get_score_list(self):
        """
        A function used to retrieve the current score of the players playing the game
        
        Parameters: None

        Returns: A list of dictionaries reprresenting the players name and score.
        """
        return [{'player_name': player.get_player_name(), 'player_score': player.get_player_score()} for player in self.players]

    def check_highest_score(self):
        """
        A function that finds the current highest score.

        Parameters: None

        Returns: an integer that represents the highest score.
        """
        score_list = self.get_score_list()
        highest_score = sorted(score_list, key= lambda k: k['player_score'])
        highest_score.reverse()

        return highest_score[0]['player_score']
    
    def hold(self, player):
        """
        A function that tallies up the tally points and changes the player state to `hold`

        Parameters:
            player(<Player>)
        """
        tally_sum = player.sum_tally()
        player.add_to_score(tally_sum)
        player.empty_score_tally()
        player.set_player_rolling_state(False)     
        
    def roll_die(self, player):
        """
        A function that adds to a tally if it isn't a '1' 
        or empties it if it is a '1'.

        Parameters:
            player(<Player>)
        
        Returns: An integer representing the latest rolled num.
        """
        num = self.die.roll_the_die()

        if num == 1:
            player.empty_score_tally()
            player.set_player_rolling_state(False)
        else:
            player.append_score_tally(num)

        return num
    
    def sum_tally(self, player):
        """
        A function that sums a player's tally

        Parameters:
            player(<Player>)

        Returns: An integer representing the sum of the tally
        """

        return player.sum_tally()
    
    def get_players(self):
        """
        A function that retrieves the current games players

        Parameters: None

        Returns: A list of players
        """
        return self.players
        