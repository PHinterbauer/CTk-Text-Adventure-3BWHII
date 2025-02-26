# ====================================
# © Paul Hinterbauer 2025 @ TGM Vienna

# ./main.py
# Main file for starting the game
# ====================================

if __name__ == "__main__":
    from gui.design import StartWindow
    from gui.interaction import open_main_window, confirm_player_name
    root = StartWindow(open_main_window, confirm_player_name)
    root.mainloop()