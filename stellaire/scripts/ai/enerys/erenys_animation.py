class ErenysAnimation:
    def __init__(self):
        self.state = "idle"
    
    def update_animation(self, ai_state):
        if ai_state == "attacking":
            self.play_attack_animation()
        elif ai_state == "defending":
            self.play_defend_animation()
        else:
            self.play_idle_animation()

    def play_attack_animation(self):
        print("Animation : Attaque")

    def play_defend_animation(self):
        print("Animation : Défense")

    def play_idle_animation(self):
        print("Animation : Idle")
