from random import randint
from collections import deque
from itertools import islice
import pygtrie

class GameService:
    """ Pelilogiikka
    """
    def __init__(self):
        self.win_lose_tie = [0, 0, 0]
        self.choices = deque([])
        self.trie = pygtrie.StringTrie()

    def check_winner(self, choice):
        """ Tarkistaa kumpi voitti pelin

        Args:_
            choice (str): Pelaajan valinta

        Returns:
            _type_: voittaja, tietokoneen valinta ja voittotilasto
        """
        cpu_choice = self.cpu_choice()
        if cpu_choice == 0:
            if choice == "kivi":
                self.win_lose_tie[0] += 1
                winner = "Voitit"
            elif choice == "paperi":
                self.win_lose_tie[1] += 1
                winner = "Hävisit"
            elif choice == "sakset":
                self.win_lose_tie[2] += 1
                winner = "Tasapeli"
        elif cpu_choice == 1:
            if choice == "kivi":
                self.win_lose_tie[2] += 1
                winner = "Tasapeli"
            elif choice == "paperi":
                self.win_lose_tie[0] += 1
                winner = "Voitit"
            elif choice == "sakset":
                self.win_lose_tie[1] += 1
                winner = "Hävisit"
        elif cpu_choice == 2:
            if choice == "kivi":
                self.win_lose_tie[1] += 1
                winner = "Hävisit"
            elif choice == "paperi":
                self.win_lose_tie[2] += 1
                winner = "Tasapeli"
            elif choice == "sakset":
                self.win_lose_tie[0] += 1
                winner = "Voitit"
        return winner, cpu_choice, self.win_lose_tie

    def cpu_choice(self):
        """ Tekee tietokoneen valinnan 
        (tällä hetkellä random)

        Returns:
            _type_: Tietokoneen valinta
        """
        return randint(0, 2)

    def add_choice(self, choice):
        """ Lisää valinnan trie-tietorakenteeseen

        Args:
            choice (str): pelaajan valinta
        """
        self.choices.appendleft(choice)
        if len(self.choices) > 5:
            self.choices.pop()
        for i in range(1, len(self.choices)):
            path = "/".join(list(islice(self.choices, 0, i)))
            if self.trie.has_key(path):
                self.trie[path] += 1
            else:
                self.trie[path] = 1
