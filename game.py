class Game:

    def __init__(self, players, die):
        self.players = players
        self.die = None 
        self.turn = None
        self.end = False
        self.die = die 

    def check_score(self, players):
        for player in self.players:
            if player.get_player_score() >= 100:
                print("you won")
                self.reset_game()


    def reset_game(self):
        for player in self.players:
            player.reset_score()

        self.die = None 
        self.turn = None
    
    def roll_or_hold(self, player):
        pass 
        
    def next_turn(self, player):
        self.turn = player 

