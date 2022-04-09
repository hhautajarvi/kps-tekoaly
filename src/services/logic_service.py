from random import randint, choice
from collections import deque
from itertools import islice
from datastructures.trie import Trie

class LogicService:
    """ Pelin logiikasta ja tietorakenteista huolehtiva luokka
    """
    def __init__(self):
        """
        choices : edelliset viisi pelaajan valintaa
        trie : trie-rakenne jossa kaikki pelaajan valitsemat ketjut
        number_of_choices : valintojen kokonaismäärä
        """
        self._choices = deque([])
        self._trie = Trie()
        self._number_of_choices = 0

    def check_winner(self, player_choice, cpu_choice):
        """ Tarkistaa kumpi voitti pelin
            Kivi (1) voittaa sakset (0)
            Sakset (0) voittaa paperin (2)
            Paperi (2) voittaa kiven (1)

        Args:_
            player_choice (str): Pelaajan valinta
            cpu_choice (str): Tietokoneen valinta

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
        if self._number_of_choices < 2:
            return randint(0, 2)
        answer = self._calculate(chain_length)
        if answer == 3:
            return randint(0, 2)
        return answer

    def _calculate(self, chain_length, start=0):
        """  Laskee annetun pituisen Markovin ketjun ja valitsee
        yleisimmän ketjun mukaan siirron jos vastaava edellinen ketju on
        ollut pelaajan siirroissa.

        Args:
            chain_length (int): Annettu Markovin ketjun pituus
            start (int, optional): Aloituskohta kun haetaan voittajaa vanhoista valinnoista
                Defaults to 0

        Returns:
            int: Jos ketju löytyy, palauttaa vastaavan valinnan
                jos ei, palauttaa 3
        """
        try:
            path = "".join(list(islice(self._choices, len(self._choices)-chain_length-start,\
                len(self._choices)+1-start)))
        except:
            return 3
        if self._trie.has_subtrie(path):
            values = [0, 0, 0]
            if self._trie.has_key(f"{path}0"):
                values[0] = self._trie.get_value(f"{path}0")
            if self._trie.has_key(f"{path}1"):
                values[1] = self._trie.get_value(f"{path}1")
            if self._trie.has_key(f"{path}2"):
                values[2] = self._trie.get_value(f"{path}2")
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
        Lisää uusimman valinnan edellisten 10 valinnan listaan
        Lisää myös kokonaisvalintojen lukumäärän

        Args:
            choice (str): pelaajan valinta
        """
        self._choices.append(str(new_choice))
        if len(self._choices) > 10:
            self._choices.popleft()
        max_length = len(self._choices)
        if len(self._choices) > 6:
            max_length = 6
        for i in range(0, max_length):
            path = "".join(list(islice(self._choices, i, max_length+1)))
            if self._trie.has_key(path):
                self._trie.update_value(path)
            else:
                self._trie.add_node(path)
        self._number_of_choices += 1

    def find_best_chain_length(self):
        """ Laskee tilastot viidestä edellisestä pelaajan valinnasta
        1-5 pituisilla Markovin ketjuilla. Jos valintoja 5 tai vähemmän
        annetaan oletuksena 2 pituinen ketju

        Returns:
            int: Ketjun pituus jolla olisi saatu eniten voittoja edellisen viiden
                siirron perusteella (oletuksena kahden pituinen)
        """
        if self._number_of_choices < 6:
            return 2
        winlist = [0, 0, 0, 0, 0, 0]
        for chain_length in range(1, 6):
            for start_point in range(1, 6):
                cpu_choice = self._calculate(chain_length, start_point-1)
                if cpu_choice != 3:
                    result = self.check_winner(int(self._choices[-start_point]), cpu_choice)
                    if result == "Voitit":
                        winlist[chain_length] -= 1
                    if result == "Hävisit":
                        winlist[chain_length] += 1
        max_wins = 0
        best_chain = 2
        for i in range(1, 5):
            if winlist[i] > max_wins:
                max_wins = winlist[i]
                best_chain = i
        return best_chain
