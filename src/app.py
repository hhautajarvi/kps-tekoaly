class App:
    """ Pelilooppi
    """
    def __init__(self, game_service, logic_service, io):
        self.game_service = game_service
        self.logic_service = logic_service
        self.io = io

    def run(self):
        self.io.write("Kirjoita haluamasi valinta. Tyhjä rivi lopettaa pelin.")
        while True:
            chain_length = self.logic_service.find_best_chain_length()
            cpu_pick = self.logic_service.cpu_choice(chain_length)
            command = self.io.read("Valitse kivi (k), paperi (p) tai sakset (s): ").lower()
            if not command:
                break
            try:
                user_pick = self.game_service.check_command_valid(command)
            except Exception as error:
                self.io.write(str(error))
                continue
            try:
                self.logic_service.add_choice(user_pick)
                winner = self.logic_service.check_winner(user_pick, cpu_pick)
                stats = self.game_service.statistics(winner)
                user_choice = self.game_service.translate_command(user_pick)
                cpu_choice = self.game_service.translate_command(cpu_pick)
            except:
                self.io.write("Tapahtui virhe \n Kirjoita haluamasi valinta: kivi (k), paperi (p) tai sakset (s)")
            self.io.write(f"Sinun valintasi: {user_choice} ")
            self.io.write(f"Tietokoneen valinta: {cpu_choice} ")
            self.io.write(f"{winner} ")
            self.io.write(f"Tilastot: voittoja {stats[0]}, häviöitä: {stats[1]},"\
                f" tasapelejä: {stats[2]}")
            self.io.write("* * * * * * * * \n")
