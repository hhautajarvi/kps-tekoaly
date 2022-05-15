class App:
    """ Pelilooppi
    """
    def __init__(self, game_service, logic_service, io):
        self.game_service = game_service
        self.logic_service = logic_service
        self.io = io

    def run(self):
        self.io.write('Kirjoita haluamasi valinta. "q" tai "quit" lopettaa pelin.')
        while True:
            game_mode = self.io.read("Valitse 1 pelataksesi normaalia kivi-paperi-sakset."\
                " Valitse 2 pelataksesi spock-lisko-varianttia: ").lower()
            if game_mode in ["q", "quit"]:
                return
            try:
                self.game_service.change_game_mode(game_mode)
                game_mode = int(game_mode)
                self.logic_service.change_game_mode(game_mode)
                break
            except Exception as error:
                self.io.write(str(error))
                continue
        while True:
            chain_length = self.logic_service.find_best_chain_length()
            cpu_pick = self.logic_service.cpu_choice(chain_length)
            try:
                if game_mode == 1:
                    command = self.io.read("Valitse kivi (k), paperi (p) tai sakset (s): ").lower()
                if game_mode == 2:
                    command = self.io.read("Valitse kivi (k), paperi (p), sakset (s), " \
                        "spock (c) tai lisko (l): ").lower()
            except:
                self.io.write('Anna valintasi uudestaan')
                continue
            if command in ["q", "quit"]:
                stats, total, choice_stats = self.game_service.end_stats()
                self.io.write(f"Tilastot: yhteensä pelejä: {total}, voittoja: {stats[0]},"\
                    f" häviöitä: {stats[1]}, tasapelejä: {stats[2]}")
                self.io.write(f"Pelasit sakset yhteensä: {sum(choice_stats[0])} kertaa, näistä "\
                    f"voittoja: {choice_stats[0][0]}, häviöitä: {choice_stats[0][1]}, "\
                    f"tasapelejä: {choice_stats[0][2]}")
                self.io.write(f"Pelasit kivi yhteensä: {sum(choice_stats[1])} kertaa, näistä "\
                    f"voittoja: {choice_stats[1][0]}, häviöitä: {choice_stats[1][1]}, "\
                    f"tasapelejä: {choice_stats[1][2]}")
                self.io.write(f"Pelasit paperi yhteensä: {sum(choice_stats[2])} kertaa, näistä "\
                    f"voittoja: {choice_stats[2][0]}, häviöitä: {choice_stats[2][1]}, "\
                    f"tasapelejä: {choice_stats[2][2]}")
                if game_mode == 2:
                    self.io.write(f"Pelasit spock yhteensä: {sum(choice_stats[3])} kertaa, näistä "\
                        f"voittoja: {choice_stats[3][0]}, häviöitä: {choice_stats[3][1]}, "\
                        f"tasapelejä: {choice_stats[3][2]}")
                    self.io.write(f"Pelasit lisko yhteensä: {sum(choice_stats[4])} kertaa, näistä "\
                        f"voittoja: {choice_stats[4][0]}, häviöitä: {choice_stats[4][1]}, "\
                        f"tasapelejä: {choice_stats[4][2]}")
                break
            try:
                user_pick = self.game_service.check_command_valid(command)
            except Exception as error:
                self.io.write(str(error))
                continue
            try:
                self.logic_service.add_choice(user_pick)
                winner = self.logic_service.check_winner(user_pick, cpu_pick)
                user_choice = self.game_service.translate_command(user_pick)
                cpu_choice = self.game_service.translate_command(cpu_pick)
                stats, total = self.game_service.statistics(user_pick, winner)
            except:
                self.io.write("Tapahtui virhe")
                continue
            self.io.write(f"Sinun valintasi: {user_choice} ")
            self.io.write(f"Tietokoneen valinta: {cpu_choice} ")
            self.io.write(f"{winner} ")
            self.io.write(f"Tilastot: pelejä: {total}, voittoja: {stats[0]}, häviöitä: {stats[1]},"\
                f" tasapelejä: {stats[2]}")
            self.io.write("* * * * * * * * * * * * * * * *\n")
