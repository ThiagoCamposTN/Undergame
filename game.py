from engine.core.game_manager import GameManager
from engine.core import config

def main():
    manager = GameManager(config.game_display())
    manager.start()

if __name__ == "__main__":
    # execute only if run as a script
    main()
