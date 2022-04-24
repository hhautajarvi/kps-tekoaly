import unittest
from unittest.mock import patch
from random import Random
from services.logic_service import LogicService

class LogicServiceTest(unittest.TestCase):
    def setUp(self):
        self.logic_service = LogicService()
        self.random = Random(666)

    def test_constructor(self):
        self.assertEqual(0, self.logic_service._number_of_choices)
        self.assertEqual(1, self.logic_service._game_mode)

    def test_change_game_mode(self):
        self.logic_service.change_game_mode(2)
        self.assertEqual(2, self.logic_service._game_mode)

    def test_check_winner_kivi_vs_sakset(self):
        winner = self.logic_service.check_winner(1, 0)
        self.assertEqual("Voitit", winner)
    
    def test_check_winner_kivi_vs_kivi(self):
        winner = self.logic_service.check_winner(1, 1)
        self.assertEqual("Tasapeli", winner)

    def test_check_winner_kivi_vs_paperi(self):
        winner = self.logic_service.check_winner(1, 2)
        self.assertEqual("Hävisit", winner)

    def test_check_winner_kivi_vs_spock(self):
        winner = self.logic_service.check_winner(1, 3)
        self.assertEqual("Hävisit", winner)

    def test_check_winner_kivi_vs_lisko(self):
        winner = self.logic_service.check_winner(1, 4)
        self.assertEqual("Voitit", winner)

    def test_check_winner_sakset_vs_sakset(self):
        winner = self.logic_service.check_winner(0, 0)
        self.assertEqual("Tasapeli", winner)
    
    def test_check_winner_sakset_vs_kivi(self):
        winner = self.logic_service.check_winner(0, 1)
        self.assertEqual("Hävisit", winner)

    def test_check_winner_sakset_vs_paperi(self):
        winner = self.logic_service.check_winner(0, 2)
        self.assertEqual("Voitit", winner)

    def test_check_winner_sakset_vs_spock(self):
        winner = self.logic_service.check_winner(0, 3)
        self.assertEqual("Hävisit", winner)

    def test_check_winner_sakset_vs_lisko(self):
        winner = self.logic_service.check_winner(0, 4)
        self.assertEqual("Voitit", winner)

    def test_check_winner_paperi_vs_sakset(self):
        winner = self.logic_service.check_winner(2, 0)
        self.assertEqual("Hävisit", winner)
    
    def test_check_winner_paperi_vs_kivi(self):
        winner = self.logic_service.check_winner(2, 1)
        self.assertEqual("Voitit", winner)

    def test_check_winner_paperi_vs_paperi(self):
        winner = self.logic_service.check_winner(2, 2)
        self.assertEqual("Tasapeli", winner)

    def test_check_winner_paperi_vs_spock(self):
        winner = self.logic_service.check_winner(2, 3)
        self.assertEqual("Voitit", winner)

    def test_check_winner_paperi_vs_lisko(self):
        winner = self.logic_service.check_winner(2, 4)
        self.assertEqual("Hävisit", winner)

    def test_check_winner_spock_vs_sakset(self):
        winner = self.logic_service.check_winner(3, 0)
        self.assertEqual("Voitit", winner)
    
    def test_check_winner_spock_vs_kivi(self):
        winner = self.logic_service.check_winner(3, 1)
        self.assertEqual("Voitit", winner)

    def test_check_winner_spock_vs_paperi(self):
        winner = self.logic_service.check_winner(3, 2)
        self.assertEqual("Hävisit", winner)

    def test_check_winner_spock_vs_spock(self):
        winner = self.logic_service.check_winner(3, 3)
        self.assertEqual("Tasapeli", winner)

    def test_check_winner_spock_vs_lisko(self):
        winner = self.logic_service.check_winner(3, 4)
        self.assertEqual("Hävisit", winner)

    def test_check_winner_lisko_vs_sakset(self):
        winner = self.logic_service.check_winner(4, 0)
        self.assertEqual("Hävisit", winner)
    
    def test_check_winner_lisko_vs_kivi(self):
        winner = self.logic_service.check_winner(4, 1)
        self.assertEqual("Hävisit", winner)

    def test_check_winner_lisko_vs_paperi(self):
        winner = self.logic_service.check_winner(4, 2)
        self.assertEqual("Voitit", winner)

    def test_check_winner_lisko_vs_spock(self):
        winner = self.logic_service.check_winner(4, 3)
        self.assertEqual("Voitit", winner)

    def test_check_winner_lisko_vs_lisko(self):
        winner = self.logic_service.check_winner(4, 4)
        self.assertEqual("Tasapeli", winner)

    def test_add_choice(self):
        self.logic_service.add_choice(1)
        self.assertEqual(len(self.logic_service._choices), 1)
        self.assertEqual(self.logic_service._trie.get_value("1"), 1)
        self.assertEqual(self.logic_service._number_of_choices, 1)

    def test_add_two_choices(self):
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.assertEqual(len(self.logic_service._choices), 2)
        self.assertEqual(self.logic_service._trie.get_value("11"), 1)
        self.assertEqual(self.logic_service._trie.get_value("1"), 2)
        self.assertEqual(self.logic_service._number_of_choices, 2)

    def test_add_six_choice(self):
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.assertEqual(len(self.logic_service._choices), 6)
        self.assertEqual(self.logic_service._trie.get_value("0"), 2)
        self.assertEqual(self.logic_service._trie.get_value("1"), 3)
        self.assertEqual(self.logic_service._trie.get_value("10"), 2)
        self.assertEqual(self.logic_service._trie.get_value("11021"), 1)
        self.assertEqual(self.logic_service._trie.get_value("10210"), 1)
        self.assertEqual(self.logic_service._trie.get_value("2"), 1)
        self.assertEqual(self.logic_service._number_of_choices, 6)

    def test_add_eleven_choice(self):
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(1)
        self.assertEqual(len(self.logic_service._choices), 10)
        self.assertEqual(self.logic_service._number_of_choices, 11)

    def test_cpu_choice_only_kivi_2_len(self):
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.assertEqual(self.logic_service.cpu_choice(2), 2) #choose paperi

    def test_cpu_choice_only_paperi_2_len(self):
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(2)
        self.assertEqual(self.logic_service.cpu_choice(2), 0) #choose sakset

    def test_cpu_choice_only_sakset_2_len(self):
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(0)
        self.assertEqual(self.logic_service.cpu_choice(2), 1) #choose kivi

    def test_cpu_choice_alternate_sakset_kivi_2_len(self):
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(1)
        self.assertEqual(self.logic_service.cpu_choice(2), 1) #choose kivi

    def test_cpu_choice_alternate_sakset_kivi_differently_2_len(self):
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.assertEqual(self.logic_service.cpu_choice(2), 2) #choose paperi        
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(0)
        self.assertEqual(self.logic_service.cpu_choice(2), 1) #choose kivi

    @patch('services.logic_service.randint')
    def test_cpu_choice_random_choice_one_previous(self, randint):
        randint._mock_side_effect = self.random.randint
        self.logic_service.add_choice(0)
        self.assertEqual(self.logic_service.cpu_choice(2), 1) #choose paperi

    @patch('services.logic_service.randint')
    def test_cpu_choice_random_choice_no_precedent_2_len(self, randint):
        randint._mock_side_effect = self.random.randint
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(1)
        self.assertEqual(self.logic_service.cpu_choice(2), 1) #choose paperi

    @patch('services.logic_service.randint')
    def test_cpu_choice_random_choice_one_previous_mode2(self, randint):
        self.logic_service.change_game_mode(2)
        randint._mock_side_effect = self.random.randint
        self.logic_service.add_choice(4)
        self.assertEqual(self.logic_service.cpu_choice(2), 3) #choose spock

    @patch('services.logic_service.randint')
    def test_cpu_choice_random_choice_no_precedent_2_len_mode2(self, randint):
        randint._mock_side_effect = self.random.randint
        self.logic_service.change_game_mode(2)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(3)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(4)
        self.assertEqual(self.logic_service.cpu_choice(2), 3) #choose spock

    def test_calculate_no_precedent_2_len(self):
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(1)
        self.assertEqual(self.logic_service._calculate(2), 5) #false

    def test_calculate_1_len(self):
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(0)
        self.assertEqual(self.logic_service._calculate(1), 0) #sakset

    def test_calculate_4_len(self):
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(0)
        self.assertEqual(self.logic_service._calculate(4), 0) #sakset

    @patch('services.logic_service.randint')
    def test_calculate_random_choice_three_choices_2_len(self, randint):
        randint._mock_side_effect = self.random.randint
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(0)
        self.assertEqual(self.logic_service._calculate(2), 1) #choose kivi

    @patch('services.logic_service.choice')
    def test_calculate_random_choice_two_choices_kp_2_len(self, choice):
        choice._mock_side_effect = self.random.choice
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(0)
        self.assertEqual(self.logic_service._calculate(2), 2) #choose paperi

    @patch('services.logic_service.choice')
    def test_calculate_random_choice_two_choices_sk_2_len(self, choice):
        choice._mock_side_effect = self.random.choice
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(2)
        self.assertEqual(self.logic_service._calculate(2), 2) #choose paperi

    @patch('services.logic_service.choice')
    def test_calculate_random_choice_two_choices_sp_2_len(self, choice):
        choice._mock_side_effect = self.random.choice
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.assertEqual(self.logic_service._calculate(2), 1) #choose paperi

    @patch('services.logic_service.choice')
    def test_calculate_lizard_1_len_mode2(self, choice):
        choice._mock_side_effect = self.random.choice
        self.logic_service.change_game_mode(2)
        self.logic_service.add_choice(3)
        self.logic_service.add_choice(4)
        self.logic_service.add_choice(3)
        self.assertEqual(self.logic_service._calculate(1), 1) #kivi

    @patch('services.logic_service.choice')
    def test_calculate_spock_1_len_mode2(self, choice):
        choice._mock_side_effect = self.random.choice
        self.logic_service.change_game_mode(2)
        self.logic_service.add_choice(4)
        self.logic_service.add_choice(3)
        self.logic_service.add_choice(4)
        self.assertEqual(self.logic_service._calculate(1), 4) #lisko

    @patch('services.logic_service.choice')
    def test_calculate_paper_1_len_mode2(self, choice):
        choice._mock_side_effect = self.random.choice
        self.logic_service.change_game_mode(2)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(1)
        self.assertEqual(self.logic_service._calculate(1), 4) #lisko

    @patch('services.logic_service.choice')
    def test_calculate_rock_1_len_mode2(self, choice):
        choice._mock_side_effect = self.random.choice
        self.logic_service.change_game_mode(2)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.assertEqual(self.logic_service._calculate(1), 3) #spock

    @patch('services.logic_service.choice')
    def test_calculate_scissors_1_len_mode2(self, choice):
        choice._mock_side_effect = self.random.choice
        self.logic_service.change_game_mode(2)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(1)
        self.assertEqual(self.logic_service._calculate(1), 3) #spock

    @patch('services.logic_service.randint')
    def test_calculate_random_choice_5_choices_1_len_mode2(self, randint):
        randint._mock_side_effect = self.random.randint
        self.logic_service.change_game_mode(2)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(3)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(4)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(0)
        self.assertEqual(self.logic_service._calculate(1), 3) #choose spock

    def test_find_best_chain_length_not_enough_choices(self):
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.assertEqual(self.logic_service.find_best_chain_length(), 2)

    def test_find_best_chain_length_one(self):
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.assertEqual(self.logic_service.find_best_chain_length(), 1)
    
    @patch('services.logic_service.choice')
    def test_find_best_chain_length_two(self, choice):
        choice._mock_side_effect = self.random.choice
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(0)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(1)
        self.logic_service.add_choice(2)
        self.logic_service.add_choice(2)
        self.assertEqual(self.logic_service.find_best_chain_length(), 2)
