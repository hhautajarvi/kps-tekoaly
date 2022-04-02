from console_io import ConsoleIO
from app import App
from services.game_service import GameService
from services.logic_service import LogicService

def main():
    game_service = GameService()
    logic_service = LogicService()
    console_io = ConsoleIO()
    app = App(game_service, logic_service, console_io)

    app.run()


if __name__ == "__main__":
    main()
