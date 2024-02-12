from config import *
from components.terminal_controller import rename_terminal, clear_terminal, position_terminal
from components.menus import *

actions = None

if __name__ == '__main__':

    clear_terminal()
    rename_terminal()
    position_terminal(corner=False, center=True)
    
    main()
    
