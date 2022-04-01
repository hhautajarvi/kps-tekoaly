from random import randint, choice
from collections import deque
from itertools import islice
import pygtrie

class GameService:
    """ Pelilogiikka
    """
    def __init__(self):
        """
        win_lose_tie : Voitetut, hävityt, tasapelit
        choices : edelliset viisi pelaajan valintaa
        trie : trie-rakenne jossa kaikki pelaajan valitsemat ketjut
        number_of_choices : valintojen kokonaismäärä
        """
        self.win_lose_tie = [0, 0, 0]
        self.choices = deque([])
        self.trie = pygtrie.StringTrie()
        self.number_of_choices = 0

    def check_winner(self, choice, cpu_choice):
        """ Tarkistaa kumpi voitti pelin
            Kivi voittaa sakset
            Sakset voittaa paperin
            Paperi voittaa kiven

        Args:_
            choice (str): Pelaajan valinta
            cpu_choice (int): Tietokoneen valinta ( 0 = sakset, 1 = kivi, 2 = paperi)

        Returns:
            str, str: voittaja, tietokoneen valinta
        """

        if cpu_choice == 0:
            if choice == "kivi":
                winner = "Voitit"
            elif choice == "paperi":
                winner = "Hävisit"
            elif choice == "sakset":
                winner = "Tasapeli"
        elif cpu_choice == 1:
            if choice == "kivi":
                winner = "Tasapeli"
            elif choice == "paperi":
                winner = "Voitit"
            elif choice == "sakset":
                winner = "Hävisit"
        elif cpu_choice == 2:
            if choice == "kivi":
                winner = "Hävisit"
            elif choice == "paperi":
                winner = "Tasapeli"
            elif choice == "sakset":
                winner = "Voitit"
        rps_list = ["sakset", "kivi", "paperi"]
        return winner, rps_list[cpu_choice]

    def statistics(self, winner):
        """ Päivittää tilastot ja palauttaa pelin voittotilastot

        Args:
            winner (str): Pelin voittaja

        Returns:
            list: voittotilasto
        """
        if winner == "Voitit":
            self.win_lose_tie[0] += 1
        elif winner == "Hävisit":
            self.win_lose_tie[1] += 1
        else:
            self.win_lose_tie[2] += 1
        return self.win_lose_tie

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
        else:
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
        path = "/".join(list(islice(self.choices, len(self.choices)-chain_length, len(self.choices)+1)))
        if self.trie.has_subtrie(path):
            values = [0, 0, 0]
            if self.trie.has_key(f"{path}/sakset"):
                values[0] = self.trie[f"{path}/sakset"]
            if self.trie.has_key(f"{path}/kivi"):
                values[1] = self.trie[f"{path}/kivi"]
            if self.trie.has_key(f"{path}/paperi"):
                values[2] = self.trie[f"{path}/paperi"]
            if values[0] == values[1] and values[0] == values[2]:
                return randint(0, 2)
            if values[0] == max(values):
                if values[0] > values[1]:
                    if values[0] > values[2]:
                        return 1 # palauttaa kivi koska sakset yleisin valinta
                    return choice([0, 1]) # palauttaa kivi tai sakset koska sakset/paperi yleisin valinta
                if values[0] > values[2]:
                    return choice([1, 2]) # palauttaa paperi tai kivi koska sakset/kivi yleisin valinta
            elif values[1] == max(values):
                if values[1] > values[0]:
                    if values[1] > values[2]:
                        return 2 # palauttaa paperi koska kivi yleisin valinta
                    return choice([0, 2]) # palauttaa paperi tai sakset koska kivi/paperi yleisin valinta
            elif values[2] == max(values):
                return 0  # palauttaa sakset koska paperi yleisin valinta
        else:
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
        self.choices.append(new_choice)
        if len(self.choices) > 5:
            self.choices.popleft()
        for i in range(0, len(self.choices)):
            path = "/".join(list(islice(self.choices, i, len(self.choices)+1)))
            if self.trie.has_key(path):
                self.trie[path] += 1
            else:
                self.trie[path] = 1
        self.number_of_choices += 1

    def check_command_valid(self, command):
        """ Tarkistaa käyttäjän syötteen oikeellisuuden

        Args:
            command (str): Käyttäjän syöte

        Raises:
            Exception: Virhe jos syöte ei oikeaa muotoa
        """
        if command not in ["sakset", "kivi", "paperi"]:
            raise Exception('Anna valintasi muodossa "kivi", "paperi" tai "sakset"')

    def find_best_chain_length(self):
        """ Laskee tilastot viidestä edellisestä pelaajan valinnasta
        1-5 pituisilla Markovin ketjuilla

        Returns:
            int: Ketjun pituus jolla olisi saatu eniten voittoja edellisen viiden
                siirron perusteella
        """
        if self.number_of_choices < 6:
            return 2
        winlist = [0, 0, 0, 0, 0, 0]
        for chain_length in range(1, 5):
            answer = self.calculate(chain_length)
            if answer != 3:
                for human_choice in self.choices:
                    result, _ = self.check_winner(human_choice, answer)
                    if result == "Voitit":
                        winlist[chain_length] += 1
                    if result == "Hävisit":
                        winlist[chain_length] -= 1
        max = 0
        best_chain = 2
        for i in range(1, 5):
            if winlist[i] > max:
                max = winlist[i]
                best_chain = i
        return best_chain
