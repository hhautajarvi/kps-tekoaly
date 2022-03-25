from console_io import ConsoleIO
from app import App
from services.game_service import GameService

def main():
    game_service = GameService()
    console_io = ConsoleIO()
    app = App(game_service, console_io)

    app.run()


if __name__ == "__main__":
    main()
