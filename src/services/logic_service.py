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
        """  Laskee annetun pituisen Markovin ketjun ja valitsee
        yleisimmän ketjun mukaan siirron jos vastaava edellinen ketju on
        ollut pelaajan siirroissa.

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
            values = [0, 0, 0]
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
                    values.append(self._trie.get_value(f"{path}3"))
                if self._trie.has_key(f"{path}4"):
                    values.append(self._trie.get_value(f"{path}4"))
            return self._check_max_values(values)
        return 5

    def _check_max_values(self, values):
        """ Tarkistetaan missä valintoja on eniten
            ja palautetaan sitä vastaava valinta tai arvotaan jos useampi vaihtoehto

        Args:
            values (_type_): lista ihmisen valintojen määristä

        Returns:
            int: tietokoneen vastaava valinta
        """
        if self._game_mode == 1:
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
        else: # spock-lisko -variantti (vielä keskeneräinen)
            if all(value == values[0] for value in values):
                return randint(0, 4) # kaikkia saman verran
            if values[0] == max(values):
                if values[0] > values[1]:
                    if values[0] > values[2]:
                        if values[0] > values[3]:
                            if values[0] > values[4]: # sakset yleisin valinta
                                return choice([0, 3]) # palauttaa kivi/spock
                    if values[0] > values[3]:
                        if values[0] > values[4]: # sakset/paperi yleisin valinta
                            return choice([0, 1, 3, 4]) # palauttaa sakset/kivi/spock/lisko
                    if values[0] > values[4]: # yleisin valinta sakset/paperi/spock
                        return 4 # palauttaa lisko (voittaa sekä paperi/spock)
                    if values[0] > values[3]: # yleisin valinta sakset/paperi/lisko
                        return choice([0, 1]) # palauttaa sakset/kivi (molemmat voittaa kaksi vaihtoehdoista)

                if values[0] > values[2]:
                    if values[0] > values[3]:
                        if values[0] > values[4]: # sakset/kivi yleisin valinta
                            return 3 # palauttaa spock (voittaa molemmat)
                        # sakset/kivi/spock yleisin valinta
                        return  # palauttaa
                            
            if values[1] == max(values):
                if values[1] > values[0]:
                    if values[1] > values[2]:
                        if values[1] > values[3]:
                            if values[1] > values[4]:
                                return choice([2, 3])
                                # palauttaa paperi/spock koska kivi yleisin valinta
                    return choice([0, 2])
                    # palauttaa paperi tai sakset koska kivi/paperi yleisin valinta
            if values[2] == max(values):
                if values[2] > values[0]:
                    if values[2] > values[1]:
                        if values[2] > values[3]:
                            if values[2] > values[4]:
                                return choice([0, 4])
                                # palauttaa sakset/lisko koska paperi yleisin valinta
            if values[3] == max(values):
                if values[3] > values[0]:
                    if values[3] > values[1]:
                        if values[3] > values[2]:
                            if values[3] > values[4]:
                                return choice([2, 4])
                                # palauttaa paperi/lisko koska spock yleisin valinta
            if values[4] == max(values):
                return choice([0, 1])
                # palauttaa sakset/kivi koska lisko yleisin valinta

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
        for i in range(1, 5):
            if winlist[i] > max_wins:
                max_wins = winlist[i]
                best_chain = i
        return best_chain
