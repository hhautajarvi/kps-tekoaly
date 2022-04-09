class GameService:
    """ Pelin toiminnasta huolehtiva luokka
    """
    def __init__(self):
        """
        win_lose_tie : Voitetut, hävityt, tasapelit
        """
        self._win_lose_tie = [0, 0, 0]

    def statistics(self, winner):
        """ Päivittää tilastot ja palauttaa pelin voittotilastot

        Args:
            winner (str): Pelin voittaja

        Returns:
            list: voittotilasto
        """
        if winner == "Voitit":
            self._win_lose_tie[0] += 1
        elif winner == "Hävisit":
            self._win_lose_tie[1] += 1
        else:
            self._win_lose_tie[2] += 1
        return self._win_lose_tie

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
        if command not in ["sakset", "kivi", "paperi", "s", "k", "p"]:
            raise Exception('Anna valintasi muodossa "kivi" tai "k",'\
                ' "paperi" tai "p" taikka "sakset" tai "s"')
        if command in ["sakset", "s"]:
            return 0
        if command in ["kivi", "k"]:
            return 1
        return 2

    def translate_command(self, command):
        """ Palauttaa numeerisen komennon tekstinä

        Args:
            command (int): annettu komento

        Returns:
            str: komento tekstimuodossa
        """
        rps_list = ["sakset", "kivi", "paperi"]
        return rps_list[command]
