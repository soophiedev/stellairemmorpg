import unittest
from ai.erenys_logic import ErenysAI
from ai.erenys_config import ErenysConfig

class DummyPosition:
    def __init__(self, x):
        self.x = x
    def distance_to(self, other):
        return abs(self.x - other.x)

class DummyErenys(ErenysAI):
    def get_position(self):
        return DummyPosition(0)

class TestErenysAI(unittest.TestCase):
    def test_idle_state(self):
        ai = DummyErenys()
        ai.update(player_position=DummyPosition(100), player_health=100)
        self.assertEqual(ai.state, "idle")
    
    def test_attack_state(self):
        ai = DummyErenys()
        ai.update(player_position=DummyPosition(100), player_health=30)
        self.assertEqual(ai.state, "attacking")
    
    def test_defend_state(self):
        ai = DummyErenys()
        ai.update(player_position=DummyPosition(5), player_health=90)
        self.assertEqual(ai.state, "defending")

if __name__ == "__main__":
    unittest.main()
