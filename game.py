class Game:

    def __init__(self, players, die):
        self.players = players
        self.die = None 
        self.turn = None
        self.end = False
        self.die = die 


    def reset_game(self):
        for player in self.players:
            player.reset_score()

        self.die = None 
        self.turn = None

    def get_score_list(self):
        return [{'player_name': player.name, 'player_score': player.score} for player in self.players]

    def check_highest_score(self):
        score_list = self.get_score_list()
        highest_score = sorted(score_list, key= lambda k: k['player_score'])
        highest_score.reverse()

        return highest_score[0]['player_score']

    def current_score(self):
        score_list = self.get_score_list()
        sorted_score = sorted(score_list, key= lambda k: k['player_name'])

        return sorted_score
    
    def hold(self, player):
        tally_sum = player.sum_tally()
        player.add_to_score(tally_sum)
        player.empty_score_tally()
        player.set_player_rolling_state(False)     
        
    def roll_die(self, player):
        num = self.die.roll_the_die()

        if num == 1:
            player.empty_score_tally()
            player.set_player_rolling_state(False)
        else:
            player.append_score_tally(num)

        return num 
    
    def get_players(self):
        return self.players

    def get_die(self):
        return self.die

