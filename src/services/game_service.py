class GameService:
    """ Pelin toiminnasta huolehtiva luokka
    """
    def __init__(self):
        """
        win_lose_tie : Voitetut, hävityt, tasapelit
        game_mode : normaali kps (default) tai spock-lisko (2)
        """
        self._win_lose_tie = [0, 0, 0]
        self._game_mode = 1

    def change_game_mode(self, game_mode):
        """ Vaihtaa pelimoodia normaalin ja
        spocl-lisko-variantin välillä

        Args:
            game_mode (int): 1: normi, 2: sl-variantti

        Raises:
            Exception: jos valinta ei ole 1 tai 2
        """
        if game_mode not in [1, 2]:
            raise Exception('Anna valintasi muodossa "1" tai "2"')
        self._game_mode = game_mode

    def statistics(self, winner):
        """ Päivittää tilastot ja palauttaa pelin voittotilastot

        Args:
            winner (str): Pelin voittaja

        Returns:
            list: voittotilasto
            int: pelien kokonaismäärä
        """
        if winner == "Voitit":
            self._win_lose_tie[0] += 1
        elif winner == "Hävisit":
            self._win_lose_tie[1] += 1
        else:
            self._win_lose_tie[2] += 1
        return self._win_lose_tie, sum(self._win_lose_tie)

    def check_command_valid(self, command):
        """ Tarkistaa käyttäjän syötteen oikeellisuuden
            ja palauttaa sen numeerisessa muodossa

        Args:
            command (str): Käyttäjän syöte

        Raises:
            Exception: Virhe jos syöte ei oikeaa muotoa

        Returns:
            int: komento numeerisessa muodossa
        """
        if self._game_mode == 1:
            if command not in ["sakset", "kivi", "paperi", "s", "k", "p"]:
                raise Exception('Anna valintasi muodossa "kivi" tai "k",'\
                    ' "paperi" tai "p" taikka "sakset" tai "s"')
            if command in ["sakset", "s"]:
                return 0
            if command in ["kivi", "k"]:
                return 1
            return 2

        if command not in ["sakset", "kivi", "paperi", "spock", "lisko", \
            "s", "k", "p", "c", "l"]:
            raise Exception('Anna valintasi muodossa "kivi" tai "k",'\
                ' "paperi" tai "p", "sakset" tai "s", "spock" tai "c" taikka "lisko" tai "l" ')
        if command in ["sakset", "s"]:
            return 0
        if command in ["kivi", "k"]:
            return 1
        if command in ["paperi", "p"]:
            return 2
        if command in ["spock", "c"]:
            return 3
        return 4

    def translate_command(self, command):
        """ Palauttaa numeerisen komennon tekstinä

        Args:
            command (int): annettu komento

        Returns:
            str: komento tekstimuodossa
        """
        rps_list = ["sakset", "kivi", "paperi", "spock", "lisko"]
        return rps_list[command]
