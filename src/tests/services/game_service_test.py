import unittest
from services.game_service import GameService

class GameServiceTest(unittest.TestCase):
    def setUp(self):
        self.game_service = GameService()

    def test_constructor(self):
        self.assertEqual([0, 0, 0], self.game_service._win_lose_tie)
        self.assertEqual(1, self.game_service._game_mode)

    def test_statistics_winner(self):
        stats = self.game_service.statistics("Voitit")
        self.assertEqual(([1, 0, 0], 1), stats)

    def test_statistics_loser(self):
        stats = self.game_service.statistics("Hävisit")
        self.assertEqual(([0, 1, 0], 1), stats)

    def test_statistics_draw(self):
        stats = self.game_service.statistics("Tasapeli")
        self.assertEqual(([0, 0, 1], 1), stats)

    def test_statistics_several_rounds(self):
        stats = self.game_service.statistics("Hävisit")
        stats = self.game_service.statistics("Hävisit")
        self.assertEqual(([0, 2, 0], 2), stats)
        stats = self.game_service.statistics("Voitit")
        stats = self.game_service.statistics("Voitit")
        self.assertEqual(([2, 2, 0], 4), stats)
        stats = self.game_service.statistics("Tasapeli")
        stats = self.game_service.statistics("Tasapeli")
        self.assertEqual(([2, 2, 2], 6), stats)

    def test_translate_command_kivi(self):
        self.assertEqual(self.game_service.translate_command(1), "kivi")

    def test_translate_command_sakset(self):
        self.assertEqual(self.game_service.translate_command(0), "sakset")

    def test_translate_command_paperi(self):
        self.assertEqual(self.game_service.translate_command(2), "paperi")

    def test_check_command_valid_not_valid(self):
        with self.assertRaises(Exception):
            self.game_service.check_command_valid("komento")

    def test_check_command_valid_sakset(self):
        self.assertEqual(self.game_service.check_command_valid("sakset"), 0)
        self.assertEqual(self.game_service.check_command_valid("s"), 0)

    def test_check_command_valid_kivi(self):
        self.assertEqual(self.game_service.check_command_valid("kivi"), 1)
        self.assertEqual(self.game_service.check_command_valid("k"), 1)
            
    def test_check_command_valid_paperi(self):
        self.assertEqual(self.game_service.check_command_valid("paperi"), 2)
        self.assertEqual(self.game_service.check_command_valid("p"), 2)

    def test_check_command_valid_not_valid_mode2(self):
        self.game_service.change_game_mode("2")
        with self.assertRaises(Exception):
            self.game_service.check_command_valid("spoock")

    def test_check_command_valid_sakset_mode2(self):
        self.game_service.change_game_mode("2")
        self.assertEqual(self.game_service.check_command_valid("sakset"), 0)
        self.assertEqual(self.game_service.check_command_valid("s"), 0)

    def test_check_command_valid_kivi_mode2(self):
        self.game_service.change_game_mode("2")
        self.assertEqual(self.game_service.check_command_valid("kivi"), 1)
        self.assertEqual(self.game_service.check_command_valid("k"), 1)
            
    def test_check_command_valid_paperi_mode2(self):
        self.game_service.change_game_mode("2")
        self.assertEqual(self.game_service.check_command_valid("paperi"), 2)
        self.assertEqual(self.game_service.check_command_valid("p"), 2)

    def test_check_command_valid_spock_mode2(self):
        self.game_service.change_game_mode("2")
        self.assertEqual(self.game_service.check_command_valid("spock"), 3)
        self.assertEqual(self.game_service.check_command_valid("c"), 3)

    def test_check_command_valid_lisko_mode2(self):
        self.game_service.change_game_mode("2")
        self.assertEqual(self.game_service.check_command_valid("lisko"), 4)
        self.assertEqual(self.game_service.check_command_valid("l"), 4)

    def test_change_game_mode(self):
        self.game_service.change_game_mode("2")
        self.assertEqual(2, self.game_service._game_mode)

    def test_change_game_mode_not_valid(self):
        with self.assertRaises(Exception):
            self.game_service.change_game_mode(3)
