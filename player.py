import uuid

class Player:
    def __init__(self, name = uuid.uuid4().hex):
        self.score = 0
        self.name = name
        self.tally = []
        self.rolling = False

    def reset_score(self):
        self.score = 0    
        self.tally = []
        
    def empty_score_tally(self):
        self.tally = []
    
    def push_to_score_tally(self):
        return self.tally
    
    def add_player_score(self, score_num):
        self.score = self.score + score_num
        
    def get_player_score(self):
        return self.score

    def get_player_name(self):
        return self.name

    def get_player_rolling_state(self):
        return self.rolling

    def set_player_rolling_state(self, boolean):  
        self.rolling = boolean