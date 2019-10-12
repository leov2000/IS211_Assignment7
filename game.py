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

    def check_highest_score(self):
        score_list = [{'player_name': player.name, 'player_score': player.score} for player in self.players]
        highest_score = sorted(score_list, key= lambda k: k['player_score'])

        return highest_score[0]
   
    
    def roll_or_hold(self, player):
        pass 
        
    def next_turn(self, player):
        self.turn = player 
    
    def get_players(self):
        return self.players

    def get_die(self):
        return self.die

