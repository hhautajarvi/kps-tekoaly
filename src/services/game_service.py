from random import randint

class GameService:
    def __init__(self):
        self.win_lose_tie = [0, 0, 0]

    def check_winner(self, choice):
        cpu_choice = randint(0, 2)
        if cpu_choice == 0:
            if choice == "kivi":
                self.win_lose_tie[0] += 1
                winner = "Voitit"
            elif choice == "paperi":
                self.win_lose_tie[1] += 1
                winner = "Hävisit"
            elif choice == "sakset":
                self.win_lose_tie[2] += 1
                winner = "Tasapeli"
        if cpu_choice == 1:
            if choice == "kivi":
                self.win_lose_tie[2] += 1
                winner = "Tasapeli"
            elif choice == "paperi":
                self.win_lose_tie[0] += 1
                winner = "Voitit"
            elif choice == "sakset":
                self.win_lose_tie[1] += 1
                winner = "Hävisit"
        if cpu_choice == 2:
            if choice == "kivi":
                self.win_lose_tie[1] += 1
                winner = "Hävisit"
            elif choice == "paperi":
                self.win_lose_tie[2] += 1
                winner = "Tasapeli"
            elif choice == "sakset":
                self.win_lose_tie[0] += 1
                winner = "Voitit"
        return winner, cpu_choice, self.win_lose_tie
