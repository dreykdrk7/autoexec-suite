from config import *
from components.terminal_controller import clear_terminal, position_terminal

if __name__ == '__main__':

    clear_terminal()
    position_terminal(corner=False, center=True, visible_size=[TERMINAL_WIDTH, TERMINAL_HEIGHT])
    print("HAllo")
    
