from random import randint, choice
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
        self.number_of_choices = 0

    def check_winner(self, choice):
        """ Tarkistaa kumpi voitti pelin

        Args:_
            choice (str): Pelaajan valinta

        Returns:
            _type_: voittaja, tietokoneen valinta ja voittotilasto
        """
        cpu_choice = self.cpu_choice() # 0 = sakset, 1 = kivi, 2 = paperi
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
        rps_list = ["sakset", "kivi", "paperi"]
        return winner, rps_list[cpu_choice], self.win_lose_tie

    def cpu_choice(self):
        """ Tekee tietokoneen valinnan 
        Tällä hetkellä vain toisen asteen Markovin ketju joka valitsee
        yleisimmän ketjun mukaan siirron jos vastaava edellinen ketju on
        ollut pelaajan siirroissa.
        Muuten palauttaa arvotun valinnan

        Returns:
            int: Tietokoneen valinta (0 = sakset, 1 = kivi, 2 = paperi)
        """
        if self.number_of_choices < 2:
            return randint(0, 2)
        chain_length = 2
        path = "/".join(list(islice(self.choices, 0, chain_length)))
        if self.trie.has_subtrie(path):
            values = [0, 0, 0]
            if self.trie.has_key(f"{path}/sakset"):
                values[0] = self.trie[f"{path}/sakset"]
            if self.trie.has_key(f"{path}/kivi"):
                values[1] = self.trie[f"{path}/kivi"]
            if self.trie.has_key(f"{path}/paperi"):
                values[2] = self.trie[f"{path}/paperi"]
            if values[0] == max(values):
                if values[0] > values[1]:
                    if values[0] > values[2]:
                        print("cpu: kivi")
                        return 1 # palauttaa kivi koska sakset yleisin valinta
                    else:
                        return choice([0, 1]) # palauttaa kivi tai sakset koska sakset/paperi yleisin valinta
                elif values[0] > values[2]:
                    return choice([1, 2]) # palauttaa paperi tai kivi koska sakset/kivi yleisin valinta
            elif values[1] == max(values):
                if values[1] > values[0]:
                    if values[1] > values[2]:
                        print("cpu: paperi")
                        return 2 # palauttaa paperi koska kivi yleisin valinta
                    else:
                        return choice([0, 2]) # palauttaa paperi tai sakset koska kivi/paperi yleisin valinta
            elif values[2] == max(values):
                print("cpu: sakset")
                return 0  # palauttaa sakset koska paperi yleisin valinta
        else:
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
        self.number_of_choices += 1
