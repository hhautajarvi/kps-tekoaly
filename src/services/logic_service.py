from random import randint, choice
from collections import deque
from itertools import islice
from datastructures.trie import Trie

class LogicService:
    """ Pelin logiikasta ja tietorakenteista huolehtiva luokka
    """
    def __init__(self):
        """
        choices : edelliset kymmenen pelaajan valintaa
        trie : trie-rakenne jossa kaikki pelaajan valitsemat ketjut
        number_of_choices : valintojen kokonaismäärä
        game_mode : normaali kps (default) tai spock-lisko (2)
        """
        self._choices = deque([])
        self._trie = Trie()
        self._number_of_choices = 0
        self._game_mode = 1

    def change_game_mode(self, game_mode):
        """ Vaihtaa pelimoodia normaalin ja
        spocl-lisko-variantin välillä

        Args:
            game_mode (int): 1: normi, 2: sl-variantti
        """
        self._game_mode = game_mode

    def check_winner(self, player_choice, cpu_choice):
        """ Tarkistaa kumpi voitti pelin
            Sakset (0) voittaa paperin (2)
            Sakset (0) voittaa liskon (4)
            Kivi (1) voittaa sakset (0)
            Kivi (1) voittaa liskon (4)
            Paperi (2) voittaa kiven (1)
            Paperi (2) voittaa spockin (3)
            Spock (3) voittaa sakset (0)
            Spock (3) voittaa kiven (1)
            Lisko (4) voittaa spockin (3)
            Lisko (4) voittaa paperin (2)

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
            elif player_choice == 3:
                winner = "Voitit"
            elif player_choice == 4:
                winner = "Hävisit"
            else:
                winner = "Tasapeli"
        elif cpu_choice == 1:
            if player_choice == 1:
                winner = "Tasapeli"
            elif player_choice == 2:
                winner = "Voitit"
            elif player_choice == 3:
                winner = "Voitit"
            elif player_choice == 4:
                winner = "Hävisit"
            else:
                winner = "Hävisit"
        elif cpu_choice == 2:
            if player_choice == 1:
                winner = "Hävisit"
            elif player_choice == 2:
                winner = "Tasapeli"
            elif player_choice == 3:
                winner = "Hävisit"
            elif player_choice == 4:
                winner = "Voitit"
            else:
                winner = "Voitit"
        elif cpu_choice == 3:
            if player_choice == 1:
                winner = "Hävisit"
            elif player_choice == 2:
                winner = "Voitit"
            elif player_choice == 3:
                winner = "Tasapeli"
            elif player_choice == 4:
                winner = "Voitit"
            else:
                winner = "Hävisit"
        elif cpu_choice == 4:
            if player_choice == 1:
                winner = "Voitit"
            elif player_choice == 2:
                winner = "Hävisit"
            elif player_choice == 3:
                winner = "Hävisit"
            elif player_choice == 4:
                winner = "Tasapeli"
            else:
                winner = "Voitit"
        return winner

    def cpu_choice(self, chain_length):
        """ Tekee tietokoneen valinnan käyttäen calculate-metodia
        Jos saa sieltä 5(false)-vastauksen tai valintoja tehty
        vasta alle 2, palauttaa arvotun valinnan

        Returns:
            int: Tietokoneen valinta (0 = sakset, 1 = kivi, 2 = paperi, 3 = spock, 4 = lisko)
        """
        if self._number_of_choices < 2:
            if self._game_mode == 1:
                return randint(0, 2)
            return randint(0, 4)
        answer = self._calculate(chain_length)
        if answer == 5:
            if self._game_mode == 1:
                return randint(0, 2)
            return randint(0, 4)
        return answer

    def _calculate(self, chain_length, start=0):
        """  Laskee annetun pituisen Markovin ketjun ja sitä vastaavat
            pelaajan eri valintojen määrät triehen tallennetuista siirroista.
            Pyytää check_max_values-metodilta suurimpia valintoja vastaavat tietokoneen valinnat.

        Args:
            chain_length (int): Annettu Markovin ketjun pituus
            start (int, optional): Aloituskohta kun haetaan voittajaa vanhoista valinnoista
                Defaults to 0

        Returns:
            int: Jos ketju löytyy, palauttaa vastaavan valinnan
                jos ei, palauttaa 5
        """
        #tarkistetaan onko ketju olemassa valintalistassa
        try:
            path = "".join(list(islice(self._choices, len(self._choices)-chain_length-start,\
                len(self._choices)+1-start)))
        except:
            return 5
        #tarkistetaan löytyykö polun päästä valintoja
        if self._trie.has_subtrie(path):
            values = [0, 0, 0, 0, 0]
            #lisätään löytyvien valintojen määrä listaan
            if self._trie.has_key(f"{path}0"):
                values[0] = self._trie.get_value(f"{path}0")
            if self._trie.has_key(f"{path}1"):
                values[1] = self._trie.get_value(f"{path}1")
            if self._trie.has_key(f"{path}2"):
                values[2] = self._trie.get_value(f"{path}2")
            # jos pelataan lisko/spock:
            if self._game_mode == 2:
                if self._trie.has_key(f"{path}3"):
                    values[3] = self._trie.get_value(f"{path}3")
                if self._trie.has_key(f"{path}4"):
                    values[4] = self._trie.get_value(f"{path}4")
                # haetaan valinta variantin versiolla
                return self._check_max_values_variant(values)
            # haetaan valinta normi-kps:n versiolla
            return self._check_max_values_normal(values)
        return 5

    def _check_max_values_normal(self, values):
        """ Tarkistetaan mitä valintoja on eniten ja palautetaan
            sitä parhaiten vastaava valinta tai arvotaan sellainen
            jos monta vaihtoehtoa.
            Normaalin kps:n versio

        Args:
            values (list): lista ihmisen valintojen määristä

        Returns:
            int: tietokoneen vastaava valinta
        """
        if values[0] == values[1] and values[0] == values[2]:
            return randint(0, 2)
        if values[0] == max(values):
            if values[0] > values[1]:
                if values[0] > values[2]: # sakset yleisin valinta
                    return 1 # palauttaa kivi
                # sakset/paperi yleisin valinta
                return choice([0, 1]) # palauttaa kivi tai sakset
            # sakset/kivi yleisin valinta
            return choice([1, 2]) # palauttaa paperi tai kivi
        if values[1] == max(values):
            if values[1] > values[2]: # kivi yleisin valinta
                return 2 # palauttaa paperi
            # kivi/paperi yleisin valinta
            return choice([0, 2]) # palauttaa paperi tai sakset
        # paperi yleisin valinta
        return 0 # palauttaa sakset

    def _check_max_values_variant(self, values):
        """ Tarkistetaan mitä valintoja on eniten ja palautetaan
            sitä parhaiten vastaava valinta tai arvotaan sellainen
            jos monta vaihtoehtoa.
            Spock-lisko-variantin versio

        Args:
            values (list): lista ihmisen valintojen määristä

        Returns:
            int: tietokoneen vastaava valinta
        """
        if all(value == values[0] for value in values):
            return randint(0, 4) # kaikkia saman verran
        if values[0] == max(values):
            if values[0] > values[1]:
                if values[0] > values[2]:
                    if values[0] > values[3]:
                        if values[0] > values[4]: # sakset yleisin valinta
                            return choice([1, 3]) # palauttaa kivi/spock
                        # sakset/lisko yleisin valinta
                        return 1 # palauttaa kivi (voittaa molemmat)
                    if values[0] > values[4]: # sakset/spock yleisin
                        return 3 # palauttaa spock (voitto + tasapeli)
                    # sakset/spock/lisko yleisin
                    return 1 # palauttaa kivi (voittaa ainoana 2)
                if values[0] > values[3]:
                    if values[0] > values[4]: # sakset/paperi yleisin valinta
                        return 0 # palauttaa sakset (voitto + tasapeli)
                    # yleisin valinta sakset/paperi/lisko
                    return 0 # palauttaa sakset (voittaa 2 + tasapeli)
                if values[0] > values[4]: # yleisin valinta sakset/paperi/spock
                    return 4 # palauttaa lisko (voittaa sekä paperi/spock)
                # sakset/paperi/spock/lisko yleisin
                return choice([0, 4]) #palauttaa sakset/lisko (voittaa 2 + tasapeli)
            if values[0] > values[2]:
                if values[0] > values[3]:
                    if values[0] > values[4]: # sakset/kivi yleisin valinta
                        return 3 # palauttaa spock (voittaa molemmat)
                    # sakset/kivi/lisko yleisin valinta
                    return 1 # palauttaa kivi (voittaa 2 + tasapeli)
                if values[0] > values[4]: # sakset/kivi/spock yleisin
                    return 3  # palauttaa spock (voittaa 2 + tasapeli)
                # sakset/kivi/spock/lisko yleisin
                return choice([1, 3]) # palauttaa kivi/spock (voittaa 2 + tasapeli)
            if values[0] > values[3]:
                if values[0] > values[4]: # sakset/kivi/paperi yleisin
                    return 3 # palauttaa spock (voittaa sakset/kivi)
                # sakset/kivi/paperi/lisko yleisin
                return choice([0, 1]) # palauttaa sakset/kivi (voittaa 2 + tasapeli)
            # sakset/kivi/paperi/spock yleisin
            return choice([2, 3]) # palauttaa paperi/spock (voittaa 2 + tasapeli)
        if values[1] == max(values):
            if values[1] > values[2]:
                if values[1] > values[3]:
                    if values[1] > values[4]: # kivi yleisin valinta
                        return choice([2, 3]) # palauttaa paperi/spock
                    #kivi/lisko yleisin
                    return 1 # palauttaa kivi (voitto + tasapeli)
                if values[1] > values[4]: # kivi/spock yleisin
                    return 2 # palauttaa paperi (voittaa molemmat)
                # kivi/spock/lisko yleisin
                return 2 # palauttaa paperi (voittaa 2)
            if values[1] > values[3]:
                if values[1] > values[4]: #kivi/paperi yleisin
                    return 2 # palauttaa paperi (voitto + tasapeli)
                # kivi/paperi/lisko yleisin
                return 0 #palauttaa sakset (voittaa 2)
            if values[1] > values[4]: #kivi/paperi/spock
                return 2 # palauttaa paperi (voittaa molemmat + tasapeli)
            #kivi/paperi/spock/lisko yleisin
            return choice([2, 4]) # palauttaa paperi/lisko (voittaa 2 + tasapeli)
        if values[2] == max(values):
            if values[2] > values[3]:
                if values[2] > values[4]: # paperi yleisin valinta
                    return choice([0, 4]) # palauttaa sakset/lisko
                # paperi/lisko yleisin
                return 0 #palauttaa sakset (voittaa molemmat)
            if values[2] > values[4]: # paperi/spock yleisin
                return 4 #palauttaa lisko (voittaa molemmat)
            # paperi/spock/lisko yleisin
            return 4 # palauttaa lisko (voittaa 2 + tasapeli)
        if values[3] == max(values):
            if values[3] > values[4]: # spock yleisin valinta
                return choice([2, 4]) # palauttaa paperi/lisko
            # spock/lisko yleisin
            return 4 # palauttaa lisko (yksi voitto+tasapeli)
        # lisko yleisin valinta
        return choice([0, 1]) # palauttaa sakset/kivi

    def add_choice(self, new_choice):
        """ Lisää valinnan trie-tietorakenteeseen
        Lisää tietorakenteeseen maksimissaan viiden valinnan ketjuja.
        Lisää samalla myös edelliset neljän, kolmen, kahden ja yhden ketjut
        Lisää uusimman valinnan edellisten 10 valinnan listaan
        Lisää myös kokonaisvalintojen lukumäärän

        Args:
            choice (str): pelaajan valinta
        """
        #lisää valinnan jonoon
        self._choices.append(str(new_choice))
        #jos yli 10 jonossa poistaa vanhimman
        if len(self._choices) > 10:
            self._choices.popleft()
        #aloituskohta jonosta mistä tallennettaan valinnat
        #ei haluta tallentaa yli viiden pituisia valintoja
        max_length = 0
        if len(self._choices) > 5:
            max_length = len(self._choices)-5
        #tallennetaan valinnasta 1-5 pituiset jonot triehen
        for i in range(0+max_length, len(self._choices)):
            path = "".join(list(islice(self._choices, i, len(self._choices)+1)))
            #jos valinta on tehty ennenkin päivitetään lukuarvoa yhden ylöspäin
            if self._trie.has_key(path):
                self._trie.update_value(path)
            else:
                #jos valintaa ei ole tehty lisätään polulle solmut
                #ja annetaan lukuarvoksi 1
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
        #lista eripituisten ketjujen voitto/häviömääristä
        winlist = [0, 0, 0, 0, 0, 0]
        #käydään läpi 1-5 pituiset ketjut
        for chain_length in range(1, 6):
            #käydään läpi 5 edellistä valintaa valintalistasta
            for start_point in range(1, 6):
                cpu_choice = self._calculate(chain_length, start_point-1)
                #jos valintaan on vastaavia valintoja triessä tarkistetaan voittaja
                if cpu_choice != 5:
                    result = self.check_winner(int(self._choices[-start_point]), cpu_choice)
                    #jos pelaaja voitti, annetaan tietokoneelle -1 piste
                    if result == "Voitit":
                        winlist[chain_length] -= 1
                    #jos tietokone voitti annetaan tietokoneelle +1 piste
                    elif result == "Hävisit":
                        winlist[chain_length] += 1
        #valitaan eniten voittoja kerännyt ketju, oletuksena 2 pituinen
        max_wins = 0
        best_chain = 2
        for i in range(1, 6):
            if winlist[i] > max_wins:
                max_wins = winlist[i]
                best_chain = i
        return best_chain
