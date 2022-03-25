import imp
import unittest
from services.game_service import GameService

class GameServiceTest(unittest.TestCase):
    def setUp(self):
        self.game_service = GameService()

    def test_constructor(self):
        self.assertEqual([0, 0, 0], self.game_service.win_lose_tie)