import unittest
from services.game_service import GameService

class GameServiceTest(unittest.TestCase):
    def setUp(self):
        self.game_service = GameService()

    def test_constructor(self):
        self.assertEqual([0, 0, 0], self.game_service.win_lose_tie)
        self.assertEqual(0, self.game_service.number_of_choices)

    def test_check_winner_kivi_vs_sakset(self):
        winner = self.game_service.check_winner(1, 0)
        self.assertEqual("Voitit", winner)
    
    def test_check_winner_kivi_vs_kivi(self):
        winner = self.game_service.check_winner(1, 1)
        self.assertEqual("Tasapeli", winner)

    def test_check_winner_kivi_vs_paperi(self):
        winner = self.game_service.check_winner(1, 2)
        self.assertEqual("Hävisit", winner)

    def test_check_winner_sakset_vs_sakset(self):
        winner = self.game_service.check_winner(0, 0)
        self.assertEqual("Tasapeli", winner)
    
    def test_check_winner_sakset_vs_kivi(self):
        winner = self.game_service.check_winner(0, 1)
        self.assertEqual("Hävisit", winner)

    def test_check_winner_sakset_vs_paperi(self):
        winner = self.game_service.check_winner(0, 2)
        self.assertEqual("Voitit", winner)

    def test_check_winner_paperi_vs_sakset(self):
        winner = self.game_service.check_winner(2, 0)
        self.assertEqual("Hävisit", winner)
    
    def test_check_winner_paperi_vs_kivi(self):
        winner = self.game_service.check_winner(2, 1)
        self.assertEqual("Voitit", winner)

    def test_check_winner_paperi_vs_paperi(self):
        winner = self.game_service.check_winner(2, 2)
        self.assertEqual("Tasapeli", winner)

    def test_statistics_winner(self):
        stats = self.game_service.statistics("Voitit")
        self.assertEqual([1, 0, 0], stats)

    def test_statistics_loser(self):
        stats = self.game_service.statistics("Hävisit")
        self.assertEqual([0, 1, 0], stats)

    def test_statistics_draw(self):
        stats = self.game_service.statistics("Tasapeli")
        self.assertEqual([0, 0, 1], stats)

    def test_add_choice(self):
        self.game_service.add_choice(1)
        self.assertEqual(len(self.game_service.choices), 1)
        self.assertEqual(self.game_service.trie["1"], 1)
        self.assertEqual(self.game_service.number_of_choices, 1)

    def test_add_two_choices(self):
        self.game_service.add_choice(1)
        self.game_service.add_choice(1)
        self.assertEqual(len(self.game_service.choices), 2)
        self.assertEqual(self.game_service.trie["1/1"], 1)
        self.assertEqual(self.game_service.trie["1"], 2)
        self.assertEqual(self.game_service.number_of_choices, 2)

    def test_add_six_choice(self):
        self.game_service.add_choice(1)
        self.game_service.add_choice(1)
        self.game_service.add_choice(0)
        self.game_service.add_choice(2)
        self.game_service.add_choice(1)
        self.game_service.add_choice(0)
        self.assertEqual(len(self.game_service.choices), 5)
        self.assertEqual(self.game_service.trie["0"], 2)
        self.assertEqual(self.game_service.trie["1"], 3)
        self.assertEqual(self.game_service.trie["1/0"], 2)
        self.assertEqual(self.game_service.trie["1/1/0/2/1"], 1)
        self.assertEqual(self.game_service.trie["1/0/2/1/0"], 1)
        self.assertEqual(self.game_service.trie["2"], 1)
        self.assertEqual(self.game_service.number_of_choices, 6)

    def test_cpu_choice_only_kivi_2_len(self):
        self.game_service.add_choice(1)
        self.game_service.add_choice(1)
        self.game_service.add_choice(1)
        self.assertEqual(self.game_service.cpu_choice(2), 2) #choose paperi

    def test_cpu_choice_only_paperi_2_len(self):
        self.game_service.add_choice(2)
        self.game_service.add_choice(2)
        self.game_service.add_choice(2)
        self.assertEqual(self.game_service.cpu_choice(2), 0) #choose sakset

    def test_cpu_choice_only_sakset_2_len(self):
        self.game_service.add_choice(0)
        self.game_service.add_choice(0)
        self.game_service.add_choice(0)
        self.assertEqual(self.game_service.cpu_choice(2), 1) #choose kivi

    def test_cpu_choice_alternate_sakset_kivi_2_len(self):
        self.game_service.add_choice(0)
        self.game_service.add_choice(1)
        self.game_service.add_choice(0)
        self.game_service.add_choice(1)
        self.game_service.add_choice(0)
        self.game_service.add_choice(1)
        self.game_service.add_choice(0)
        self.game_service.add_choice(1)
        self.assertEqual(self.game_service.cpu_choice(2), 1) #choose kivi

    def test_cpu_choice_alternate_sakset_kivi_differently_2_len(self):
        self.game_service.add_choice(0)
        self.game_service.add_choice(0)
        self.game_service.add_choice(0)
        self.game_service.add_choice(1)
        self.game_service.add_choice(0)
        self.game_service.add_choice(1)
        self.game_service.add_choice(0)
        self.game_service.add_choice(1)
        self.game_service.add_choice(0)
        self.assertEqual(self.game_service.cpu_choice(2), 2) #choose paperi        
        self.game_service.add_choice(0)
        self.game_service.add_choice(0)
        self.game_service.add_choice(2)
        self.game_service.add_choice(0)
        self.game_service.add_choice(0)
        self.assertEqual(self.game_service.cpu_choice(2), 1) #choose kivi