class App:
    """ Pelilooppi
    """
    def __init__(self, game_service, io):
        self.game_service = game_service
        self.io = io

    def run(self):
        self.io.write("Kirjoita haluamasi valinta. Tyhjä rivi lopettaa pelin.")
        while True:
            command = self.io.read("Valitse kivi, paperi tai sakset: ").lower()
            if not command:
                break
            self.game_service.add_choice(command)
            try:
                winner, cpu_choice, stats = self.game_service.check_winner(command)
                self.io.write(f"Sinun valintasi: {command} ")
                self.io.write(f"Tietokoneen valinta: {cpu_choice} ")
                self.io.write(f"{winner} ")
                self.io.write(f"Tilastot: voittoja {stats[0]}, häviöitä: {stats[1]}, tasapelejä: {stats[2]}")
                self.io.write("* * * * * * * * \n")
            except:
                self.io.write("Kirjoita haluamasi valinta: kivi, paperi tai sakset")
