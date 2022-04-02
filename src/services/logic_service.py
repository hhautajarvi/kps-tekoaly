from random import randint, choice
from collections import deque
from itertools import islice
import pygtrie

class LogicService:
    """ Pelin logiikasta ja tietorakenteista huolehtiva luokka
    """
    def __init__(self):
        """
        choices : edelliset viisi pelaajan valintaa
        trie : trie-rakenne jossa kaikki pelaajan valitsemat ketjut
        number_of_choices : valintojen kokonaismäärä
        """
        self.choices = deque([])
        self.trie = pygtrie.StringTrie()
        self.number_of_choices = 0

    def check_winner(self, player_choice, cpu_choice):
        """ Tarkistaa kumpi voitti pelin
            Kivi voittaa sakset
            Sakset voittaa paperin
            Paperi voittaa kiven

        Args:_
            choice (str): Pelaajan valinta

        Returns:
            str: pelin tulos
        """

        if cpu_choice == 0:
            if player_choice == 1:
                winner = "Voitit"
            elif player_choice == 2:
                winner = "Hävisit"
            else:
                winner = "Tasapeli"
        elif cpu_choice == 1:
            if player_choice == 1:
                winner = "Tasapeli"
            elif player_choice == 2:
                winner = "Voitit"
            else:
                winner = "Hävisit"
        elif cpu_choice == 2:
            if player_choice == 1:
                winner = "Hävisit"
            elif player_choice == 2:
                winner = "Tasapeli"
            else:
                winner = "Voitit"
        return winner

    def cpu_choice(self, chain_length):
        """ Tekee tietokoneen valinnan käyttäen calculate-metodia
        Jos saa sieltä False-vastauksen tai valintoja tehty
        vasta alle 2, palauttaa arvotun valinnan

        Returns:
            int: Tietokoneen valinta (0 = sakset, 1 = kivi, 2 = paperi)
        """
        if self.number_of_choices < 2:
            return randint(0, 2)
        answer = self.calculate(chain_length)
        if answer == 3:
            return randint(0, 2)
        return answer

    def calculate(self, chain_length):
        """  Laskee annetun pituisen Markovin ketjun ja valitsee
        yleisimmän ketjun mukaan siirron jos vastaava edellinen ketju on
        ollut pelaajan siirroissa.

        Args:
            chain_length (int): Annettu Markovin ketjun pituus

        Returns:
            int: Jos ketju löytyy, palauttaa vastaavan valinnan
                jos ei, palauttaa 3
        """
        path = "/".join(list(islice(self.choices, len(self.choices)-chain_length,\
            len(self.choices)+1)))
        if self.trie.has_subtrie(path):
            values = [0, 0, 0]
            if self.trie.has_key(f"{path}/0"):
                values[0] = self.trie[f"{path}/0"]
            if self.trie.has_key(f"{path}/1"):
                values[1] = self.trie[f"{path}/1"]
            if self.trie.has_key(f"{path}/2"):
                values[2] = self.trie[f"{path}/2"]
            if values[0] == values[1] and values[0] == values[2]:
                return randint(0, 2)
            if values[0] == max(values):
                if values[0] > values[1]:
                    if values[0] > values[2]:
                        return 1
                        # palauttaa kivi koska sakset yleisin valinta
                    return choice([0, 1])
                    # palauttaa kivi tai sakset koska sakset/paperi yleisin valinta
                if values[0] > values[2]:
                    return choice([1, 2])
                    # palauttaa paperi tai kivi koska sakset/kivi yleisin valinta
            if values[1] == max(values):
                if values[1] > values[0]:
                    if values[1] > values[2]:
                        return 2
                        # palauttaa paperi koska kivi yleisin valinta
                    return choice([0, 2])
                    # palauttaa paperi tai sakset koska kivi/paperi yleisin valinta
            if values[2] == max(values):
                return 0
                # palauttaa sakset koska paperi yleisin valinta
        return 3

    def add_choice(self, new_choice):
        """ Lisää valinnan trie-tietorakenteeseen
        Lisää tietorakenteeseen maksimissaan viiden valinnan ketjuja.
        Lisää samalla myös edelliset neljän, kolmen, kahden ja yhden ketjut
        Lisää uusimman valinnan edellisten 5 valinnan listaan
        Lisää myös kokonaisvalintojen lukumäärän

        Args:
            choice (str): pelaajan valinta
        """
        self.choices.append(str(new_choice))
        if len(self.choices) > 5:
            self.choices.popleft()
        for i in range(0, len(self.choices)):
            path = "/".join(list(islice(self.choices, i, len(self.choices)+1)))
            if self.trie.has_key(path):
                self.trie[path] += 1
            else:
                self.trie[path] = 1
        self.number_of_choices += 1

    def find_best_chain_length(self):
        """ Laskee tilastot viidestä edellisestä pelaajan valinnasta
        1-5 pituisilla Markovin ketjuilla

        Returns:
            int: Ketjun pituus jolla olisi saatu eniten voittoja edellisen viiden
                siirron perusteella (oletuksena kahden pituinen)
        """
        if self.number_of_choices < 6:
            return 2
        winlist = [0, 0, 0, 0, 0, 0]
        for chain_length in range(1, 5):
            answer = self.calculate(chain_length)
            if answer != 3:
                for human_choice in self.choices:
                    result = self.check_winner(human_choice, answer)
                    if result == "Voitit":
                        winlist[chain_length] += 1
                    if result == "Hävisit":
                        winlist[chain_length] -= 1
        max_wins = 0
        best_chain = 2
        for i in range(1, 5):
            if winlist[i] > max_wins:
                max_wins = winlist[i]
                best_chain = i
        return best_chain
