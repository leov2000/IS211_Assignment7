from random import randint

class Die:
    def __init__(self): 
        self.face = 0
        self.roll_count = 0

    def reset_die_face(self):
        self.face = 0
    
    def reset_roll_count(self):
        self.roll_count = 0
    
    def roll_the_die(self):
        random_num = randint(1,6)
        
        self.face = random_num
        self.roll_count = self.roll_count + 1