from Controllers.Game_controller import GameController

if __name__ == '__main__':
    width, height = int(input())
    g = GameController(width, height)
    g.start('')
