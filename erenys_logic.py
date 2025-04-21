class ErenysAI:
    def __init__(self):
        self.state = "idle"  # Peut-être "idle", "attacking", "defending", etc.
    
    def update(self, player_position, player_health):
        if player_health < 50:
            self.state = "attacking"
        elif player_position and player_position.distance_to(self.get_position()) < 10:
            self.state = "defending"
        else:
            self.state = "idle"
    
    def get_position(self):
        # À remplacer par la vraie position
        pass

    def execute_action(self):
        if self.state == "attacking":
            self.attack()
        elif self.state == "defending":
            self.defend()
        else:
            self.idle()
    
    def attack(self):
        print("Énérys attaque !")
    
    def defend(self):
        print("Énérys se défend.")
    
    def idle(self):
        print("Énérys est au repos.")
