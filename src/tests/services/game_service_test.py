import imp
import unittest
from services.game_service import GameService

class GameServiceTest(unittest.TestCase):
    def setUp(self):
        self.game_service = GameService()

    def test_constructor(self):
        self.assertEqual([0, 0, 0], self.game_service.win_lose_tie)
        self.assertEqual(0, self.game_service.number_of_choices)

    def test_check_winner_kivi_vs_sakset(self):
        winner, cpu_choice, stats = self.game_service.check_winner("kivi", 0)
        self.assertEqual("Voitit", winner)
        self.assertEqual("sakset", cpu_choice)
        self.assertEqual([1, 0, 0], stats)
    
    def test_check_winner_kivi_vs_kivi(self):
        winner, cpu_choice, stats = self.game_service.check_winner("kivi", 1)
        self.assertEqual("Tasapeli", winner)
        self.assertEqual("kivi", cpu_choice)
        self.assertEqual([0, 0, 1], stats)

    def test_check_winner_kivi_vs_paperi(self):
        winner, cpu_choice, stats = self.game_service.check_winner("kivi", 2)
        self.assertEqual("Hävisit", winner)
        self.assertEqual("paperi", cpu_choice)
        self.assertEqual([0, 1, 0], stats)

    def test_check_winner_sakset_vs_sakset(self):
        winner, cpu_choice, stats = self.game_service.check_winner("sakset", 0)
        self.assertEqual("Tasapeli", winner)
        self.assertEqual("sakset", cpu_choice)
        self.assertEqual([0, 0, 1], stats)
    
    def test_check_winner_sakset_vs_kivi(self):
        winner, cpu_choice, stats = self.game_service.check_winner("sakset", 1)
        self.assertEqual("Hävisit", winner)
        self.assertEqual("kivi", cpu_choice)
        self.assertEqual([0, 1, 0], stats)

    def test_check_winner_sakset_vs_paperi(self):
        winner, cpu_choice, stats = self.game_service.check_winner("sakset", 2)
        self.assertEqual("Voitit", winner)
        self.assertEqual("paperi", cpu_choice)
        self.assertEqual([1, 0, 0], stats)

    def test_check_winner_paperi_vs_sakset(self):
        winner, cpu_choice, stats = self.game_service.check_winner("paperi", 0)
        self.assertEqual("Hävisit", winner)
        self.assertEqual("sakset", cpu_choice)
        self.assertEqual([0, 1, 0], stats)
    
    def test_check_winner_paperi_vs_kivi(self):
        winner, cpu_choice, stats = self.game_service.check_winner("paperi", 1)
        self.assertEqual("Voitit", winner)
        self.assertEqual("kivi", cpu_choice)
        self.assertEqual([1, 0, 0], stats)

    def test_check_winner_paperi_vs_paperi(self):
        winner, cpu_choice, stats = self.game_service.check_winner("paperi", 2)
        self.assertEqual("Tasapeli", winner)
        self.assertEqual("paperi", cpu_choice)
        self.assertEqual([0, 0, 1], stats)

    def test_add_choice(self):
        self.game_service.add_choice("kivi")
        self.assertEqual(len(self.game_service.choices), 1)
        self.assertEqual(self.game_service.trie["kivi"], 1)
        self.assertEqual(self.game_service.number_of_choices, 1)

    def test_add_two_choices(self):
        self.game_service.add_choice("kivi")
        self.game_service.add_choice("kivi")
        self.assertEqual(len(self.game_service.choices), 2)
        self.assertEqual(self.game_service.trie["kivi/kivi"], 1)
        self.assertEqual(self.game_service.trie["kivi"], 2)
        self.assertEqual(self.game_service.number_of_choices, 2)

    def test_add_six_choice(self):
        self.game_service.add_choice("kivi")
        self.game_service.add_choice("kivi")
        self.game_service.add_choice("sakset")
        self.game_service.add_choice("paperi")
        self.game_service.add_choice("kivi")
        self.game_service.add_choice("sakset")
        self.assertEqual(len(self.game_service.choices), 5)
        self.assertEqual(self.game_service.trie["sakset"], 2)
        self.assertEqual(self.game_service.trie["kivi"], 3)
        self.assertEqual(self.game_service.trie["kivi/sakset"], 2)
        self.assertEqual(self.game_service.trie["kivi/kivi/sakset/paperi/kivi"], 1)
        self.assertEqual(self.game_service.trie["kivi/sakset/paperi/kivi/sakset"], 1)
        self.assertEqual(self.game_service.trie["paperi"], 1)
        self.assertEqual(self.game_service.number_of_choices, 6)

    def test_cpu_choice_only_kivi(self):
        self.game_service.add_choice("kivi")
        self.game_service.add_choice("kivi")
        self.game_service.add_choice("kivi")
        self.assertEqual(self.game_service.cpu_choice(), 2) #choose paperi

    def test_cpu_choice_only_paperi(self):
        self.game_service.add_choice("paperi")
        self.game_service.add_choice("paperi")
        self.game_service.add_choice("paperi")
        self.assertEqual(self.game_service.cpu_choice(), 0) #choose sakset

    def test_cpu_choice_only_sakset(self):
        self.game_service.add_choice("sakset")
        self.game_service.add_choice("sakset")
        self.game_service.add_choice("sakset")
        self.assertEqual(self.game_service.cpu_choice(), 1) #choose kivi

    def test_cpu_choice_alternate_sakset_kivi(self):
        self.game_service.add_choice("sakset")
        self.game_service.add_choice("kivi")
        self.game_service.add_choice("sakset")
        self.game_service.add_choice("kivi")
        self.game_service.add_choice("sakset")
        self.game_service.add_choice("kivi")
        self.game_service.add_choice("sakset")
        self.game_service.add_choice("kivi")
        self.assertEqual(self.game_service.cpu_choice(), 1) #choose kivi

    def test_cpu_choice_alternate_sakset_kivi_differently(self):
        self.game_service.add_choice("sakset")
        self.game_service.add_choice("sakset")
        self.game_service.add_choice("sakset")
        self.game_service.add_choice("kivi")
        self.game_service.add_choice("sakset")
        self.game_service.add_choice("kivi")
        self.game_service.add_choice("sakset")
        self.game_service.add_choice("kivi")
        self.game_service.add_choice("sakset")
        self.assertEqual(self.game_service.cpu_choice(), 2) #choose paperi        
        self.game_service.add_choice("sakset")
        self.game_service.add_choice("sakset")
        self.game_service.add_choice("paperi")
        self.game_service.add_choice("sakset")
        self.game_service.add_choice("sakset")
        self.assertEqual(self.game_service.cpu_choice(), 1) #choose kivi