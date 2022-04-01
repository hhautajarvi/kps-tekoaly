class App:
    """ Pelilooppi
    """
    def __init__(self, game_service, io):
        self.game_service = game_service
        self.io = io

    def run(self):
        self.io.write("Kirjoita haluamasi valinta. Tyhjä rivi lopettaa pelin.")
        while True:
            chain_length = self.game_service.find_best_chain_length()
            cpu_pick = self.game_service.cpu_choice(chain_length)
            command = self.io.read("Valitse kivi, paperi tai sakset: ").lower()
            if not command:
                break
            try:
                self.game_service.check_command_valid(command)
            except Exception as error:
                self.io.write(str(error))
                continue
            try:
                self.game_service.add_choice(command)
                winner, cpu_choice = self.game_service.check_winner(command, cpu_pick)
                stats = self.game_service.statistics(winner)
                self.io.write(f"Sinun valintasi: {command} ")
                self.io.write(f"Tietokoneen valinta: {cpu_choice} ")
                self.io.write(f"{winner} ")
                self.io.write(f"Tilastot: voittoja {stats[0]}, häviöitä: {stats[1]}, tasapelejä: {stats[2]}")
                self.io.write("* * * * * * * * \n")
            except:
                self.io.write("Kirjoita haluamasi valinta: kivi, paperi tai sakset")
